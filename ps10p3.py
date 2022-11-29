def displaynameswithscore(lnames, score):
  for i in range(0,len(lnames),1):
    print(lnames[i] + ' ' + score[i])


f= open("lnames.txt", "r" )

lnames=[]
score=[]

high = 0.0;
low = 101.0;
lowName ='';
highName = '';

lines=f.readline()
while lines !="":
  lnames.append(str(lines).rstrip(""))
  lines=f.readline()
  if float(str(lines).rstrip(""))>high:
    high = float(str(lines).rstrip(""))
    highName = lnames[len(lnames)-1]

  if float(str(lines).rstrip(""))<low:
    low = float(str(lines).rstrip(""))
    lowName = lnames[len(lnames)-1]
  
  score.append(str(lines).rstrip(""))
  lines=f.readline()
  

f.close()

displaynameswithscore(lnames,score)
print ('The highest score is: '+ highName + ' ' + str(high))

print ('The lowest score is: '+ lowName + ' ' + str(low))