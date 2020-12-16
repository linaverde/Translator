import lex
import grammar as gr
import earley


class Parser:

    __earley = earley.Earley()

    def __init__(self, lex: lex.LexAnalyzer, g: gr.Grammar):
        self.__lex = lex
        self.__grammar = g

    def parse(self, file):
        lex_list = self.__lex.lex_analysis(file)
        state_list = self.__earley.start(self.__grammar, lex_list)
        print(state_list)
        for st in state_list:
            if not st.afterDot:
                return self.R(state_list, st, len(state_list)-1, [])

    def R(self, states, s: earley.Situation, j: int, pi: []):

        pi.append(self.__grammar.get_rules().index(s))
        k = len(s.beforeDot)
        c = j
        if k == 0:
            return pi
        while (k != 0):
            if self.__grammar.is_terminal(s.beforeDot[k]):
                k = k - 1
                c = c - 1
            elif self.__grammar.is_nonterminal(s.beforeDot[k]):
                # находим ситуацию в I[c]
                for st in states[c]:
                    if not st.afterDot and st.left == s.beforeDot[k]:
                        r = st.get_k
                        Xk = st.left
                        # находим ситуацию в I[r]
                        for nst in states[r]:
                            if nst.left == s.left and nst.beforeDot[-1] == Xk:
                                self.R(states,st, c, pi)
                                k = k - 1
                                c = r
        return pi
