import sys


class Term:

    def __init__(self, value: str, lex=""):
        self.value = value
        self.lex = lex

    def value(self):
        return self.value

    def lex(self):
        return self.lex

    def setlex(self, lex):
        self.lex = lex


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
            if self.is_terminal(r.left):
                print(
                    'Rule ' + str(rules.left.value) + '->' + str(rules.right) + ' have mistake: left part is terminal')
                check = False
        if not check:
            sys.exit(2)

    def rules_count(self):
        return len(self.rules)

    def rule_equals(self, r1: Rule, r2: Rule):
        if r1.left.value != r2.left.value or len(r1.right) != len(r2.right):
            return False
        for i, t in enumerate(r1.right):
            if t.value != r2.right[i].value:
                return False
        return True

    def find_rule_number(self, r: Rule):
        for i, rule in enumerate(self.rules):
            if self.rule_equals(r, rule):
                return i
        return -1

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

    def print_rule(self, i):
        rule = self.rules[i]
        s = str(i) + ": " + rule.left.value + "->"
        for t in rule.right:
            s += t.value + " "
        print(s)

    def get_rule(self, i):
        return self.rules[i]
