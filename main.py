import lex


f = open('main.cpp', 'r')
print(lex.LexAnalyzer.lex_analysis(f))
f.close()