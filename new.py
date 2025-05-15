import random

while True:
    son = random.randint(1, 5)
    print(son)
    user=int(input('1,5 gacha ayting'))
    if user==6:
        break
    if user==son:
        print('topdingiz')
    else:
        print("Topolmadiz")

