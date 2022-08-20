dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("translate.txt", "w", encoding="utf-8") as translate:
    with open("text_4.txt", "r", encoding="utf-8") as numbers:
        translate.writelines([line.replace(line.split()[0], dictionary.get(line.split()[0])) for line in numbers])