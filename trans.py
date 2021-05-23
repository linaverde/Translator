from os import get_terminal_size
from termcolor import colored

class trans():
    def __init__(self):
        self.type_dict = {"bool":"bool", "char":"byte", "int":"int",
                          "float":"float32", "double":"float64"}
        
        pass

    def late(self, parsed):
        # parsed - массив
        go_skeleton = self.__main_change(parsed)
        print("-------")
        # print(go_skeleton)
        # go_types = self.types(go_skeleton)
        # self.__to_go(go_types, "test")
        # go_loops = self.loops(go_skeleton)
        go_loops = self.find_and_replace_loop(go_skeleton, 0)
        go_types = self.types(go_loops)
        self.__to_go(go_types, "test")

    def __main_change(self, parsed):
        parsed[0] = ["func",'GO',parsed[0][2]]
        for element in parsed:
            element[2] = int(element[2]) + 2
        parsed = [['package','GO',1], ['main','GO',1]] + parsed
        return parsed

    def types(self, parsed):
        injections = []
        type_arr = []
        start = -1
        for i in range(len(parsed)):
            # [type, name, =, value]
            # [type, name, =, value, ., value]
            # [type, name]
            if parsed[i][1] in ["R1", "R2", "R3", "R4", "R5"]:
                start = i
                print("START:",i)
                type_arr.append(parsed[i])
                foo = True
                k=i+1
                while parsed[k][1] not in ["D3", "D7"]:
                    type_arr.append(parsed[k])
                    k += 1
                end = k
                new_arr = self.transform_type(type_arr)
                injections.append([start, end, new_arr])
                type_arr = []        

        injections.reverse()
        for element in injections:
            parsed[element[0]:element[1]] = element[2]

        return parsed
    
    def transform_type(self, type_arr):
        # type arr variants: 
        # [type, name, =, value]
        # [type, name, =, value, ., value]
        # [type, name]
        new_arr = [["var","GO",type_arr[0][2]]]
        new_arr.append(type_arr[1])
        new_arr.append([self.type_dict[type_arr[0][0]],type_arr[0][1], type_arr[0][2]])
        if len(type_arr) == 2:
            return new_arr
        else:
            return new_arr+type_arr[2:]

    def __select_block(self, start_index, arr, left_edge, right_edge):
        # arr[start_index] always '(' or '{'
        block = []
        print(colored(arr[start_index],"red"))
        local_index = start_index
        recursive = False
        if arr[start_index][0] == left_edge:
            block.append(arr[start_index])
            open_bracket_counter = 1
            local_index += 1
            while open_bracket_counter != 0:
                block.append(arr[local_index])
                if arr[local_index][0] == right_edge:
                    open_bracket_counter -= 1
                elif arr[local_index][0] == left_edge:
                    open_bracket_counter += 1
                if arr[local_index][0] in ["for", "while", "do"]:
                    recursive = True
                local_index += 1
        return block, local_index, recursive

    def find_and_replace_loop(self, parsed, start_point):
        i = start_point
        while i < len(parsed):
            print(colored("-----"+str(i)+"-----"+str(parsed[i]), "cyan"))
            if parsed[i][0] in ["for", "while"]:
                print(colored(parsed[i][0],"cyan"))
                condition, c_end, fake_bool = self.__select_block(i+1, parsed, '(', ')')
                print(colored(condition, "yellow"))
                body, b_end, recursive = self.__select_block(c_end, parsed, '{', '}')
                if recursive:
                    body = self.find_and_replace_loop(body,0)
                print(colored(body, "blue"))
                print(colored([parsed[i][0], condition, body], "green"))
                if body != [] and condition != []:
                    transformed = self.transform_loop([parsed[i], condition, body])
                    print(colored(transformed, "red"))
                    print(colored(parsed[b_end],"red"), b_end)
                    start = i
                    i += len(transformed)
                    parsed[start:b_end] = transformed
                else:
                    i = i + 1
            elif parsed[i][0] == "do":
                body, b_end, recursive = self.__select_block(i+1, parsed, '{', '}')
                if recursive:
                    body = self.find_and_replace_loop(body,0)
                condition, c_end, fake_bool = self.__select_block(b_end+1, parsed, '(', ')')
                print("LAST DO:",colored(parsed[c_end],"cyan"))
                if body != [] and condition != [] and parsed[b_end][0] == "while":
                    transformed = self.transform_loop([parsed[i],body, parsed[b_end],condition])
                    start = i
                    i += len(transformed)
                    parsed[start:c_end] = transformed
                else:
                    i = i + 1
            else:
                i = i + 1
        return parsed

    def transform_loop(self, loop):
        # loops:
        # [for, [condition],[body]]
        # [while, [condition],[body]]
        # [do, [body], while, [condition]]
        new_loop = []
        if loop[0][0] in ["for", "while"]:
            new_loop.append(['for','GO',loop[0][2]])

            start = 1
            
            # redact condition if for
            if loop[0][0] == "for":
                loop[1][3][0] = ":="
                start = 2

            # add condition
            for i in range(start,len(loop[1])-1):
                new_loop.append(loop[1][i])
            
            # add body
            for i in range(len(loop[2])):
                new_loop.append(loop[2][i])

            print(new_loop)
            return new_loop

        elif loop[0][0] == "do":
            cond = ""
            print("loop0: ",loop[0])
            print("loop1: ",loop[1])
            print("loop2: ",loop[2])
            print("loop3: ",loop[3])
            for element in loop[3]:
                cond += str(element[0])
            new_loop.append(["for ok := true; ok; ok = "+cond, 'GO',loop[0][2]])
            for element in loop[1]:
                new_loop.append(element)
            print(new_loop)
            return new_loop


    def __to_go(self, parsed, name):
        # name - string w/o .cpp or .go
        spec = ["N", "D1"]
        open_bracket_count = 0

        f = open(name+".go", "w+")
         
        line_number = 1
        for element in parsed:
            
            if element[0] == "{":
                open_bracket_count += 1
            if element[0] == "}":
                open_bracket_count -= 1

            if int(element[2]) != line_number:
                while (line_number != int(element[2])):
                    line_number += 1
                    f.write("\n"+("\t"*open_bracket_count))
            
            if element[1] in spec:
                f.write(str(element[0]))
            else:
                f.write(str(element[0])+" ")
        
        f.close()