# функция для создания числа из двух чисел постановкой их друг за другом
def fun_list_to_number(a, b):
    str_ = ''
    list_1 = []
    list_1.append(a)
    list_1.append(b)
    for element in list_1:
        str_ += str(element)
    return int(str_)

# функция для преобразования словаря в список, состоящего из элементов (key + каждый элемент списка value)
def fun_dict_to_list(dict_):
    list_ = []
    for key in dict_:
        for element in dict_[key]:
            val = fun_list_to_number(key, element)
            list_.append(val)
    return list_

# функция для поиска пар чисел для пароли
def fun_dict_from_pairs_of_numbers (m):
    dict_ = {}
    for i in range(1, m+1):
        if m % i == 0:
            for j in range(1, int(i/2)+1):
                a = j
                b = i - j
                if a != b and a != 0 and b != 0:
                    if a not in dict_: # создаем пару ключ:значение
                        list_ = []
                        list_.append(b)
                        dict_.update({a: list_})
                    elif a in dict_: # к значению существующего ключа добавляем b
                        b_value = []
                        b_value.extend(dict_[a])
                        b_value.append(b)
                        dict_[a] = b_value
        else:
            continue
    return dict_

n = int(input('Введите число от 3 до 20 '))

dict_pairs_of_numbers = fun_dict_from_pairs_of_numbers(n)
list_result = fun_dict_to_list(dict_pairs_of_numbers)
result = ''
for number in list_result:
    result += str(number)
print(f'Пароль для числа {n}: {result}')


