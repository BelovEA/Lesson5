
with open("text.txt", "r", encoding="utf-8" ) as f:
    f = f.readlines()
    for number, word in enumerate(f, 1):
        words = len(word.split())
        print(f"Строка {number} содержит {words} слов")



