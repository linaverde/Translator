import lex


f = open('main.cpp', 'r')
l = lex.LexAnalyzer()
print(l.lex_analysis(f))
f.close()