with open("text_6.txt", "r", encoding="utf-8") as text_6:
    my_dict = {}
    for line in text_6:
        name, amount = line.split(":")
        name_sum = sum(map(int, "".join([i for i in amount if i == " " or "9">= i >= "0"]).split()))
        my_dict[name] = name_sum
print(my_dict)