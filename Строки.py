word = "Hello"
num = 123
mum = str(num) # присвоение числу строкового значения
print(word, num, sep = ' ')

word1 = "py"
word2 = "th"
word3 = "on"
print(word1 + word2 + word3) # склейка слова

name = "potato"
print(name[0]) #Первый элемент слова ('p')
print(name[2])
# А теперь в обратном порядке
print(name[-1]) #последный элемент слова ('o')
print(name[-2])

srezes = "Python"
print(srezes[0:4:1]) #вывод первых четырех элементов в прямом порядке
print(srezes[4:0:-1]) # вывод последних 4 элементов
print(srezes[::-1]) # Вывод в обратном порядке
print(srezes[:]) # Просто вывод