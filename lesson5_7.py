import json
with open("tak_7.json", "w", encoding="utf-8") as task_7_w, open("text_7.txt", encoding="utf-8") as task_7:
    proceeds = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in task_7}
    a = [i for i in proceeds.values() if i > 0]
    average = [proceeds, {"average proceeds": round(sum(a) / len(a))}]

    json.dump(average, task_7_w, ensure_ascii=False, indent=5)