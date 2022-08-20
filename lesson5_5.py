from random import randint

with open("task_5.txt", "w+", encoding="utf-8") as task_5:
    task_5.write(" ".join([str(randint(1, 100)) for i in range(1000)]))
    task_5.seek(0)
    print(sum(map(int, task_5.readline().split())))