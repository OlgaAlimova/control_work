from animal import Animal


class PackAnimal(Animal):
    def __init__(self, name, commands, birth_date):
        super().__init__(name, commands, birth_date)
        self.category = "Вьючное"
