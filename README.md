# Rule-Based System

This Python project implements a simple rule-based system that can add facts and rules, and perform inference based on the given facts and rules.

## Features

- **Fact Management**: Add new facts to the system and save them to a file for persistence.
- **Rule Management**: Create rules with antecedents and consequents, and save them for later use.
- **Inference Engine**: Apply the rules to the known facts to infer new information.

## Usage

1. Run `main()` to start the system.
2. Follow the prompts to add facts and rules, or to perform inference.
3. View the current facts and rules at any time.

## How It Works

The system uses a `Rule` class to represent individual rules, and a `RuleBasedSystem` class to manage the collection of rules and facts. It saves facts and rules to `facts.txt` and `rules.txt` respectively, and uses these files to persist data across sessions.
