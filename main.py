import courses

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
    chosen_courses.append(str(input(f"Qual curso você escolhe para a {o}ª opção? ")).title())

print(f"Suas escolhas foram de {chosen_courses[0]} para a 1ª opção e {chosen_courses[1]} para a 2ª opção.")