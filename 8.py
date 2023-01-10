from itertools import product

k = 0
s = ""
for x in product("ПОЛИН", "ПОЛИНА","ПОЛИНА","ПОЛИНА","ПОЛИНА","ПОЛИНА","ПОЛИНА"):
    s = "".join(x)

    # Буквы 'П' и 'А' ДОЛЖНЫ встречаться по одному разу
    if(s.count('А') == 1 and s.count('П') == 1):
        print(s)
        k+=1

print(k)
# Ответ: 36864