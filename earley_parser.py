import lex
import grammar as gr
import earley
import copy
from anytree import Node, RenderTree
from syntax_tree import MyNodeClass


class Parser:
    __earley = earley.Earley()

    tree = None

    def __init__(self, lex: lex.CppLexAnalyzer, g: gr.Grammar):
        self.__lex = lex
        self.__grammar = g
        self.pi = []

    def parse(self, file):
        lex_list = self.__lex.lex_analysis(file)
        print(lex_list)
        state_list = self.__earley.start(self.__grammar, lex_list)
        if type(state_list) is str:
            print(state_list)
            return "Stop parsing"
        for sit in state_list[-1]:
            if not sit.afterDot and sit.left.value == self.__grammar.s.value:
                print(str(self.__grammar.rules_count()))
                self.R(state_list, sit, len(state_list) - 1)
                self.print_rules()
                print("_______TREE________")
                self.grow_tree()

    def R(self, states, s: earley.Situation, j: int):
        breaked = False
        rule = gr.Rule(copy.deepcopy(s.left), copy.deepcopy(s.beforeDot))
        self.pi.append(self.__grammar.find_rule_number(rule))
        print(self.pi)
        k = len(s.beforeDot)
        print("k = " + str(k))
        c = j
        print("c = " + str(c))
        if k == 0:
            return self.pi
        while k != 0:
            breaked = False
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
                for st in states[c]:
                    if breaked:
                        break
                    if not st.afterDot and st.left.value == Xk:
                        r = st.get_k()
                        print("r = " + str(r))
                        # находим ситуацию в I[r]
                        print("-------")
                        for nst in states[r]:
                            if breaked:
                                break
                            if nst.left.value == A and nst.afterDot and nst.afterDot[0].value == Xk:
                                self.R(states, st, c)
                                k = k - 1
                                c = r
                                breaked = True
        return self.pi

    def print_rules(self):
        for number in self.pi:
            self.__grammar.print_rule(number)

    def grow_tree(self):
        self.pi.reverse()
        first_rule = self.__grammar.get_rule(self.pi.pop())
        self.tree = MyNodeClass(first_rule.left, 0, len(self.pi) + 1, 0)
        new_nodes = []
        for id, item in enumerate(first_rule.right):
            new_nodes.append(MyNodeClass(item, 1, len(self.pi), id, self.tree))
        for item in reversed(new_nodes):
            self.add_children(item.term, item, item.deep)
        self.print_tree()



    def add_children(self, term, parent, depth):
        if self.__grammar.is_terminal(term):
            return
        else:
            rule = self.__grammar.get_rule(self.pi.pop())
            new_nodes = []
            for id, item in enumerate(rule.right):
                new_nodes.append(MyNodeClass(item, depth+1, len(self.pi), id, parent))
            for item in reversed(new_nodes):
                self.add_children(item.term, item, item.deep)


    def print_tree(self):
        for pre, fill, node in RenderTree(self.tree):
            treestr = u"%s%s" % (pre, node.term.value)
            print(treestr.ljust(8), node.deep, node.pi_stack_number, node.right_number)

