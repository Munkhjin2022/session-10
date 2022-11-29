def displaynameswithscore(lnames, score):
  for i in range(0,len(lnames),1):
    print(lnames[i] + ' ' + score[i])


f= open("lnames.txt", "r" )

lnames=[]
score=[]

lines=f.readline()

while lines !="":
  lnames.append(str(lines).rstrip(""))
  lines=f.readline()
  score.append(str(lines).rstrip(""))
  lines=f.readline()
  

f.close()

displaynameswithscore(lnames,score)