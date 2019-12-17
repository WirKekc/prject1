import csv

text = []
with open('inst_pws_err.csv') as a:
    reader = csv.reader(a, delimiter=";")
    for line in reader:
        # b = line[1].encode('windows-1251').decode('utf8')
        # print(line)
        text.append(line)


with open('ru_inst_errors.csv', 'w') as f:
    writer = csv.writer(f)
    for i in text:
        i[1] = i[1].encode('windows-1251').decode('utf8')
        print(i)
        writer.writerow(i)
