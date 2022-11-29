def displaynames(lnames):
  for i in lnames:
    print(i)

def displayr(lnames):
  l=len(lnames)
  print("Arrays in reverse order")
  for i in range (l-1,-1,-1):
    print(lnames[i]) 

f=open("lnames.txt", "r" )

name=f.readline()

lnames=[]

while name !="":
  lnames.append(str(name).rstrip(""))
  name=f.readline()
f.close()

displaynames(lnames)
displayr(lnames)