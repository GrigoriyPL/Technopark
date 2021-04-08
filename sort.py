num = int(input())
mas = []
for k in range (k):
    sym = int(input())
    mas.append(sym)

for i in range(len(mas)-1):
    for j in range(len(mas)-1-i):
        if mas[j] > mas[j+1]:
            mas[j], mas[j+1] = mas[j+1], mas[j]
            print(mas)


# примерочная сортировочная от пероподователя
#             mas = [0,3,5,7,2,1,4,9,6,8]
# for i in range(len(mas)-1):
#     for j in range(len(mas)-1-i):
#         if mas[j] > mas[j+1]:
#             mas[j], mas[j+1] = mas[j+1], mas[j]
#             print(mas)