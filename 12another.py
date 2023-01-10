for g1 in range(0, 50):
    for g2 in range(0, 50):
        for g3 in range(0, 50):
            for g4 in range(0, 50):
                 if(2*g1 + g3 == 2*g2 + g4 and g2 + 2 * g4 == 40 and 2*g3+g1 > 50 and 2*g3+g1 < 53):
                     print(2 * g3 + g1)

#Ответ 52