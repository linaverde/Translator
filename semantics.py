import copy

from anytree import findall_by_attr
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
        #print("init id", init_id)

        #проверим наличие объявления main
        if 'main' in init_id:
            print("Переобъявление имени main запрещено")
            return False

        #проверка того, что переменная совпадает с ключевым словом, была раньше
        # for id in init_id:
        #     if id in KEYWORD:
        #         print(id, " - имя переменной не может быть ключевым словом")
        #         return False

        #проверим наличие повторяющихся объявлений
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
            if is_repeatable:
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

        #проверяем, что переменные объявлены до использования
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