

'''
3
abc
abcabcxyzabc
abcabc
3


4
xyzfoobarfooxyzabckoko
abcxycfoobarfooxyzkoko
foobarfooxyzabcabckoko
kokokokokoko




'''
n = 4 # hardcodig input for simplicity
strings_list = ['xyzfoobarfooxyzabckoko','abcxycfoobarfooxyzkoko','foobarfooxyzabcabckoko','kokokokokoko']
print(strings_list)

q = int(input())



for i in range(q):# every query:

    query = input().split(" ")

    theString = strings_list[int(query[0])-1]

    SuperDuper = query[1]
    temp = SuperDuper
    count = 0
    
    
    while True:
        if len(temp) > len(theString):
            break
        tempString = theString
        slicer = 0
        while temp in tempString[slicer:]:
            tempString = tempString[slicer:]
            slicer = tempString.find(temp)+1
            if slicer == -1:
                break
            count+=1
            if count>100:
                break
       
        temp+=SuperDuper
        
            
    print(count)
    
    
