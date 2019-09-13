qa = {"Как дела?": "Хорошооо", "Что делаешь?": "Программирую"}

def ask_user(dela):
    while True:
        dela = input("Как дела? ")
        if dela == 'Хорошо':
            break
        elif dela == dict.keys(qa):
            print(f'{qa["dela"]}')
            break

ask_user(input("Как дела? "))