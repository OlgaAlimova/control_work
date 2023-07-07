import random


class Animal:
    def __init__(self, name, commands, birth_date):
        self.name = name
        self.commands = commands
        self.birth_date = birth_date

    def execute_command(self):
        command = random.choice(self.commands)
        print(f"{self.name} выполняет команду: {command}")

    def learn_command(self, new_command):
        self.commands.append(new_command)
        print(f"{self.name} выучил новую команду: {new_command}")
