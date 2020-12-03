import lex
import grammar as gr
import earley

class Parser:

    __earley = earley.Earley()

    def __init__(self, lex: lex.LexAnalyzer, g: gr.Grammar):
        self.lex = lex
        self.grammar = g

    def parse(self, file):
        lex_list = self.lex.lex_analysis(file)
        state_list = self.__earley.start(self.grammar, lex_list)

    def __R(self, state_list):
        #реализация процедуры R
        return None
