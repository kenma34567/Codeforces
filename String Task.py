Vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
x = input()
x = x.lower()
for i in x:
    if i in Vowels:
        x = x.replace(i, "")
y = ''
for i in range(len(x)):
    y += '.'
    y += x[i]
print(y)
