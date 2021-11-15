l = [1,1,1,1,1,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,2,2,2,2,2,2,2,2,2]


a,b,c,d,e=0,0,0,0,0
for i in l:
    if i==1:
        a+=1
    elif i==2:
        b+=1
    elif i==3:
        c+=1
    elif i==4:
        d+=1
    elif i==5:
        e+=1

print(a,b,c,d,e)




d = dict()

for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)


ans = [0]*19

for i in l:
    ans[i]+=1

print(ans)