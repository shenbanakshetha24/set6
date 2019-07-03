d,g=map(int,input().split())
o=list(map(int,input().split()))
count=0
for i in o:
 if(i==g):
  print("yes")
  break
else:
 print("no")
