import lex


f = open('main.cpp', 'r')
print(lex.lex_analysis(f))
f.close()