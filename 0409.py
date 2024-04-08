from random import randint

money = 50
while money > 0 and money < 100:
    coin = randint(1,2)
    choice = randint(1,2)
    if choice == coin:
        money += 9
    else:
        money -= 10
    print("money:",money)

print("money:",money)