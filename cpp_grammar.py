import grammar as gr

def set_nonterm():
    nonterms = []
    nonterms.append(gr.Term("знак типа сложения"))
    # тут заполнить остальнфе нетерминалы
    return nonterms


def set_term():
    terms = []
    terms.append(gr.Term("+"))
    terms.append(gr.Term("-"))
    # тут заполнить остальные терминалы
    return terms


def set_rules():
    rules = []
    rules.append(gr.Rule(gr.Term("знак типа сложения"), gr.Term("+")))
    rules.append(gr.Rule(gr.Term("знак типа сложения"), gr.Term("-")))
    # тут заполнить остальные правила
    return rules


def set_cpp():
    return gr.Grammar(set_rules(), set_nonterm(), set_rules(), gr.Term("программа"))
