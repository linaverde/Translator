import sys

class Term:

    def __init__(self, value: str):
        self.value = value

    def value(self):
        return self.value


class Rule:

    def __init__(self, left: Term, right):
        self.left = left
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class Grammar:

    def __init__(self, rules, nonterminal, terminal, s: Term):
        self.rules = rules
        self.terminal = terminal
        self.nonterminal = nonterminal
        self.s = s
        check = True
        for r in rules:
            if self.is_terminal(r.left) :
                print('Rule '+str(rules.left.value)+'->'+str(rules.right)+' have mistake: left part is terminal')
                check = False
        if not check:
            sys.exit(2)

    def get_rules(self):
        return self.rules

    def get_terms(self):
        return self.terminal + self.nonterminal

    def get_s(self):
        return self.s

    def get_terminal(self):
        return self.terminal

    def get_nonterminal(self):
        return self.nonterminal

    def is_terminal(self, t: Term):
        for term in self.terminal:
            if t.value == term.value:
                return True
        return False

    def is_nonterminal(self, t: Term):
        for term in self.nonterminal:
            if t.value == term.value:
                return True
        return False


