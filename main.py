class FavorieCharacter:
  name = ""
  personalitytraits = ""
  height = ""
  
tv = []  
for r in range(3):
  f = FavorieCharacter
  f.name = int(input("name?"))
  f.personalitytraits = int(input("personalitytraits?"))
  f.height = int(input("height?"))

for r in range(3): 
  print(tv[r].name)

