# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def coinToss():
    # This returns 0 or 1 at random
    return random.randint(0,1)

def stpetersburg():
    # 0 is heads, 1 is tails
    max = 0
    total = 0
    for i in range(0,300):
        toss = 0
        k = 0
        while (toss == 0):
            toss = coinToss()
            k = k + 1
        money = 2 ** k
        total = total + money
        if (money > max):
            max = money
    print("Average for 300 is " + str(total / 300))
    print("Max for 300 is " + str(max))

    max = 0
    total = 0
    for i in range(0,30000):
        toss = 0
        k = 0
        while (toss == 0):
            toss = coinToss()
            k = k + 1
        money = 2 ** k
        total = total + money
        if (money > max):
            max = money
    print("Average for 300 is " + str(total / 30000))
    print("Max for 300 is " + str(max))

    max = 0
    total = 0
    for i in range(0,3000000):
        toss = 0
        k = 0
        while (toss == 0):
            toss = coinToss()
            k = k + 1
        money = 2 ** k
        total = total + money
        if (money > max):
            max = money
    print("Average for 300 is " + str(total / 3000000))
    print("Max for 300 is " + str(max))

def montyhall():
    wins = 0
    iters = 1000

    for i in range(0,iters):
        winner = random.randint(0,2)
        guess = random.randint(0,2)

        # The guess changing strategy
        randomgoat = random.randint(0,1)
        doors = [0,1,2]
        doors.remove(guess)
        if (winner != doors[0]):
            # goat is revealed on door 0 (of 2 remaining)
            guess = doors[1]
        else:
            # goat is revealed on door 1 (of 2 remaining)
            guess = doors[0]

        if (guess == winner):
            wins = wins + 1
    print("Guess change strategy wins " + str((wins/1000) * 100) + " percent of the time")

    wins = 0
    for i in range(0, iters):
        winner = random.randint(0, 2)
        guess = random.randint(0, 2)

        if (guess == winner):
            wins = wins + 1
    print("Don't guess change strategy wins " + str((wins/1000) * 100) + " percent of the time")



if __name__ == '__main__':
    stpetersburg()
    montyhall()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
