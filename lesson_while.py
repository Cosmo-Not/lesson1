qa = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user():
    while True:
        dela = input("Как дела? ")
        if dela == 'Хорошо':
            break
        elif dela in dict.keys(qa):
            print(f'{qa[dela]}')
        else:
            print(f'Не понимаю :(')

ask_user()