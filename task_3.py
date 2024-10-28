# Your code here /ᐠ˵- ⩊ -˵マ

person = [
    'Энакин Скайуокер',
    41,
    ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
    {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
]


def main():
    while True:
        user_input = input("Введите номер задания (1-10) или 'выход' для завершения: ")

        if user_input == 'выход':
            break

        task_num = int(user_input)

        if task_num == 1:
            # 1. Фамилия и имя Энакина
            name_parts = person[0].split()
            print(f"Персона: {name_parts[1]}, {name_parts[0]}")

        elif task_num == 2:
            # 2. Возраст Энакина
            print(f"Возраст: {person[1]}")

        elif task_num == 3:
            # 3. Места крупных событий
            print(", ".join(person[2]))

        elif task_num == 4:
            print(f"Количество мест: {len(person[2])}")

        elif task_num == 5:
            print('Звезда Смерти' in person[2])

        elif task_num == 6:
            # 6. Цвет светового меча
            print(f"Цвет светового меча: {person[3]['световой меч']}")

        elif task_num == 7:
            person[1] = 42
            print(f"Возраст: {person[1]}")

        elif task_num == 8:
            if 'Эндор' not in person[2]:
                person[2].append('Эндор')
            print(f"Список мест: {', '.join(person[2])}")

        elif task_num == 9:
            # 9. Проверка на ранг 'лорд ситхов'
            if person[3]['ранг'] == 'лорд ситхов':
                print("Энакин - лорд ситхов")
            else:
                print("Энакин - джедай")

        elif task_num == 10:
            # 10. Проверка количества мест
            if len(person[2]) > 4:
                print("Энакин побывал во многих местах")
            else:
                print("Энакин не так много путешествовал")


main()