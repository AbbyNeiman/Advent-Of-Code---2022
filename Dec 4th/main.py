

with open('data.txt') as file:
  f = file.read()
def p1(f):
  amt= 0
  x = 0
  y = 0
  t = 0
  dt = f.split('\n')
  for i in dt:
    s = i.split(',')
    sec1 = s[0].split('-')
    sec2 = s[1].split('-')
    v1 = list(range(int(sec1[0],10),int(sec1[1],10)+1))
    v2 = list(range(int(sec2[0],10),int(sec2[1],10)+1))

    for i in v1:
      if i in v2:
        x+=1
      else:
        x = 0
        break
    if x == 0: 
      for i in v2:
        if i in v1:
          x += 1
        else: 
          x=0
          break
    
    if x >= 1:
      amt +=1
## part 2
    for i in v1:
      if i in v2:
        y+=1
      else:
        y += 0
    if y == 0: 
      for i in v2:
        if i in v1:
          x += 1
        else: 
          y += 0
    if y >= 1:
      t += 1
      y=0
  print(t)
  print(amt)

p1(f)
  
  