my_set = set() # Добавление элементов
my_set.add('a')
my_set.add('b')
my_set.add('c')

print(my_set)

методы удаления элемента

my_set.remove('a') # метод .remove (обязательное наличие элемента)
print(my_set)
my_set.discard('a') # метод .discard (Необязательное наличие элемента)
print(my_set)
my_set.clear() # Удалине всего списка

# Объединения
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set3 = {6, 7, 8}

union = my_set1.union(my_set2, my_set3) # метод .union
print(union)
print("\n")

union1 = my_set1 | my_set2 | my_set3
print(union1) # | объединение

interp = my_set1.intersection(my_set2, my_set3) # .itersection Нахождение общей части у всех множеств
print(interp)

interp_1 = my_set1 & my_set2 & my_set3
print(interp_1)

# Разность

differ = my_set1.difference(my_set2) # Метод .difference выводит только my_set1
print(differ)

differ_1 = my_set1 - my_set2
print (differ_1)

# Симетричная разность
sim = my_set1.symmetric_difference(my_set2) # Метод .symmetric_difference выводит my_set1, my_set2 без пересечения (3)
print(sim)

sim_1 = my_set1 ^ my_set2
print(sim_1)

if my_set1 == my_set2:
    print("Равны")
else:
    print("Не равны")

