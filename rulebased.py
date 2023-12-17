import re
import os

class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = set(antecedents)
        self.consequent = consequent
        self.fired = False

class RuleBasedSystem:
    def __init__(self):
        self.fact_base = set()
        self.rule_base = []
        self.knowledge_base = {}

    def add_fact(self, fact):
        self.fact_base.add(fact)
        check_and_create_file('facts.txt')
        with open('facts.txt', 'a') as file:
            file.write(fact + '\n')

    def add_rule(self, rule):
        self.rule_base.append(rule)
        check_and_create_file('rules.txt')
        with open('rules.txt', 'a') as file:
            file.write('if ' + ' and '.join(rule.antecedents) + ' then ' + rule.consequent + '\n')

    def infer(self):
        while True:
            no_rules_fired = True
            for rule in self.rule_base:
                if not rule.fired and rule.antecedents.issubset(self.fact_base):
                    if rule.consequent not in self.fact_base:
                        self.fact_base.add(rule.consequent)
                        no_rules_fired = False
                        rule.fired = True
            if no_rules_fired:
                break

def check_and_create_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

def process_line(line):
    line = line.lower()
    line = re.sub(r'[^\w\s]', '', line)
    line = re.sub(' +', ' ', line)
    words = line.split()
    if 'if' in words and 'then' in words:
        antecedents = ' '.join(words[words.index('if')+1:words.index('then')]).split(' and ')
        consequent = ' '.join(words[words.index('then')+1:])
        return antecedents, consequent
    return None, None

def load_rules(filename):
    try:
        with open(filename, 'a+') as file:
            file.seek(0)
            lines = file.readlines()
        rules = []
        for line in lines:
            line = process_line(line)
            if line:
                antecedents, consequent = line
                rules.append(Rule(antecedents, consequent))
        return rules
    except IOError:
        print(f"Error opening or reading the file: {filename}")
        return []

def load_facts(filename):
    try:
        with open(filename, 'a+') as file:
            file.seek(0)
            lines = file.readlines()
        facts = [line.strip() for line in lines]
        return facts
    except IOError:
        print(f"Error opening or reading the file: {filename}")
        return []


def main():
    system = RuleBasedSystem()

    rules = load_rules('rules.txt')
    for rule in rules:
        system.add_rule(rule)
    
    facts = load_facts('facts.txt')
    for fact in facts:
        system.add_fact(fact)
    
    while True:
        print("\n=======================================================\n\t\tRULE-BASED SYSTEM\n=======================================================\n[1] Add a fact\t\t[4] View facts\n[2] Add a rule\t\t[5] View rules\n[3] Infer\t\t[6] Quit\n=======================================================\nPlease enter your choice: ")
        choice = input("Your choice: ")
        print("------------------------------------------------------")
        if choice == '1':
            fact = input("Enter a fact: ")
            system.add_fact(fact)
        elif choice == '2':
            rule = input("Enter a rule in 'if...then' format: ")
            antecedents, consequent = process_line(rule)
            if antecedents and consequent:
                system.add_rule(Rule(antecedents, consequent))
            else:
                print("Invalid rule format.")
        elif choice == '3':
            system.infer()
        elif choice == '4':
            print("Facts:")
            for fact in system.fact_base:
                print(fact)
        elif choice == '5':
            print("Rules:")
            for rule in system.rule_base:
                print('if ' + ' and '.join(rule.antecedents) + ' then ' + rule.consequent)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()