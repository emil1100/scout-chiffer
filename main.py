
print("scoutchiffer:  ")
print("               ")
print("     S C O U T ")
print("               ")
print("  s  a b c d e ")
print("  c  f g h i j ")
print("  o  k l m n o ")
print("  u  p r s t u ")
print("  t  v y å ä ö ")
print("               ")

s = ["a", "b", "c", "d","e"]
c = ["f", "g", "h", "i","j"]
o = ["k", "l", "m", "n","o"]
u = ["p", "r", "s", "t","u"]
t = ["v", "y", "å", "ä","ö"]

a = 1
gf = 0

x = input("lösa eller göra: ").split()

if x[0] == "lösa":
  x = input("Skriv in skiffer: ").split()
  while a == 1:
    try:
      x[gf] = list(x[gf])
      gf = gf + 1
    except:
      a = 0
  a = gf

  
  for gf in range(a):
    if x[gf][0] == "S":
      x[gf][0] = 0
    elif x[gf][0] == "C":
      x[gf][0] = 1
    elif x[gf][0] == "O":
      x[gf][0] = 2
    elif x[gf][0] == "U":
      x[gf][0] = 3
    elif x[gf][0] == "T":
      x[gf][0] = 4
  print(x)
  for gf in range(a):
    if x[gf][1] == "s":
      x[gf] = s[x[gf][0]]
    elif x[gf][1] == "c":
      x[gf] = c[x[gf][0]]
    elif x[gf][1] == "o":
      x[gf] = o[x[gf][0]]
    elif x[gf][1] == "u":
      x[gf] = u[x[gf][0]]
    elif x[gf][1] == "t":
      x[gf] = t[x[gf][0]]
    print("")
    print("")
    print(x)
  for gf in range(a):
    exec("")

elif x[0] == "göra":
  x = list(input("Skriv in text: "))

print(x)

# Oc Ts Tc Ut StbTs Uo Uu Ct Cu Ss Cu Ou Os To Tu Tu Uu Uu Ss Os So Sc Tt Cu Ts Uo Oo Ct Os So Ts Uu Uu Cu Ts St Co Uc Cc Uu Ts Cu OoUc Uo