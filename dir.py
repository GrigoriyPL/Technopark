print(dir([])) # показывает все методы для данного типа 
help([].insert) # объясняет, что делает тот или иной метод или функция

# f-строки позволяет удобно вводить переменные, в строку

name = "Dima"
age = 16

print(f"Меня зовут {name}. Мне {age} лет ") # пример f-строки

list_of_age = [12, 16, 18]
print(f"Диме {list_of_age[1]}, а Ладе {list_of_age[0]} ")# индексы из масивов

x = 10
y = 20

print(f"New summ is {x} + {y} = {x+y}") # арифметика

###
word = " мало Средне МНОГО "

word.strip().lower() # lower - одинаковый регистр

print(word.strip().lower().replace("о", "ё")) # strip уберает пробелы в начале и конце
print(word)

