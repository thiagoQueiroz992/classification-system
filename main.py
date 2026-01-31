import courses

scores = {"linguagens": 0, "matemática": 0, "ciências da natureza": 0, "ciências humanas": 0, "redação": 0}
for s in scores.keys():
    scores[s] = float(input(f"Qual foi sua nota em {s.title()}? "))