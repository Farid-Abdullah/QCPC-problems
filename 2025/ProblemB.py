

c = 0
def endersAndAll(s,al):
    global c
    e = []
    a = al.copy()
    for i in al:
        if s == i:
            c+=1
        elif s.endswith(i):
            e.append(i)
        elif len(s)<len(i) or i not in s:
            a.remove(i) #remove all occurences of i
    return e,a

def divide(pos):
    newPos = []
    count = 0
    stopper = len(pos)
    for p in pos:
        s = p[0]
        if(s == ""):
            count+=1
            stopper-=1
        
        All = p[1].copy()
        enders = p[2].copy()
        for e in enders:
            temp_s = s.removesuffix(e)
            if temp_s != "":
                temp_enders,temp_All = endersAndAll(temp_s,All)
                newPos.append((temp_s,temp_All,temp_enders))
            
    if stopper == 0:
        return count,newPos
    print(newPos)
    return divide(newPos)


#main:
'''
#inputs:
n = int(input())
All = []
for i in range(n):
    a = input()
    All.append(a)

len_s = int(input())
s = input()
'''
#hardcodedInputsForSimplicity:
n = 5
All = ["i","is","show","speed","how"]
len_s = 10
s = "ishowspeed"

enders,All = endersAndAll(s,All)

pos = [(s,All,enders)]
divide(pos)
print(c)




    
            
    
        


    
