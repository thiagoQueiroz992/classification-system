import courses, settings

name = "null"
subscription_number = 0
scores = {"linguagens": 0, "matemática": 0, "ciências da natureza": 0, "ciências humanas": 0, "redação": 0}
score_mean = 0
chosen_courses = list()

while True:
    try:
        name = str(input("Nome:\n")).title()
    except:
        print("Valor inválido!")
        continue
    else:
        break

for s in scores.keys():
    while True:
        try:
            scores[s] = float(input(f"Qual foi sua nota em {s.title()}? "))
            if not (0 <= scores[s] <= 1000):
                print("Deve ser um número até 1000!")
                continue
        except:
            print("Valor inválido!")
            continue
        else:
            break

score_mean = sum(scores.values()) / 5
print(f"A sua média foi de {score_mean} pontos.")

for o in range(1, 3):
    chosen_courses.append(courses.courses[settings.answer_generator(o)])

print(f"Suas escolhas foram de {chosen_courses[0]} para a 1ª opção e {chosen_courses[1]} para a 2ª opção.")

while True:
    ans = 0
    try:
        ans = int(input("Quer confirmar a realização da inscrição?\n\t[ 0 ] Sim\n\t[ 1 ] Não\n"))
        if ans not in (0, 1):
            print("Valor inválido!")
            continue
    except:
        print("Valor inválido!")
        continue
    else:
        if ans == 0: break
        else: exit()