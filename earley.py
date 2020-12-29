from inspect import stack

import grammar as gr
import copy


class Situation:

    def __init__(self, k: int, left: gr.Term, afterdot: [], beforedot=None):
        if beforedot is None:
            self.beforeDot = []
        else:
            self.beforeDot = beforedot
        self.k = k
        self.left = left
        if type(afterdot) is list:
            self.afterDot = afterdot
        else:
            self.afterDot = [afterdot]

    def move_dot(self):
        self.beforeDot.append(self.afterDot.pop(0))

    def set_k(self, k: int):
        self.k = k

    def get_k(self):
        return self.k


class Earley:
    __states = []
    __grammar = None
    __lex_list = None
    __pi = []

    def print_state(self, state, j):
        print("State " + str(j))
        printstr = ""
        for sit in state:
            s = ""
            s += str(sit.get_k()) + "," + str(sit.left.value) + "->"
            for beforedot in sit.beforeDot:
                s += beforedot.value + " "
            s += " DOT "
            for afterdot in sit.afterDot:
                s += afterdot.value + " "
            printstr += "[" + s + "], "
        print(printstr + "\n")

    def sit_equals(self, sit1: Situation, sit2: Situation):
        if sit1.left.value != sit2.left.value or len(sit1.afterDot) != len(sit2.afterDot) or len(sit1.beforeDot) != len(
                sit2.beforeDot) or sit1.k != sit2.k:
            return False
        for idx, val in enumerate(sit1.afterDot):
            if val.value != sit2.afterDot[idx].value:
                return False
        for idx, val in enumerate(sit1.beforeDot):
            if val.value != sit2.beforeDot[idx].value:
                return False
        return True

    def check_sit_in_state(self, state: [], sit):
        for s in state:
            if self.sit_equals(s, sit):
                return True
        return False

    def start(self, grammar: gr.Grammar, lex_list):
        self.__grammar = grammar
        self.__lex_list = lex_list
        self.__set_start_state()
        self.print_state(self.__states[0], 0)
        if not self.__states[0]:
            return "ERROR CREATING EARLEY START STATE"
        for j in range(1, len(lex_list) + 1):
            j_state = self.__create_j_state(j, gr.Term(copy.deepcopy(lex_list[j - 1][1])))
            if j_state is None:
                # pos = self.get_pos_in_string(lex_list, lex_list[j - 1], j - 1)
                return "ERROR IN LINE " + str(lex_list[j - 1][2]) + " IN " + str(lex_list[j - 1][0])
            else:
                self.__states.append(copy.deepcopy(j_state))
            last_len = 0
            while last_len != len(self.__states[j]):
                last_len = len(self.__states[j])
                new_state_1 = self.__check_end_dot(j)
                new_state_2 = self.__grow_tree(j)
                if new_state_1 is not None:
                    for n in new_state_1:
                        if not self.check_sit_in_state(self.__states[j], n):
                            self.__states[j].append(copy.deepcopy(n))
                if new_state_2 is not None:
                    for n in new_state_2:
                        if not self.check_sit_in_state(self.__states[j], n):
                            self.__states[j].append(copy.deepcopy(n))
            self.print_state(self.__states[j], j)
        return self.__states

    def __set_start_state(self):
        s = copy.deepcopy(self.__grammar.s)
        state0 = []
        for rule in self.__grammar.get_rules():
            if rule.left.value == s.value:
                state0.append(Situation(0, copy.deepcopy(rule.left), copy.deepcopy(rule.right)))
        if state0:
            self.__states.append(state0)
            last_len = 0
            while last_len != len(self.__states[0]):
                last_len = len(self.__states[0])
                new_state_1 = self.__check_end_dot(0)
                new_state_2 = self.__grow_tree(0)
                if new_state_1 is not None:
                    for n in new_state_1:
                        if not self.check_sit_in_state(self.__states[0], n):
                            self.__states[0].append(copy.deepcopy(n))
                if new_state_2 is not None:
                    for n in new_state_2:
                        if not self.check_sit_in_state(self.__states[0], n):
                            self.__states[0].append(copy.deepcopy(n))
        else:
            self.__states.append(None)

    def __grow_tree(self, j: int):
        last_state = copy.deepcopy(self.__states[j])
        new_state = []
        for sit in last_state:
            if self.__is_dot_before_nt(sit):
                term = copy.deepcopy(sit.afterDot[0])
                for rule in self.__grammar.get_rules():
                    if rule.left.value == term.value:
                        new_state.append(Situation(j, copy.deepcopy(rule.left), copy.deepcopy(rule.right)))
        if new_state:
            return new_state
        return None

    def __create_j_state(self, j: int, t: gr.Term):
        last_state = copy.deepcopy(self.__states[j - 1])
        new_state = []
        for sit in last_state:
            if sit.afterDot:
                if sit.afterDot[0].value == t.value:
                    new_sit = copy.deepcopy(sit)
                    new_sit.move_dot()
                    new_state.append(new_sit)
        if new_state:
            return new_state
        return None

    def __check_end_dot(self, j: int):
        last_state = copy.deepcopy(self.__states[j])
        new_state = []
        for sit in last_state:
            if self.__is_dot_last(sit):
                i_state = copy.deepcopy(self.__states[sit.k])
                for s in i_state:
                    if s.afterDot:
                        if s.afterDot[0].value == sit.left.value:
                            new_sit = copy.deepcopy(s)
                            new_sit.move_dot()
                            new_state.append(new_sit)
        if new_state:
            return new_state
        return None

    def __is_dot_last(self, sit: Situation):
        if not sit.afterDot:
            return True
        return False

    def __is_dot_before_nt(self, sit: Situation):
        if sit.afterDot:
            return self.__grammar.is_nonterminal(sit.afterDot[0])
        return False

    def get_pos_in_string(self, source, lex, pos):
        str_num = lex[2]
        count = 0
        i = pos
        while source[i][2] == str_num:
            count += 1
            i -= 1
        return count
