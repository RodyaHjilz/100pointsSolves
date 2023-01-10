
for a in range(1, 1000000):

    if any(((int(f'2{y}23{x}5',15) + a)%int(f'67{x}9{y}', 13)) == 0 for x in "0123456789ABC" for y in "0123456789ABC"):
        print(a)
        break

#1535 - ответ