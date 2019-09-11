age = int(input("Введите ваш возраст: "))

def stage(age):
    if age <= 0:
        return "Возраст должен быть больше 0"
    elif 0 < age < 2:
        return "Вы пока никуда не ходите"
    elif 2 <= age < 7:
        return "Вы ходите в детский сад"
    elif 7 <= age < 17:
        return "Вы учитесь в школе"
    elif 17 <= age < 23:
        return "Вы учитесь в ВУЗе"
    else:
        return "Вы работаете"

result = stage (age)
print(result)