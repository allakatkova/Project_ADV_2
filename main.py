from pprint import pprint
import csv
import re

with open(r"phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

# task 1
for line in contacts_list:
    if " " in line[0]:
        fullname = list(line[0].split(' '))
        for number_w, word in enumerate(fullname):
            line[number_w] = fullname[number_w]
    if " " in line[1]:
        fullname = list(line[1].split(' '))
        for number_w, word in enumerate(fullname):
            line[number_w + 1] = fullname[number_w]

# task 3
for template_line_number, template_line in enumerate(contacts_list):
    verifiable_line_number = len(contacts_list) - 1
    while verifiable_line_number > template_line_number:
        if contacts_list[template_line_number][0] == contacts_list[verifiable_line_number][0]:
            for entry_position, entry in enumerate(contacts_list[verifiable_line_number]):
                if entry != '':
                    template_line[entry_position] = entry
            del contacts_list[verifiable_line_number]
        verifiable_line_number -= 1

# task 2
old_phone_format = r"(8\s?|\+7\s?)\(?(\d+)\)?(\s|\-)?(\d+)(\s|\-)?(\d+)(\s|\-)?(\d+)"
new_phone_format = r"+7(\2)-\4-\6-\8"
old_add_phone_format = r"\(?(доб?)(\.?)(\s)(\d+)\)?"
new_add_phone_format = r"доб.\4"

for line in contacts_list:
    line[5] = re.sub(old_phone_format, new_phone_format, line[5], flags=0)
    line[5] = re.sub(old_add_phone_format,
                     new_add_phone_format, line[5], flags=0)

pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open(r"phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
