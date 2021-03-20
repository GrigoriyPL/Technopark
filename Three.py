word = input()
num1 = num2 = 0
d = 0
for i in range(0, 6, 2):
    num1 += int(word[i])
for j in range(1, 6, 2):
    num2 += int(word[j])
print(num1, num2)
if num1 == num2:
    print("True")
else:
    print("False")

    