#1
with open("text.txt", "w", encoding="utf-8") as f_obj:
    s = input("введите данные, после ввода пустой строки - ввод завершен ")
    while s != "":
        f_obj.writelines(f"введено через Python - {s}\n")
        s = input("введите данные, после ввода пустой строки - ввод завершен ")