# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    first_group_set = set(participants_first_group.split(delimiter))
    second_group_set = set(participants_second_group.split(delimiter))
    return sorted(list(first_group_set.intersection(second_group_set)))

# TODO Провеьте работу функции с разделителем отличным от запятой

result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)