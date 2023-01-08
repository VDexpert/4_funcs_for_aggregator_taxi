import csv

count = 0
list_duration = []

with open("submission.csv", "r") as File:
    reader = csv.reader(File)
    count = 0
    for i in reader:
        if count >= 1:
            list_duration.append(float(i[1]))
        elif count == 0:
            count += 1
            continue

max_duration = max(list_duration)

def create_special_object(duration_gt=0, duration_gte=0, duration_lt = max_duration, duration_lte = max_duration):
    data_special = []
    with open("submission.csv", "r") as File:
        reader = csv.reader(File)
        count_reader = 0 #переменная для контроля невывода первой строки документа "submission.csv"
        for line in reader:
            if count_reader == 0:
                count_reader += 1
                continue
            else:
                if float(line[1])  > duration_gt and float(line[1]) >= duration_gte and float(line[1]) < duration_lt and float(line[1]) <= duration_lte:
                    data_special.append((line[0], float(line[1])))
    return data_special

data = create_special_object(duration_gt=600, duration_gte=0, duration_lt = 1500, duration_lte = max_duration)

print(len(data))