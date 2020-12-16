# -*- coding: utf-8 -*-

import grammar as gr


def set_nonterm():
    non_terms_str = ["программа", "объявление переменной", "объявление константы", "значение",
                     "объявление функции", "параметры функции", "значимый тип данных", "тип данных функции",
                     "модификатор типа данных", "тип данных", "буква", "цифра", "целое число", "вещественное число",
                     "число", "прочие символы", "символ идентификатора", "идентификатор", "ид", "тело функции",
                     "возврат значения", "блок кода", "цикл", "тело цикла", "оператор цикла", "ветвление",
                     "символьное значение", "оператор сравнения", "знак типа сложения", "знак типа умножения",
                     "знак унарной операции", "выражение", "E", "T", "F", "логическое значение", "инструкция",
                     "вызов функции", "параметры вызова функции", "оператор присваивания", "присваивание",
                     "главная функция"]
    nonterms = []
    for element in non_terms_str:
        nonterms.append(gr.Term(element))
    return nonterms


def set_term():
    terms_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789(){}[]+-*/%><=!&|;“‘,_#@$^~№:?"
    terms = []
    for symbol in terms_str:
        terms.append(gr.Term(symbol))
    print(terms_str)
    return terms


def set_rules():
    terms_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789(){}[]+-*/%><=!&|;“‘,_#@$^~№:?"
    rules = []
    # Программа ->
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("объявление переменной"), gr.Term("программа")]))
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("объявление функции"), gr.Term("программа")]))
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("объявление константы"), gr.Term("программа")]))
    rules.append(gr.Rule(gr.Term("программа"), gr.Term("главная функция")))

    # объявление переменной
    rules.append(
        gr.Rule(gr.Term("объявление переменной"), [gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term(";")]))
    rules.append(
        gr.Rule(gr.Term("объявление переменной"), [gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term("="),
                                                   gr.Term("значение"), gr.Term(";")]))
    # в документе "тип данных переменной"

    # объявление константы
    rules.append(
        gr.Rule(gr.Term("объявление константы"), [gr.Term("c"), gr.Term("o"), gr.Term("n"), gr.Term("s"), gr.Term("t"),
                                                  gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term("="),
                                                  gr.Term("значение"), gr.Term(";")]))

    # значение
    rules.append(gr.Rule(gr.Term("значение"), gr.Term("число")))
    rules.append(gr.Rule(gr.Term("значение"), gr.Term("символьное значение")))
    rules.append(gr.Rule(gr.Term("значение"), gr.Term("логическое значение")))
    rules.append(gr.Rule(gr.Term("значение"), gr.Term("идентификатор")))
    rules.append(gr.Rule(gr.Term("значение"), gr.Term("вызов функции")))

    # объявление функции
    rules.append(
        gr.Rule(gr.Term("объявление функции"), [gr.Term("тип данных функции"), gr.Term("идентификатор"), gr.Term("("),
                                                gr.Term("параметры функции"), gr.Term(")"), gr.Term("{"),
                                                gr.Term("тело функции"), gr.Term("}")]))
    rules.append(
        gr.Rule(gr.Term("объявление функции"), [gr.Term("тип данных функции"), gr.Term("идентификатор"), gr.Term("("),
                                                gr.Term(")"), gr.Term("{"), gr.Term("тело функции"), gr.Term("}")]))

    # параметры функции
    rules.append(gr.Rule(gr.Term("параметры функции"), [gr.Term("тип данных"), gr.Term("идентификатор")]))
    rules.append(gr.Rule(gr.Term("параметры функции"),
                         [gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term(","), gr.Term("параметры функции")]))

    # Значимый тип данных
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("b"), gr.Term("o"), gr.Term("o"), gr.Term("l")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("c"), gr.Term("h"), gr.Term("a"), gr.Term("r")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("i"), gr.Term("n"), gr.Term("t")]))
    rules.append(
        gr.Rule(gr.Term("значимый тип данных"), [gr.Term("f"), gr.Term("l"), gr.Term("o"), gr.Term("a"), gr.Term("t")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"),
                         [gr.Term("d"), gr.Term("o"), gr.Term("u"), gr.Term("b"), gr.Term("l"), gr.Term("e")]))

    # модификатор типа данных
    rules.append(gr.Rule(gr.Term("модификатор типа данных"),
                         [gr.Term("s"), gr.Term("h"), gr.Term("o"), gr.Term("r"), gr.Term("t")]))
    rules.append(gr.Rule(gr.Term("модификатор типа данных"), [gr.Term("l"), gr.Term("o"), gr.Term("n"), gr.Term("g")]))
    rules.append(gr.Rule(gr.Term("модификатор типа данных"),
                         [gr.Term("s"), gr.Term("i"), gr.Term("g"), gr.Term("n"), gr.Term("e"), gr.Term("d")]))
    rules.append(gr.Rule(gr.Term("модификатор типа данных"),
                         [gr.Term("u"), gr.Term("n"), gr.Term("s"), gr.Term("i"), gr.Term("g"), gr.Term("n"),
                          gr.Term("e"), gr.Term("d")]))

    # тип данных
    rules.append(gr.Rule(gr.Term("тип данных"), [gr.Term("модификатор типа данных"), gr.Term("значимый тип данных")]))
    rules.append(gr.Rule(gr.Term("тип данных"), gr.Term("значимый тип данных")))

    # тип данных функции
    rules.append(gr.Rule(gr.Term("тип данных функции"), gr.Term("тип данных")))
    rules.append(gr.Rule(gr.Term("тип данных функции"), [gr.Term("v"), gr.Term("o"), gr.Term("i"), gr.Term("d")]))

    # буква
    for i in range(0, 52):
        rules.append(gr.Rule(gr.Term("буква"), gr.Term(terms_str[i])))

    # цифра
    for i in range(10):
        rules.append(gr.Rule(gr.Term("цифра"), gr.Term(str(i))))

    # целое число
    rules.append(gr.Rule(gr.Term("целое число"), [gr.Term("цифра"), gr.Term("целое число")]))
    rules.append(gr.Rule(gr.Term("целое число"), gr.Term("цифра")))

    # вещественное число
    rules.append(gr.Rule(gr.Term("вещественное число"), [gr.Term("целое число"), gr.Term("."), gr.Term("целое число")]))

    # число
    rules.append(gr.Rule(gr.Term("число"), gr.Term("целое число")))
    rules.append(gr.Rule(gr.Term("число"), gr.Term("вещественное число")))

    # прочие символы
    for i in range(52, 158):
        rules.append(gr.Rule(gr.Term("прочие символы"), gr.Term(terms_str[i])))

    # символ идентификатора
    rules.append(gr.Rule(gr.Term("символ идентификатора"), gr.Term("буква")))
    rules.append(gr.Rule(gr.Term("символ идентификатора"), gr.Term("_")))

    # идентификатор
    rules.append(gr.Rule(gr.Term("идентификатор"), [gr.Term("символ идентификатора"), gr.Term("ид")]))

    # ид
    rules.append(gr.Rule(gr.Term("ид"), [gr.Term("символ идентификатора"), gr.Term("ид")]))
    rules.append(gr.Rule(gr.Term("ид"), [gr.Term("цифра"), gr.Term("ид")]))
    rules.append(gr.Rule(gr.Term("ид"), gr.Term("символ идентификатора")))
    rules.append(gr.Rule(gr.Term("ид"), gr.Term("цифра")))

    # тело функции
    rules.append(gr.Rule(gr.Term("тело функции"), [gr.Term("блок кода"), gr.Term("возврат значения")]))
    rules.append(gr.Rule(gr.Term("тело функции"), gr.Term("блок кода")))

    # возврат значения
    rules.append(gr.Rule(gr.Term("возврат значения"),
                         [gr.Term("r"), gr.Term("e"), gr.Term("t"), gr.Term("u"), gr.Term("r"), gr.Term("n"),
                          gr.Term("выражение"), gr.Term(";")]))
    rules.append(gr.Rule(gr.Term("возврат значения"),
                         [gr.Term("r"), gr.Term("e"), gr.Term("t"), gr.Term("u"), gr.Term("r"), gr.Term("n"),
                          gr.Term("имя переменной"), gr.Term(";")]))
    rules.append(gr.Rule(gr.Term("возврат значения"),
                         [gr.Term("r"), gr.Term("e"), gr.Term("t"), gr.Term("u"), gr.Term("r"), gr.Term("n"),
                          gr.Term("имя константы"), gr.Term(";")]))

    # блок кода
    rules.append(gr.Rule(gr.Term("блок кода"), [gr.Term("инструкция"), gr.Term("блок кода")]))
    rules.append(gr.Rule(gr.Term("блок кода"), gr.Term("инструкция")))

    # цикл
    rules.append(
        gr.Rule(gr.Term("цикл"), [gr.Term("w"), gr.Term("h"), gr.Term("i"), gr.Term("l"), gr.Term("e"), gr.Term("("),
                                  gr.Term("выражение"), gr.Term(")"), gr.Term("{"), gr.Term("тело цикла"),
                                  gr.Term("}")]))
    rules.append(
        gr.Rule(gr.Term("цикл"), [gr.Term("d"), gr.Term("o"), gr.Term("{"), gr.Term("тело цикла"), gr.Term("}"),
                                  gr.Term("w"), gr.Term("h"), gr.Term("i"), gr.Term("l"), gr.Term("e"), gr.Term("("),
                                  gr.Term("выражение"), gr.Term(")")]))
    rules.append(gr.Rule(gr.Term("цикл"),
                         [gr.Term("f"), gr.Term("o"), gr.Term("r"), gr.Term("("), gr.Term("инструкция"), gr.Term(";"),
                          gr.Term("логическое выражение"), gr.Term(";"), gr.Term("инструкция"), gr.Term(")"),
                          gr.Term("{"), gr.Term("тело цикла"), gr.Term("}")]))

    # тело цикла
    rules.append(
        gr.Rule(gr.Term("тело цикла"), [gr.Term("блок кода"), gr.Term("оператор цикла"), gr.Term("блок кода")]))
    rules.append(gr.Rule(gr.Term("тело цикла"), [gr.Term("оператор цикла"), gr.Term("блок кода")]))
    rules.append(gr.Rule(gr.Term("тело цикла"), [gr.Term("блок кода"), gr.Term("оператор цикла")]))
    rules.append(gr.Rule(gr.Term("тело цикла"), gr.Term("блок кода")))
    rules.append(gr.Rule(gr.Term("тело цикла"), gr.Term("оператор цикла")))

    # оператор цикла
    rules.append(gr.Rule(gr.Term("оператор цикла"),
                         [gr.Term("b"), gr.Term("r"), gr.Term("e"), gr.Term("a"), gr.Term("k"), gr.Term(";")]))
    rules.append(gr.Rule(gr.Term("оператор цикла"),
                         [gr.Term("c"), gr.Term("o"), gr.Term("n"), gr.Term("t"), gr.Term("i"), gr.Term("n"),
                          gr.Term("u"), gr.Term("e"), gr.Term(";")]))

    # ветвление
    rules.append(gr.Rule(gr.Term("ветвление"),
                         [gr.Term("i"), gr.Term("f"), gr.Term("("), gr.Term("выражение"), gr.Term(")"), gr.Term("{"),
                          gr.Term("блок кода"), gr.Term("}")]))
    rules.append(gr.Rule(gr.Term("ветвление"),
                         [gr.Term("i"), gr.Term("f"), gr.Term("("), gr.Term("выражение"), gr.Term(")"), gr.Term("{"),
                          gr.Term("блок кода"), gr.Term("}"), gr.Term("e"), gr.Term("l"), gr.Term("s"), gr.Term("e"),
                          gr.Term("{"), gr.Term("блок кода"), gr.Term("}")]))
    rules.append(gr.Rule(gr.Term("ветвление"),
                         [gr.Term("i"), gr.Term("f"), gr.Term("("), gr.Term("выражение"), gr.Term(")"), gr.Term("{"),
                          gr.Term("блок кода"), gr.Term("}"), gr.Term("e"), gr.Term("l"), gr.Term("s"), gr.Term("e"),
                          gr.Term("ветвление")]))

    # символьное значение
    rules.append(gr.Rule(gr.Term("символьное значение"), [gr.Term("'"), gr.Term("символ"), gr.Term("'")]))
    rules.append(gr.Rule(gr.Term("символьное значение"), [gr.Term("'"), gr.Term("цифра"), gr.Term("'")]))
    rules.append(gr.Rule(gr.Term("символьное значение"), [gr.Term("'"), gr.Term("прочие символы"), gr.Term("'")]))

    # оператор сравнения
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("="), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("!"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term(">"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("<"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), gr.Term(">")))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), gr.Term("<")))

    # мат знак типа сложения
    rules.append(gr.Rule(gr.Term("мат знак типа сложения"), gr.Term("+")))
    rules.append(gr.Rule(gr.Term("мат знак типа сложения"), gr.Term("-")))

    # мат знак типа умножения
    rules.append(gr.Rule(gr.Term("мат знак типа умножения"), gr.Term("*")))
    rules.append(gr.Rule(gr.Term("мат знак типа умножения"), gr.Term("%")))
    rules.append(gr.Rule(gr.Term("мат знак типа умножения"), gr.Term("/")))

    # мат выражение
    rules.append(gr.Rule(gr.Term("мат выражение"), gr.Term("E1")))

    # E1
    rules.append(gr.Rule(gr.Term("E1"), [gr.Term("T1"), gr.Term("мат знак типа сложения"), gr.Term("E1")]))
    rules.append(gr.Rule(gr.Term("E1"), gr.Term("T1")))

    # T1
    rules.append(gr.Rule(gr.Term("T1"), [gr.Term("T1"), gr.Term("мат знак типа умножения"), gr.Term("F1")]))
    rules.append(gr.Rule(gr.Term("T1"), gr.Term("F1")))
    # разве тут не должно быть наподобие предыдущего, F1 мат знак T1 ?

    # F1
    rules.append(gr.Rule(gr.Term("F1"), [gr.Term("("), gr.Term("E1"), gr.Term(")")]))
    rules.append(gr.Rule(gr.Term("F1"), gr.Term("число")))
    rules.append(gr.Rule(gr.Term("F1"), gr.Term("идентификатор")))

    # логическое значение
    rules.append(gr.Rule(gr.Term("логическое значение"), [gr.Term("t"), gr.Term("r"), gr.Term("u"), gr.Term("e")]))
    rules.append(
        gr.Rule(gr.Term("логическое значение"), [gr.Term("f"), gr.Term("a"), gr.Term("l"), gr.Term("s"), gr.Term("e")]))

    # лог знак типа сложения
    rules.append(gr.Rule(gr.Term("лог знак типа сложения"), [gr.Term("|"), gr.Term("|")]))
    rules.append(gr.Rule(gr.Term("лог знак типа сложения"), gr.Term("оператор сравнения")))

    # лог знак типа умножения
    rules.append(gr.Rule(gr.Term("лог знак типа умножения"), [gr.Term("&"), gr.Term("&")]))

    # лог знак унарной операции
    rules.append(gr.Rule(gr.Term("лог знак унарной операции"), gr.Term("!")))

    # лог выражение
    rules.append(gr.Rule(gr.Term("лог выражение"), gr.Term("E2")))

    # E2
    rules.append(gr.Rule(gr.Term("E2"), [gr.Term("T2"), gr.Term("лог знак типа сложения"), gr.Term("E2")]))
    rules.append(gr.Rule(gr.Term("E2"), gr.Term("T2")))
    rules.append(gr.Rule(gr.Term("E2"), [gr.Term("лог знак унарной операции"), gr.Term("T2")]))

    # T2
    rules.append(gr.Rule(gr.Term("T2"), [gr.Term("T2"), gr.Term("лог знак типа умножения"), gr.Term("F2")]))
    rules.append(gr.Rule(gr.Term("T2"), gr.Term("F2")))
    rules.append(gr.Rule(gr.Term("T2"), [gr.Term("лог знак унарной операции"), gr.Term("F2")]))
    # разве тут не должно быть наподобие предыдущего, F2 лог знак T2 ?

    # F2
    rules.append(gr.Rule(gr.Term("F2"), [gr.Term("("), gr.Term("E2"), gr.Term(")")]))
    rules.append(gr.Rule(gr.Term("F2"), gr.Term("значение")))

    # инструкция
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("присваивание"), gr.Term(";")]))
    rules.append(gr.Rule(gr.Term("инструкция"), gr.Term("объявление переменной")))
    rules.append(gr.Rule(gr.Term("инструкция"), gr.Term("объявление константы")))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("вызов функции"), gr.Term(";")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("выражение"), gr.Term(";")]))
    rules.append(gr.Rule(gr.Term("инструкция"), gr.Term("цикл")))
    rules.append(gr.Rule(gr.Term("инструкция"), gr.Term("ветвление")))

    # вызов функции
    rules.append(gr.Rule(gr.Term("вызов функции"), [gr.Term("имя функции"), gr.Term("("), gr.Term(")")]))
    rules.append(gr.Rule(gr.Term("вызов функции"),
                         [gr.Term("имя функции"), gr.Term("("), gr.Term("параметры вызова функции"), gr.Term(")")]))

    # параметры вызова функции
    rules.append(gr.Rule(gr.Term("параметры вызова функции"), gr.Term("выражение")))
    rules.append(gr.Rule(gr.Term("параметры вызова функции"),
                         [gr.Term("выражение"), gr.Term(","), gr.Term("параметры вызова функции")]))

    # оператор присваивания
    rules.append(gr.Rule(gr.Term("оператор присваивания"), gr.Term("=")))
    rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("+"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("-"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("*"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("/"), gr.Term("=")]))
    rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("%"), gr.Term("=")]))

    # присваивание
    rules.append(gr.Rule(gr.Term("присваивание"),
                         [gr.Term("идентификатор"), gr.Term("оператор присваивания"), gr.Term("выражение")]))
    rules.append(gr.Rule(gr.Term("присваивание"),
                         [gr.Term("идентификатор"), gr.Term("оператор присваивания"), gr.Term("идентификатор")]))

    # главная функция
    first = "int main (){"
    arr = []
    for i in first:
        arr.append(gr.Term(i))
    rules.append(
        gr.Rule(gr.Term("главная функция"), arr + [gr.Term("блок кода")] + [gr.Term("возврат значения")] + [gr.Term("}")]))
    # должно работать ))))
    second = "int main (int argc, char *argv[]){"
    darr = []
    for i in second:
        darr.append(gr.Term(i))
    rules.append(
        gr.Rule(gr.Term("главная функция"), darr + [gr.Term("блок кода")] + [gr.Term("возврат значения")] + [gr.Term("}")]))
    # должно работать (((

    return rules


def set_cpp():
    return gr.Grammar(set_rules(), set_nonterm(), set_term(), gr.Term("программа"))
