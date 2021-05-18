# -*- coding: utf-8 -*-

import grammar as gr


def set_nonterm():
    non_terms_str = ["программа", "объявление переменной", "объявление константы",
                     "объявление функции", "параметры функции", "значимый тип данных", "тип данных функции",
                     "модификатор типа данных", "тип данных", "буква", "цифра", "целое число", "вещественное число",
                     "число", "прочие символы", "символ идентификатора", "идентификатор", "ид", "тело функции",
                     "возврат значения", "блок кода", "цикл", "тело цикла", "ветвление",
                     "символьное значение", "оператор сравнения", "знак типа сложения", "знак типа умножения",
                     "знак унарной операции", "выражение", "лог выражение", "мат выражение", "E1", "T1", "F1", "E2",
                     "T2", "F2", "лог значение", "инструкция", "мат знак типа сложения",
                     "мат знак типа умножения",
                     "лог знак типа сложения", "лог знак типа умножения", "лог знак унарной операции",
                     "вызов функции", "параметры вызова функции", "оператор присваивания", "присваивание",
                     "главная функция"]
    nonterms = []
    for element in non_terms_str:
        nonterms.append(gr.Term(element))
    return nonterms


def set_term():
    terms_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789(){}[]+-*/%><=!&|;“‘,_#@$^~№:?"
    terms = []
    terms_array = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8",
                   "K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9", "K10",
                   "D1", "D2", "D3", "D4", "D5", "D6", "D7",
                   "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "O10",
                   "O11", "O12", "O13", "O14", "O15",
                   "N", "C", "ID"]
    for symbol in terms_str:
        terms.append(gr.Term(symbol))
    for element in terms_array:
        terms.append(gr.Term(element))
    return terms


def set_rules():
    terms_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789(){}[]+-*/%><=!&|;“‘,_#@$^~№:?"
    rules = []
    # Программа ->
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("объявление переменной"), gr.Term("программа")]))
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("объявление функции"), gr.Term("программа")]))
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("объявление константы"), gr.Term("программа")]))
    rules.append(gr.Rule(gr.Term("программа"), [gr.Term("главная функция")]))

    # главная функция
    rules.append(
        gr.Rule(gr.Term("главная функция"),
                [gr.Term("R3"), gr.Term("ID"), gr.Term("D6"), gr.Term("D7"), gr.Term("D4"),
                 gr.Term("блок кода"), gr.Term("возврат значения"), gr.Term("D5")]))

    # объявление переменной
    rules.append(
        gr.Rule(gr.Term("объявление переменной"), [gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term("D3")]))

    rules.append(
        gr.Rule(gr.Term("объявление переменной"), [gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term("O15"),
                                                   gr.Term("выражение"), gr.Term("D3")]))
    # в документе "тип данных переменной"

    # объявление константы
    # rules.append(
    #     gr.Rule(gr.Term("объявление константы"), [gr.Term("c"), gr.Term("o"), gr.Term("n"), gr.Term("s"), gr.Term("t"),
    #                                               gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term("="),
    #                                               gr.Term("значение"), gr.Term(";")]))

    # значение
    # rules.append(gr.Rule(gr.Term("значение"), [gr.Term("число")]))
    # rules.append(gr.Rule(gr.Term("значение"), [gr.Term("символьное значение")]))
    # rules.append(gr.Rule(gr.Term("значение"), [gr.Term("логическое значение")]))
    # rules.append(gr.Rule(gr.Term("значение"), [gr.Term("идентификатор")]))
    # rules.append(gr.Rule(gr.Term("значение"), [gr.Term("вызов функции")]))

    # объявление функции
    rules.append(
        gr.Rule(gr.Term("объявление функции"), [gr.Term("тип данных функции"), gr.Term("идентификатор"), gr.Term("D6"),
                                                gr.Term("параметры функции"), gr.Term("D7"), gr.Term("D4"),
                                                gr.Term("тело функции"), gr.Term("D5")]))
    rules.append(
        gr.Rule(gr.Term("объявление функции"), [gr.Term("тип данных функции"), gr.Term("идентификатор"), gr.Term("D6"),
                                                gr.Term("D7"), gr.Term("D4"), gr.Term("тело функции"), gr.Term("D5")]))

    # параметры функции
    rules.append(gr.Rule(gr.Term("параметры функции"), [gr.Term("тип данных"), gr.Term("идентификатор")]))
    rules.append(gr.Rule(gr.Term("параметры функции"),
                         [gr.Term("тип данных"), gr.Term("идентификатор"), gr.Term("D2"),
                          gr.Term("параметры функции")]))

    # Значимый тип данных
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("R1")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("R2")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("R3")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("R4")]))
    rules.append(gr.Rule(gr.Term("значимый тип данных"), [gr.Term("R5")]))

    # модификатор типа данных
    rules.append(gr.Rule(gr.Term("модификатор типа данных"), [gr.Term("K5")]))
    rules.append(gr.Rule(gr.Term("модификатор типа данных"), [gr.Term("K6")]))
    rules.append(gr.Rule(gr.Term("модификатор типа данных"), [gr.Term("K7")]))
    rules.append(gr.Rule(gr.Term("модификатор типа данных"), [gr.Term("K8")]))

    # тип данных
    rules.append(gr.Rule(gr.Term("тип данных"), [gr.Term("модификатор типа данных"), gr.Term("значимый тип данных")]))
    rules.append(gr.Rule(gr.Term("тип данных"), [gr.Term("значимый тип данных")]))

    # тип данных функции
    rules.append(gr.Rule(gr.Term("тип данных функции"), [gr.Term("тип данных")]))
    rules.append(gr.Rule(gr.Term("тип данных функции"), [gr.Term("R6")]))

    # буква
    for i in range(0, 52):
        rules.append(gr.Rule(gr.Term("буква"), [gr.Term(terms_str[i])]))

    # цифра
    for i in range(10):
        rules.append(gr.Rule(gr.Term("цифра"), [gr.Term(str(i))]))

    # целое число
    rules.append(gr.Rule(gr.Term("целое число"), [gr.Term("цифра"), gr.Term("целое число")]))
    rules.append(gr.Rule(gr.Term("целое число"), [gr.Term("цифра")]))

    # вещественное число
    rules.append(
        gr.Rule(gr.Term("вещественное число"), [gr.Term("N"), gr.Term("D1"), gr.Term("N")]))

    # число
    rules.append(gr.Rule(gr.Term("число"), [gr.Term("целое число")]))
    rules.append(gr.Rule(gr.Term("число"), [gr.Term("вещественное число")]))

    # прочие символы
    for i in range(52, 158):
        rules.append(gr.Rule(gr.Term("прочие символы"), [gr.Term(terms_str[i])]))

    # символ идентификатора
    # rules.append(gr.Rule(gr.Term("символ идентификатора"), gr.Term("буква")))
    # rules.append(gr.Rule(gr.Term("символ идентификатора"), gr.Term("_")))

    # идентификатор
    rules.append(gr.Rule(gr.Term("идентификатор"), [gr.Term("ID")]))

    # ид
    # rules.append(gr.Rule(gr.Term("ид"), [gr.Term("символ идентификатора"), gr.Term("ид")]))
    # rules.append(gr.Rule(gr.Term("ид"), [gr.Term("цифра"), gr.Term("ид")]))
    # rules.append(gr.Rule(gr.Term("ид"), gr.Term("символ идентификатора")))
    # rules.append(gr.Rule(gr.Term("ид"), gr.Term("цифра")))

    # тело функции
    rules.append(gr.Rule(gr.Term("тело функции"), [gr.Term("блок кода"), gr.Term("возврат значения")]))
    rules.append(gr.Rule(gr.Term("тело функции"), [gr.Term("блок кода")]))

    # возврат значения
    rules.append(gr.Rule(gr.Term("возврат значения"), [gr.Term("K10"), gr.Term("выражение"), gr.Term("D3")]))
    rules.append(gr.Rule(gr.Term("возврат значения"),
                         [gr.Term("K10"), gr.Term("ID"), gr.Term("D3")]))
    rules.append(gr.Rule(gr.Term("возврат значения"),
                         [gr.Term("K10"), gr.Term("имя константы"), gr.Term("D3")]))

    # блок кода
    rules.append(gr.Rule(gr.Term("блок кода"), [gr.Term("блок кода"), gr.Term("инструкция")]))
    rules.append(gr.Rule(gr.Term("блок кода"), [gr.Term("инструкция")]))

    # цикл
    rules.append(
        gr.Rule(gr.Term("цикл"), [gr.Term("K9"), gr.Term("D6"),
                                  gr.Term("выражение"), gr.Term("D7"), gr.Term("D4"), gr.Term("тело цикла"),
                                  gr.Term("D5")]))
    rules.append(
        gr.Rule(gr.Term("цикл"), [gr.Term("K1"), gr.Term("D4"), gr.Term("тело цикла"), gr.Term("D5"),
                                  gr.Term("K9"), gr.Term("D6"),
                                  gr.Term("выражение"), gr.Term("D7"), gr.Term("D3")]))

    rules.append(gr.Rule(gr.Term("цикл"),
                         [gr.Term("K3"), gr.Term("D6"), gr.Term("инструкция"),
                          gr.Term("лог выражение"), gr.Term("D3"), gr.Term("присваивание"), gr.Term("D7"),
                          gr.Term("D4"), gr.Term("тело цикла"), gr.Term("D5")]))

    rules.append(gr.Rule(gr.Term("цикл"),
                         [gr.Term("K3"), gr.Term("D6"), gr.Term("ID"), gr.Term("D3"),
                          gr.Term("лог выражение"), gr.Term("D3"), gr.Term("присваивание"), gr.Term("D7"),
                          gr.Term("D4"), gr.Term("тело цикла"), gr.Term("D5")]))

    # тело цикла
    # rules.append(
    #    gr.Rule(gr.Term("тело цикла"), [gr.Term("блок кода"), gr.Term("оператор цикла"), gr.Term("блок кода")]))
    # rules.append(gr.Rule(gr.Term("тело цикла"), [gr.Term("оператор цикла"), gr.Term("блок кода")]))
    # rules.append(gr.Rule(gr.Term("тело цикла"), [gr.Term("блок кода"), gr.Term("оператор цикла")]))
    rules.append(gr.Rule(gr.Term("тело цикла"), [gr.Term("блок кода")]))
    # rules.append(gr.Rule(gr.Term("тело цикла"), [gr.Term("оператор цикла")]))

    # оператор цикла
    # rules.append(gr.Rule(gr.Term("оператор цикла"),
    #                      [gr.Term("b"), gr.Term("r"), gr.Term("e"), gr.Term("a"), gr.Term("k"), gr.Term("D3")]))
    # rules.append(gr.Rule(gr.Term("оператор цикла"),
    #                      [gr.Term("c"), gr.Term("o"), gr.Term("n"), gr.Term("t"), gr.Term("i"), gr.Term("n"),
    #                       gr.Term("u"), gr.Term("e"), gr.Term(";")]))

    # ветвление
    rules.append(gr.Rule(gr.Term("ветвление"),
                         [gr.Term("K4"), gr.Term("D6"), gr.Term("выражение"), gr.Term("D7"), gr.Term("D4"),
                          gr.Term("блок кода"), gr.Term("D5")]))
    rules.append(gr.Rule(gr.Term("ветвление"),
                         [gr.Term("K4"), gr.Term("D6"), gr.Term("выражение"), gr.Term("D7"), gr.Term("D4"),
                          gr.Term("блок кода"), gr.Term("D5"), gr.Term("K2"),
                          gr.Term("D4"), gr.Term("блок кода"), gr.Term("D5")]))
    rules.append(gr.Rule(gr.Term("ветвление"),
                         [gr.Term("K4"), gr.Term("D6"), gr.Term("выражение"), gr.Term("D7"), gr.Term("D4"),
                          gr.Term("блок кода"), gr.Term("D5"), gr.Term("K2"),
                          gr.Term("ветвление")]))

    # символьное значение
    rules.append(gr.Rule(gr.Term("символьное значение"), [gr.Term("C")]))
    # rules.append(gr.Rule(gr.Term("символьное значение"), [gr.Term("'"), gr.Term("цифра"), gr.Term("'")]))
    # rules.append(gr.Rule(gr.Term("символьное значение"), [gr.Term("'"), gr.Term("прочие символы"), gr.Term("'")]))

    # оператор сравнения
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("O13")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("O14")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("O11")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("O12")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("O9")]))
    rules.append(gr.Rule(gr.Term("оператор сравнения"), [gr.Term("O10")]))

    # мат знак типа сложения
    rules.append(gr.Rule(gr.Term("мат знак типа сложения"), [gr.Term("O1")]))
    rules.append(gr.Rule(gr.Term("мат знак типа сложения"), [gr.Term("O2")]))

    # мат знак типа умножения
    rules.append(gr.Rule(gr.Term("мат знак типа умножения"), [gr.Term("O3")]))
    rules.append(gr.Rule(gr.Term("мат знак типа умножения"), [gr.Term("O4")]))
    rules.append(gr.Rule(gr.Term("мат знак типа умножения"), [gr.Term("O5")]))

    # мат выражение
    rules.append(gr.Rule(gr.Term("мат выражение"), [gr.Term("E1")]))

    # E1
    rules.append(gr.Rule(gr.Term("E1"), [gr.Term("T1"), gr.Term("мат знак типа сложения"), gr.Term("E1")]))
    rules.append(gr.Rule(gr.Term("E1"), [gr.Term("T1")]))

    # T1
    rules.append(gr.Rule(gr.Term("T1"), [gr.Term("F1"), gr.Term("мат знак типа умножения"), gr.Term("T1")]))
    rules.append(gr.Rule(gr.Term("T1"), [gr.Term("F1")]))
    # разве тут не должно быть наподобие предыдущего, F1 мат знак T1 ?

    # F1
    rules.append(gr.Rule(gr.Term("F1"), [gr.Term("D6"), gr.Term("E1"), gr.Term("D7")]))
    rules.append(gr.Rule(gr.Term("F1"), [gr.Term("N")]))
    rules.append(gr.Rule(gr.Term("F1"), [gr.Term("вещественное число")]))
    rules.append(gr.Rule(gr.Term("F1"), [gr.Term("ID")]))

    # лог знак типа сложения
    rules.append(gr.Rule(gr.Term("лог знак типа сложения"), [gr.Term("O6")]))
    #rules.append(gr.Rule(gr.Term("лог знак типа сложения"), [gr.Term("оператор сравнения")]))

    # лог знак типа умножения
    rules.append(gr.Rule(gr.Term("лог знак типа умножения"), [gr.Term("O7")]))

    # лог знак унарной операции
    rules.append(gr.Rule(gr.Term("лог знак унарной операции"), [gr.Term("O8")]))

    # лог выражение
    rules.append(gr.Rule(gr.Term("лог выражение"), [gr.Term("мат выражение"), gr.Term("оператор сравнения"),
                                                    gr.Term("мат выражение")]))

    rules.append(gr.Rule(gr.Term("лог выражение"), [gr.Term("мат выражение"), gr.Term("O7"),
                                                    gr.Term("мат выражение")]))

    rules.append(gr.Rule(gr.Term("лог выражение"), [gr.Term("мат выражение"), gr.Term("O6"),
                                                    gr.Term("мат выражение")]))

    rules.append(gr.Rule(gr.Term("лог выражение"), [gr.Term("O8"), gr.Term("мат выражение")]))

    rules.append(gr.Rule(gr.Term("лог выражение"),
                         [gr.Term("символьное значение"), gr.Term("оператор сравнения"),
                          gr.Term("символьное значение")]))

    rules.append(gr.Rule(gr.Term("лог выражение"), [gr.Term("лог значение")]))

    # rules.append(gr.Rule(gr.Term("лог выражение"), [gr.Term("E2")]))

    # логическое значение
    rules.append(gr.Rule(gr.Term("лог значение"), [gr.Term("R7")]))
    rules.append(gr.Rule(gr.Term("лог значение"), [gr.Term("R8")]))

    # # E2
    # rules.append(gr.Rule(gr.Term("E2"), [gr.Term("T2"), gr.Term("лог знак типа сложения"), gr.Term("E2")]))
    # rules.append(gr.Rule(gr.Term("E2"), [gr.Term("T2")]))
    # #rules.append(gr.Rule(gr.Term("E2"), [gr.Term("лог знак унарной операции"), gr.Term("T2")]))
    #
    # # T2
    # rules.append(gr.Rule(gr.Term("T2"), [gr.Term("F2"), gr.Term("лог знак типа умножения"), gr.Term("T2")]))
    # rules.append(gr.Rule(gr.Term("T2"), [gr.Term("F2")]))
    # #rules.append(gr.Rule(gr.Term("T2"), [gr.Term("лог знак унарной операции"), gr.Term("F2")]))
    #
    # # F2
    # rules.append(gr.Rule(gr.Term("F2"), [gr.Term("D6"), gr.Term("E2"), gr.Term("D7")]))
    # rules.append(gr.Rule(gr.Term("F2"), [gr.Term("лог знак унарной операции"), gr.Term("E2")]))
    # rules.append(gr.Rule(gr.Term("F2"), [gr.Term("ID")]))
    # rules.append(gr.Rule(gr.Term("F2"), [gr.Term("лог выражение")]))

    # выражение
    rules.append(gr.Rule(gr.Term("выражение"), [gr.Term("лог выражение")]))
    rules.append(gr.Rule(gr.Term("выражение"), [gr.Term("мат выражение")]))
    rules.append(gr.Rule(gr.Term("выражение"), [gr.Term("символьное значение")]))

    # инструкция
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("присваивание"), gr.Term("D3")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("объявление переменной")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("объявление константы")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("вызов функции"), gr.Term("D3")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("выражение"), gr.Term("D3")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("цикл")]))
    rules.append(gr.Rule(gr.Term("инструкция"), [gr.Term("ветвление")]))

    # вызов функции
    rules.append(gr.Rule(gr.Term("вызов функции"), [gr.Term("имя функции"), gr.Term("D6"), gr.Term("D7")]))
    rules.append(gr.Rule(gr.Term("вызов функции"),
                         [gr.Term("имя функции"), gr.Term("D6"), gr.Term("параметры вызова функции"), gr.Term("D7")]))

    # параметры вызова функции
    rules.append(gr.Rule(gr.Term("параметры вызова функции"), [gr.Term("выражение")]))
    rules.append(gr.Rule(gr.Term("параметры вызова функции"),
                         [gr.Term("выражение"), gr.Term(","), gr.Term("параметры вызова функции")]))

    # оператор присваивания
    rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("O15")]))
    # rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("+"), gr.Term("=")]))
    # rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("-"), gr.Term("=")]))
    # rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("*"), gr.Term("=")]))
    # rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("/"), gr.Term("=")]))
    # rules.append(gr.Rule(gr.Term("оператор присваивания"), [gr.Term("%"), gr.Term("=")]))

    # присваивание
    rules.append(gr.Rule(gr.Term("присваивание"),
                         [gr.Term("идентификатор"), gr.Term("оператор присваивания"), gr.Term("выражение")]))
    rules.append(gr.Rule(gr.Term("присваивание"),
                         [gr.Term("идентификатор"), gr.Term("оператор присваивания"), gr.Term("идентификатор")]))

    return rules


def set_cpp():
    return gr.Grammar(set_rules(), set_nonterm(), set_term(), gr.Term("программа"))
