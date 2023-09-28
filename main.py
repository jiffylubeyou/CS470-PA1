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
    print("Guess change strategy wins " + str((wins/iters) * 100) + " percent of the time")

    wins = 0
    for i in range(0, iters):
        winner = random.randint(0, 2)
        guess = random.randint(0, 2)

        if (guess == winner):
            wins = wins + 1
    print("Don't guess change strategy wins " + str((wins/iters) * 100) + " percent of the time")

def diceroll():
    return random.randint(1,6)

def war(i, j, iters):
    # i is number of attacker rolls and j is number of defender rolls
    totalAttackerArmy = 0
    totaldefenderArmy = 0

    for k in range(0,iters):
        attacker = []
        for y in range(0, i):
            attacker.append(diceroll())
        defender = []
        for z in range(0, j):
            defender.append(diceroll())

        attackerArmy = 0
        defenderArmy = 0

        while ((len(attacker) != 0) and len(defender) != 0):
            attack = max(attacker)
            defense = max(defender)

            if (attack > defense):
                defenderArmy = defenderArmy - 1
            else:
                attackerArmy = attackerArmy - 1

            attacker.remove(attack)
            defender.remove(defense)
        totalAttackerArmy = totalAttackerArmy + attackerArmy
        totaldefenderArmy = totaldefenderArmy + defenderArmy

    print("For " + str(i) + " attacker roles and " + str(j) + " defender roles, " + str(totalAttackerArmy / iters) +
          " attacking armies are lost and " + str(totaldefenderArmy / iters) + " defending armies are lost")

def risk():
    iters = 1000

    for i in range(1,4):
        for j in range(1,3):
         war(i, j, iters)


if __name__ == '__main__':
    risk()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
