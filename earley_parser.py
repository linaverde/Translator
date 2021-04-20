import lex
import grammar as gr
import earley
import copy
from anytree import RenderTree
from syntax_tree import MyNodeClass
from semantics import CppSemanticsAnalyzer

class Parser:
    __earley = earley.Earley()

    tree = None
    lex_list = []

    def __init__(self, lex: lex.CppLexAnalyzer, g: gr.Grammar):
        self.__lex = lex
        self.__grammar = g
        self.pi = None

    def parse(self, file):
        self.lex_list = self.__lex.lex_analysis(file)
        print(self.lex_list)
        state_list = self.__earley.start(self.__grammar, self.lex_list)
        if type(state_list) is str:
            print(state_list)
            return "Stop parsing"
        print(str(self.__grammar.rules_count()))
        self.pi = self.start_r(state_list)
        self.print_rules()
        print("_______TREE________")
        self.grow_tree()
        sem = CppSemanticsAnalyzer(self.tree)
        sem.check_semantic()


    def R(self, pi, states, s: earley.Situation, j: int):
        rule = gr.Rule(copy.deepcopy(s.left), copy.deepcopy(s.beforeDot))
        pi.append(self.__grammar.find_rule_number(rule))
        # print(pi)
        k = len(s.beforeDot)
        print("k = " + str(k))
        c = j
        print("c = " + str(c))
        while k > 0:
            rightterm = rule.right[k - 1]
            print(rightterm.value)
            if self.__grammar.is_terminal(rightterm):
                k = k - 1
                c = c - 1
                print("k = " + str(k))
                print("c = " + str(c))
            elif self.__grammar.is_nonterminal(rightterm):
                # находим ситуацию в I[c]
                Xk = s.beforeDot[k - 1].value
                A = s.left.value
                searchstate = None
                searchflag = False
                for st in states[c]:
                    if searchflag:
                        break
                    if not st.afterDot and st.left.value == Xk:
                        r = st.get_k()
                        print("r = " + str(r))
                        # находим ситуацию в I[r]
                        print("-------")
                        for nst in states[r]:
                            if nst.left.value == s.left.value \
                                    and nst.afterDot and nst.afterDot[0].value == Xk \
                                    and len(nst.beforeDot) == k - 1:
                                searchstate = st
                                searchflag = True
                                break
                self.R(pi, states, searchstate, c)
                k = k - 1
                c = r
        return pi

    def start_r(self, state_list):
        state = None
        for sit in state_list[-1]:
            if not sit.afterDot and sit.left.value == self.__grammar.s.value:
                state = sit
        return self.R([], state_list, state, len(state_list) - 1)

    def print_rules(self):
        for number in self.pi:
            self.__grammar.print_rule(number)

    def grow_tree(self):
        self.pi.reverse()
        print(self.lex_list)
        first_rule = self.__grammar.get_rule(self.pi.pop())
        self.tree = MyNodeClass(copy.deepcopy(first_rule.left), 0, len(self.pi) + 1, 0)
        new_nodes = []
        for id, item in enumerate(first_rule.right):
            new_nodes.append(MyNodeClass(copy.deepcopy(item), 1, len(self.pi), id, self.tree))
        for item in reversed(new_nodes):
            self.add_children(item.term, item, item.deep)
        self.print_tree()

    def add_children(self, term, parent, depth):
        if self.__grammar.is_terminal(term):
            curr_lex = self.lex_list.pop()
            term.setlex(curr_lex[0])
            return
        else:
            rule = self.__grammar.get_rule(self.pi.pop())
            new_nodes = []
            for id, item in enumerate(rule.right):
                new_nodes.append(MyNodeClass(copy.deepcopy(item), depth + 1, len(self.pi), id, parent))
            for item in reversed(new_nodes):
                self.add_children(item.term, item, item.deep)

    def print_tree(self):
        for pre, fill, node in RenderTree(self.tree):
            treestr = u"%s%s" % (pre, node.term.value)
            if node.term.lex != "":
                print(treestr.ljust(8), node.term.lex, node.deep, node.pi_stack_number, node.right_number)
            else:
                print(treestr.ljust(8), node.deep, node.pi_stack_number, node.right_number)