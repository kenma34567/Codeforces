s = input()
n = int(input())
stick = 0
snow = 0
temp = str()
for i in range(len(s)):
    if s[i] == '?':
        stick += 1
    elif s[i] == '*':
        snow += 1
    else:
        temp += s[i]
j = 0
output = str()
sticksta = stick
snowsta = snow
count = 0
#print(len(s))
#print(snowsta)
#print(sticksta)
for i in range(len(s)):
    if not (s[i] == '?' or s[i] == '*'):
        output += s[i]
        count += 1
        #print(output)
    elif s[i] == '?':
        if snow == 0:
            if len(output)+len(temp)-count > n:
                output = output[:-1]
        elif snow != 0:
            output = output[:-1]
        stick -= 1
    elif s[i] == '*':
        if snow == 1 and len(output) < n:
            for j in range(n - len(temp) + count - len(output)):
                output += s[i - 1]
            #print(len(temp))
            #print("output:", len(output))
            #print(count)
            #print(n - count + (len(s) - count - snowsta - sticksta))
        elif len(output)+len(temp)-count > n:
            output = output[:-1]
        snow -= 1
if (snow == 0 and stick == 0) and len(output) != n:
   print("Impossible")
   exit()
#print(len(output))
print(output)
