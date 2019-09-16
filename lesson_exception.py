qa = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user():
    while True:
        try:
            dela = input("Как дела? ")
            if dela == 'Хорошо':
                break
            elif dela in dict.keys(qa):
                print(f'{qa[dela]}')
            else:
                print(f'Не понимаю :(')
        except (KeyboardInterrupt):
            print("\nПока!")
            break

ask_user()