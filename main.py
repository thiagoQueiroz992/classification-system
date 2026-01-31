import courses

name = "null"
subscription_number = 0
scores = {"linguagens": 0, "matemática": 0, "ciências da natureza": 0, "ciências humanas": 0, "redação": 0}
score_mean = 0

while True:
    try:
        name = str(input("Nome:\n")).title()
    except:
        print("Valor inválido!")
        continue
    else:
        break

for s in scores.keys():
    scores[s] = float(input(f"Qual foi sua nota em {s.title()}? "))