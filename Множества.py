name = set() #Пустое множество работает как int, str
animal = {"cat", 5, "dog", 7, "fox", 10, "cat"}
print (animal) #Выводится в одинаковом порядке
print (animal)
print (len(animal)) #Вывод кол-ва элементов
print('\n')

for i in animal:
    print(i)

print("\n")

if "dog" in animal:
    print("Eles in set")
print("\n")

new_elem = "EEEE" # добавление в множество
animal.add(new_elem) # необязательно элемент
animal.add()
print(animal)
