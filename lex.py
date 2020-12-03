import re


# _|\w≈[a-zA-Z]\w+ - регулярка для идентификатора

class LexAnalyzer:

    def lex_analysis(self, source):

        DATATYPES = {'bool': 'R1', 'char': 'R2', 'int': 'R30', 'float': 'R4', 'double': 'R5',
                     'void': 'R6', 'abs': 'R7', 'log': 'R8', 'exp': 'R9',
                     'true': 'R10', 'false': 'R11', }

        KEYWORD = {'do': 'K1', 'else': 'K2', 'for': 'K3', 'if': 'K4', 'long': 'K5', 'short': 'K6',
                   'signed': 'K7', 'unsigned': 'K8', 'while': 'K9', 'return': 'K10'}

        DIVIDER = {'.': 'D1', ',': 'D2', ';': 'D3', '{': 'D4', '}': 'D5', '(': 'D6', ')': 'D7'}

        OPERATOR = {'+': 'O1', '-': 'O2', '*': 'O3', '/': 'O4', '%': 'O5', '||': 'O6', '&&': 'O7', '!': 'O8',
                    '>': 'O9', '<': 'O10', '>=': 'O11', '<=': 'O12', '==': 'O13', '!=': 'O14', '=': 'O15'}

        result = []
        buffer = ''
        i = 0
        for line in source:
            i += 1
            for c in line:
                if c == '&' or c == '|' or c == '<' or c == '>' or c == '!' or c == '=':
                    if buffer != '':
                        if buffer == c and (buffer == '&' or buffer == '|' or buffer == '='):
                            buffer += c
                            result.append((buffer, OPERATOR[buffer]))
                            buffer = ''
                        elif (buffer == '>' or buffer == '<' or buffer == '!') and c == '=':
                            buffer += c
                            result.append([buffer, OPERATOR[buffer], i])
                            buffer = ''
                    else:
                        if c == '&' or c == '|':
                            return 'ERROR IN LINE ' + str(i) + ": WRONG LOGIC OPERATOR " + str(c)
                        else:
                            result.append([c, OPERATOR[c], i])
                elif c in OPERATOR or c in DIVIDER or c == ' ' or c == '\n':
                    if buffer != '':
                        if str.isdigit(buffer):
                            result.append([buffer, 'N', i])
                        elif str.isalpha(buffer):
                            if buffer in KEYWORD:
                                result.append([buffer, KEYWORD[buffer], i])
                            elif buffer in DATATYPES:
                                result.append([buffer, DATATYPES[buffer], i])
                            else:
                                result.append([buffer, 'ID', i])
                        elif re.fullmatch('[_a-zA-Z]\w*', buffer) is not None:
                            result.append([buffer, 'ID', i])
                        else:
                            return 'ERROR IN LINE ' + str(i) + ": WRONG IDENTIFICATION " + str(buffer)
                        buffer = ''
                        if c in OPERATOR:
                            result.append([c, OPERATOR[c], i])
                        elif c in DIVIDER:
                            result.append([c, DIVIDER[c], i])
                    else:
                        if c in OPERATOR:
                            result.append([c, OPERATOR[c], i])
                        elif c in DIVIDER:
                            result.append([c, DIVIDER[c], i])
                elif c == '\'':
                    if buffer == '':
                        buffer += c
                    elif len(buffer) > 2:
                        return 'ERROR IN LINE ' + str(i) + ": WRONG CHAR IN " + str(buffer)
                    else:
                        buffer += c
                        result.append([buffer, 'C', i])
                        buffer = ''
                else:
                    buffer += c

        return result


