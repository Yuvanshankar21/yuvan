n,m=map(eval,input().split())
aut=[]
for k in range(n):
  aut.append(list(map(eval,input().split())))
p=[]
o=[]
temp_out=[]
tt=[]
k=0
j=0
o.append(aut[k][j])
p.append([k,j])
while [n-1,m-1] not in p:
  k=0
  for x in p:
    if x[0]+1<n and x[1]+1<m:
      temp_out.append(aut[x[0]+1][x[1]]+o[k])
      temp_out.append(aut[x[0]][x[1]+1]+o[k])
      tt.append([x[0]+1,x[1]])
      tt.append([x[0],x[1]+1])
    elif x[0]+1<n:
      temp_out.append(aut[x[0]+1][x[1]]+o[k])
      tt.append([x[0]+1,x[1]])
    elif x[1]+1<m:
      temp_out.append(aut[x[0]][x[1]+1]+o[k])
      tt.append([x[0],x[1]+1])
    k+=1
  p=tt
  tt=[]
  out=temp_out
  temp_out=[]
print(max(out))
