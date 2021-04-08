##################################################################

primer = [] # Пустой список
print (primer)
print(type(primer))

priser = [1, 2, 3, 4, 5, 6]
priser_1 = list() # пустой список
print(priser, priser_1)
priser_2 = [1,2,3,4] * 3
print(priser_2)

print(priser[4]) # F по индексам


set_of = {166,25,26}
priser.append(12) #Добавление в массив (список) append - метод добавления
priser.append(14)
priser.append(15)
priser.append(16)
primer.append(set_of)
print(priser)

primer_01=[2, 4, 6, 8, 10]
primer.extend(primer_01) # слияние списков
print(primer) # Вывод слияния

primer_02=[2, 4, 6, 8, 10]
string = "121314"
primer_02.extend(string) # добавляет каждый символ по-элементно
print(primer_02) 

set_of_seth = {'a', 'b', 'c'}
primer_02.extend(set_of_seth)

primer[3] = 1234567
print(primer)

prise_11 =[1,2,3]
prise_11 += [32,21] # добавление в список
print(prise_11)

for i in priser:
    print(i**2)

number = [11,12,13,14,15,16,17,18,19,20]

print (number[1:5]) # Вывод по индексам 5 не в счет


# удаление элемента

del number[::2] # удаление через индекс и через шаг
print(number)
print(number.pop(1)) # удаление через pop pop выводит(запоминает) удаленное число

print(number)

number.remove(16) # remove - удаление конкрентного числа
print(number)

number.insert(1,141)  # замена элемента 1 число индекс 2 значение
print(number)

# clear для удаления всего списка

print(number.sort()) # сортировка списка


new_list = number.copy() # создание копии списка
print(new_list)
