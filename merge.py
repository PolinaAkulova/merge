def merge(*lists):
    new_lists = []
    for list in lists:
        new_lists.extend(list)
    return sorted(new_lists) # xbckj kbcnjd


while True:
    lists = []
    k = int(input('Введите k = '))
    for i in range(k):
        print(i+1, " список (введите значения определенного списка который вам требуется (Вводить строго через пробел)): ")
        nums = [int(i) for i in input('nums = ').split()]
        lists.append(nums)

    print("Вывод - ответ: ", list(merge(*lists)))
