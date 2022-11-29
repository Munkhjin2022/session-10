def displaynameswithscore(lnames, avg):
  for i in range(0,len(lnames),1):
    print(lnames[i] + ' ' + avg[i])


def findName(lnames,avg,response):
  for x in range(0,len(lnames),1):
    if(lnames[x]==response):
      print(lnames[x] + ' ' + avg[x])
    else:
      print('Name not found')
      break


f= open("lnames.txt", "r" )

lnames=[]
avg=[]
 
lines=f.readline()
while lines !="":
  lnames.append(str(lines).rstrip("\n"))
  lines=f.readline()
  avg.append(str(lines).rstrip("\n"))
  lines=f.readline()
 
f.close()
displaynameswithscore(lnames,avg)

response=input("Enter the last name")

while response!="":
  findName(lnames,avg,response)
  response=input("Enter the last name")
