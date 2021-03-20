word = "apple"

print(word[0])

print(word[0:3:1]) 
print(word[::-1])

for i in word:
    print(i) # i == word[i]

if "ap" in word: # in :::: not in
    print("True")
else:
    print("False")
