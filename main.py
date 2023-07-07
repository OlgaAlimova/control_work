from animal import Animal
from pet import Pet
from pack_animal import PackAnimal
from counter import Counter

def main():
    counter = Counter()

    try:
        with counter:
            while True:
                print("\n*** Реестр домашних животных ***")
                print("1. Завести новое животное")
                print("2. Определить класс животного")
                print("3. Просмотреть список команд животного")
                print("4. Обучить животное новым командам")
                print("5. Выход")
                choice = input("Введите номер пункта меню: ")

                if choice == "1":
                    animal_name = input("Введите имя животного: ")
                    animal_category = input("Введите категорию животного (кошки, собаки, хомяки, ослы, верблюды или лошади): ")
                    command = input("Введите команду животного: ")
                    birthdate = input("Введите дату рождения животного (гггг-мм-дд): ")

                    if animal_category.lower() == "кошки" or animal_category.lower() == "собаки" or animal_category.lower() == "хомяки":
                        pet = Pet(Animal(animal_name, animal_category, command, birthdate))
                        print("Животное успешно добавлено в класс домашних животных.")
                    elif animal_category.lower() == "ослы" or animal_category.lower() == "верблюды" or animal_category.lower() == "лошади":
                        pack_animal = PackAnimal(Animal(animal_name, animal_category, command, birthdate))
                        print("Животное успешно добавлено в класс вьючных животных.")
                    else:
                        print("Некорректная категория животного.")

                elif choice == "2":
                    animal_name = input("Введите имя животного: ")
                    pet = Pet(Animal(animal_name, "", "", ""))
                    if isinstance(pet.animal, Pet):
                        print("Животное принадлежит классу домашних животных.")
                    else:
                        print("Животное не принадлежит классу домашних животных.")

                elif choice == "3":
                    animal_name = input("Введите имя животного: ")
                    pet = Pet(Animal(animal_name, "", "", ""))
                    if isinstance(pet.animal, Pet):
                        print("Список команд животного:", pet.get_commands())
                    else:
                        print("Животное не принадлежит классу домашних животных.")

                elif choice == "4":
                    animal_name = input("Введите имя животного: ")
                    pet = Pet(Animal(animal_name, "", "", ""))
                    if isinstance(pet.animal, Pet):
                        new_command = input("Введите новую команду для животного: ")
                        pet.add_command(new_command)
                        print("Команда успешно добавлена.")
                    else:
                        print("Животное не принадлежит классу домашних животных.")

                elif choice == "5":
                    break

                else:
                    print("Некорректный выбор. Повторите попытку.")

    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
