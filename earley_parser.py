import lex
import grammar as gr
import earley
import copy
import syntax_tree


class Parser:
    __earley = earley.Earley()

    def __init__(self, lex: lex.CppLexAnalyzer, g: gr.Grammar):
        self.__lex = lex
        self.__grammar = g
        self.pi = []
        self.tree: syntax_tree.Elem = syntax_tree.Elem(None)

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
                self.R(state_list, sit, len(state_list)-1)
                self.print_rules()

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
        pass
        # self.pi.reverse()
        # first_rule = self.__grammar.get_rule(self.pi.pop)
        # self.tree = first_rule.left.value
        # for r in first_rule.right:
        #     self.tree.add
        # for number in self.pi:
        #     rule = self.__grammar.get_rule(number)


