# part 1
rut = {}
num = 0
total = 0
final = []
sack = {}
elf = 0

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with open('data.txt') as file:
    file_contents = file.read()
    bag = file_contents.split('\n')
    for i in bag:
      num += 1
      for x in i:
        rut[num]=i
        

for key, value in rut.items():
  comp_1,comp_2 = value[:len(value)//2], value[len(value)//2:]
  comp1 = [*set(comp_1)]
  comp2 = [*set(comp_2)]
  for i in comp1:
    if i in comp2:
      elf += 1
      sack[elf]=i
    else:
      pass

print(sack.values())
for key, value in sack.items():
  x = ((letter.index(value))+1)
  total = total + x
print('total = ',total)

## part 2
btotal=0
start = 0
end = len(bag)
step = 3
team = 0
teams = {}
badge = []
for i in range(start, end, step):
  x = i
  teams[team] = bag[x:x+step]
  team+=1


for key, value in teams.items():
  team_bags = {}
  elfs = 0
  # print(key ,' -> ',value)
  for items in value:
    team_bags[elfs] = items
    elfs +=1
  E1 = [*set(team_bags[0])]
  E2 = [*set(team_bags[1])]
  E3 = [*set(team_bags[2])]
  for i in E1:
    if i in E2 and i in E3:
      badge.append(i)

print(badge)

for i in badge:
  x = ((letter.index(i))+1)
  btotal = btotal + x
print('b total = ',btotal)
