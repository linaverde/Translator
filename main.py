import earley_parser
import lex
import cpp_grammar
from trans import * 

Trans = trans()
myParser = earley_parser.Parser(lex.CppLexAnalyzer(), cpp_grammar.set_cpp())


f = open('main.cpp', 'r')
parsed = myParser.parse(f)
print(parsed)

Trans.late(parsed)

f.close()