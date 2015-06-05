__author__ = 'Kevin PH'


# used for the game of risk
# simulates out rolls of 3 attacking dice vs 2 defending dice
# stops at a set minimum number of attackers or when the number of attackers / defenders goes lower than a 3 / 2 respectively

from random import randint

listx = []
listy = []

x =0
y =0

att = -2
deff = -3


for i in range(1, 1000):
    listx.append(randint(1,6))
    listy.append(randint(1,6))

for i in range(1, 1000):
    if listx[i -1] > listy[i -1]:
        x+=1
    if listx[i -1] < listy[i -1]:
        y+=1

print("How many attackers?")
att = int(input("attackers = "))

print("What # of att to stop at?")
attmin = int(input("min attackers = "))

print("How many defenders?")
deff = int(input("defenders = "))


i = 0
while att > 3 and deff > 2 and att > attmin:
    i = i + 1
    att1 = listx[3*i -3]
    att2 = listx[3*i -2]
    att3 = listx[3*i -1]
    listatt = [att1, att2, att3]
    listattsort = sorted(listatt)

    def1 = listy[2*i - 2]
    def2 = listy[2*i - 1]
    listdef = [def1, def2]
    listdefsort = sorted(listdef)

    if listdefsort[1] >= listattsort[2]:
        att -=1
    else:
        deff -=1

    if listdefsort[0] >= listattsort[1]:
        att -=1
    else:
        deff -=1


print(att, deff)




