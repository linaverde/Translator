import earley_parser
import lex
import cpp_grammar

myParser = earley_parser.Parser(lex.CppLexAnalyzer(), cpp_grammar.set_cpp())

f = open('main.cpp', 'r')
print(myParser.parse(f))
f.close()