import copy

from anytree import findall_by_attr

import grammar
from syntax_tree import MyNodeClass
from lex import KEYWORD


class CppSemanticsAnalyzer:

    def __init__(self, tree):
        self.__tree = tree

    def start(self):
        pass

    def start_find_by_term_value(self, value):
        res = []
        if self.__tree.term.value == value:
            res.append(self.__tree)
        children = self.__tree.children
        for ch in children:
            self.__find_by_value(ch, value, res)
        return res

    def __find_by_value(self, node, value, res):
        if node.term.value == value:
            res.append(node)
        children = node.children
        # print("children", children)
        for ch in children:
            self.__find_by_value(ch, value, res)

    def __remove_values_from_list(self, the_list, val):
        return [value for value in the_list if value != val]

    def check_semantic(self):
        # собираем все объявления переменных
        initialization_node = self.start_find_by_term_value("объявление переменной")
        init_id = []
        for node in initialization_node:
            leaves = node.leaves
            for l in leaves:
                if l.term.value == 'ID':
                    init_id.append(copy.deepcopy(l.term.lex))
        # print("init id", init_id)

        # проверим наличие объявления main
        if 'main' in init_id:
            print("Переобъявление имени main запрещено")
            return False

        # проверка того, что переменная совпадает с ключевым словом, была раньше
        # for id in init_id:
        #     if id in KEYWORD:
        #         print(id, " - имя переменной не может быть ключевым словом")
        #         return False

        # проверим наличие повторяющихся объявлений
        is_repeatable = len(init_id) != len(set(init_id))
        if is_repeatable:
            d = {}
            # Составим словарь по кол-во повторений
            for i in init_id:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            for k, v in d.items():
                if v > 1:
                    print(f"Переменная {k} объявлена {v} раз!")
                    return False


        # собираем все доступные id
        initialization_node = self.start_find_by_term_value("ID")
        used_id = []
        for node in initialization_node:
            used_id.append(copy.deepcopy(node.term.lex))
        for id in init_id:
            used_id = self.__remove_values_from_list(used_id, id)
        used_id.remove('main')
        if used_id:
            print("Есть необъявленные переменные")
            return False

        # проверяем, что переменные объявлены до использования
        initialization_node = self.start_find_by_term_value("объявление переменной")
        init_id = []
        for node in initialization_node:
            leaves = node.leaves
            for l in leaves:
                if l.term.value == 'ID':
                    init_id.append([copy.deepcopy(l.term.lex), copy.deepcopy(l.pi_stack_number)])
        initialization_node = self.start_find_by_term_value("ID")
        used_id = []
        for node in initialization_node:
            used_id.append([copy.deepcopy(node.term.lex), copy.deepcopy(node.pi_stack_number)])

        for init in init_id:
            id = init[0]
            rule = init[1]
            for used in used_id:
                if used[0] == id and used[1] < rule:
                    print("Переменная", id, "используется в программе до объявления")
                    return False

    def find_max_deep(self, node, curr_deep):
        if node.deep > curr_deep:
            curr_deep = node.deep
        children = node.children
        for ch in children:
            curr_deep = self.find_max_deep(ch, curr_deep)
        return curr_deep

    def find_leaves_with_deep(self, node, deep):
        res = []
        for l in node.leaves:
            if l.deep == deep:
                res.append(l)
        return res

    def optimizer(self):
        # находим все математические выражения, которые надо свернуть
        math_value = self.start_find_by_term_value("мат выражение")
        for m in math_value:
            leaves = m.leaves
            line = leaves[0].term.line
            id = False
            for l in leaves:
                if l.term.value == "ID":
                    id = True
                    break
            if not id:
                print("math", m.term.value, m.pi_stack_number)
                math_start = m.children[0]
                res = self.do_math(math_start)
                math_start.parent = None
                if res[0] == 'int':
                    MyNodeClass(grammar.Term(value='N', lex=res[1], line=line), None, None, None, m)
                else:
                    s = str(res[1]).split('.')
                    print(s)
                    MyNodeClass(grammar.Term(value='N', lex=s[0], line=line), None, None, None, m)
                    MyNodeClass(grammar.Term(value='D1', lex='.', line=line), None, None, None, m)
                    MyNodeClass(grammar.Term(value='N', lex=s[1], line=line), None, None, None, m)


    __operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    def do_math(self, branch):
        children = branch.children
        print('curr branch', branch.term.value)
        if not children:
            if branch.term.value == "N":
                return ["int", branch.term.lex]
            elif branch.term.value[0] == 'O':
                return ["operator", branch.term.lex]
            else:
                return "hehe"
        else:
            l = len(children)
            t = branch.term.value
            if l == 3 and t == 'вещественное число':
                new_float = str(children[0].term.lex) + '.' + str(children[2].term.lex)
                print('new float', new_float)
                return ["float", new_float]
            elif len(children) == 3 and (t == "E1" or t == "T1"):
                btw = children[1].term.value
                if btw == "мат знак типа сложения" or btw == "мат знак типа умножения":
                    operator = self.do_math(children[1])
                    left = self.do_math(children[0])
                    right = self.do_math(children[2])
                    print("op", operator, "left", left, "right", right)

                    if left[0] == "int":
                        left = int(left[1])
                    elif left[0] == "float":
                        left = float(left[1])

                    if right[0] == "int":
                        right = int(right[1])
                    elif right[0] == "float":
                        right = float(right[1])

                    result = self.__operations[operator[1]](left, right)
                    print("result", result)
                    print("type", type(result).__name__)
                    return [type(result).__name__, result]
            elif len(children) == 3 and t == "F1":
                return self.do_math(children[1])
            elif children:
                for ch in children:
                    return self.do_math(ch)
