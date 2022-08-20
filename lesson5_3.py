with open("text_3.txt", "r", encoding="utf-8") as income:
    salary = {line.split()[0]: float(line.split()[1]) for line in income}
    print(f"Средняя заработная плата = {round(sum(salary.values()) / len(salary), 2)}\n"
          f"Из списка сотрудники с заработной платой ниже 20к -{[el[0] for el in salary.items() if el[1] < 20000]}")