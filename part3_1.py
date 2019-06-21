tekst = input()
regist = len(tekst)
lower = upper = 0
for i in tekst:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
per_lower = lower / regist * 100
per_upper = upper / regist * 100
print (int(per_lower))
print (int(per_upper))
