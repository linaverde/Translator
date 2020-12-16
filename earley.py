from inspect import stack

import grammar as gr


class Situation:

    def __init__(self, k: int, left: gr.Term, afterdot: [], beforedot=None):
        if beforedot is None:
            self.beforeDot = []
        self.k = k
        self.left = left
        self.afterDot = afterdot

    def move_dot(self):
        self.beforeDot.append(self.afterDot.pop(0))

    def set_k(self, k: int):
        self.k = k

    def get_k(self):
        return self.k


class Earley:
    __states = []
    __grammar = None
    __string = None
    __pi = []

    def start(self, grammar: gr.Grammar, string: []):
        self.__grammar = grammar
        self.__string = string
        self.__set_start_state()
        self.__pi = []
        if self.__states[0] is None:
            return "ERROR CREATING EARLEY START STATE"
        for j in range(1, len(string) + 1):
            j_state = self.__create_j_state(j, string[j - 1][1])
            if j_state is None:
                pos = self.get_pos_in_string(string, string[j - 1], j - 1)
                return "ERROR IN LINE " + str(string[j - 1][2]) + " IN POSITION " + str(pos)
            new_state_1 = [0]
            new_state_2 = [0]
            while new_state_1 is not None or new_state_2 is not None:
                new_state_1 = self.__check_end_dot(j)
                new_state_2 = self.__grow_tree(j)
                if new_state_1 is not None:
                    j_state = list(set(new_state_1 + j_state))
                if new_state_2 is not None:
                    j_state = list(set(new_state_2 + j_state))
            self.__states.append(j_state)
        return self.__states

    def __set_start_state(self):
        s = self.__grammar.s
        state0 = []
        for rule in self.__grammar.get_rules():
            if rule.left == s:
                state0.append(Situation(0, rule.left, rule.right))
        if not state0:
            new_state_1 = [0]
            new_state_2 = [0]
            while new_state_1 is not None or new_state_2 is not None:
                new_state_1 = self.__check_end_dot(0)
                new_state_2 = self.__grow_tree(0)
                if new_state_1 is not None:
                    state0 = list(set(new_state_1 + state0))
                if new_state_2 is not None:
                    state0 = list(set(new_state_2 + state0))
            self.__states.append(state0)
        else:
            self.__states.append(None)

    def __grow_tree(self, j: int):
        last_state = self.__states[j]
        new_state = []
        for sit in last_state:
            if self.__is_dot_before_nt(sit):
                term = sit.afterDot[0]
                for rule in self.__grammar.get_rules():
                    if rule.left == term:
                        new_state.append(Situation(0, rule.left, rule.right))
        if new_state:
            return new_state
        return None

    def __create_j_state(self, j: int, t: gr.Term):
        last_state = self.__states[j - 1]
        new_state = []
        for sit in last_state:
            if sit.afterDot[0] == t:
                new_sit = sit
                new_sit.move_dot()
                new_state.append(new_sit)
        if new_state:
            return new_state
        return None

    def __check_end_dot(self, j: int):
        last_state = self.__states[j]
        new_state = []
        for sit in last_state:
            if self.__is_dot_last(sit):
                i_state = self.__states[sit.k]
                for s in i_state:
                    if s.afterDot[0] == sit.left:
                        new_sit = s
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
        if self.__grammar.is_nonterminal(sit.afterDot[0]):
            return True
        return False

    def get_pos_in_string(self, source, lex, pos):
        str_num = lex[2]
        count = 0
        i = pos
        while source[i][2] == str_num:
            count += 1
            i -= 1
        return count

    def R(self, s: Situation, j: int):

        self.__pi.append(self.__grammar.get_rules().index(s))
        k = len(s.beforeDot)
        c = j
        if k == 0:
            return self.__pi
        while (k != 0):
            if self.__grammar.is_terminal(s.beforeDot[k]):
                k = k - 1
                c = c - 1
            elif self.__grammar.is_nonterminal(s.beforeDot[k]):
                # находим ситуацию в I[c]
                for st in self.__states[c]:
                    if self.__is_dot_last(st) and st.left == s.beforeDot[k]:
                        r = st.get_k
                        Xk = st.left
                        # находим ситуацию в I[r]
                        for nst in self.__states[r]:
                            if nst.left == s.left and nst.beforeDot[-1] == Xk:
                                self.R(st, c)
                                k = k - 1
                                c = r
        return self.__pi