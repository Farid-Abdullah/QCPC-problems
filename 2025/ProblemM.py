


'''
In a warehouse, n crates are placed in a row,
Each crate has a weight w,.
The crates need to be rearranged in non-decreasing order by weight.
Arobotic arm can only swap adjacent crates, and every time a swap is performed,
the "stability flag of both crates toggles between Stable and Unstable.
Initially, all crates are Stable. Is it possible to sort the crates such that all are Stable again at the end?
Input
The first line contains a single integert(1<t < 50) the number of test cases.
Each test case consists of two lines: The first line contains an integer n (1 < n < 105) - the number of crates:.
The second line contains n integers w1, w2, ... wn (1 < w, < 109) - the weights of the crates.
The sum of n over all test cases does not exceed 105.
Output For each test case, print "YES" if it's possible to sort the crates and have all flags stable. Otherwise, print
"NO"
'''


def method1():
    ''' I apply the bubble sort algorithm here and check the statuses of all the crates at the end'''

    tests = int(input(""))
    for test in range(tests):
        no_crates = int(input()) # number of crates
        crates = input().split(" ") # just to get them as a list.
        
        crates_flag = [] # will store flags for the crates
        
        for i in range(no_crates):
            crates[i] = int(crates[i])
            crates_flag.append(True)
        crates_sorted = sorted(crates)
      
        position = 0
        while crates != crates_sorted:
            if position>= (no_crates-1):
                position = 0
            if crates[position]>crates[position+1]:
                crates[position],crates[position+1] = crates[position+1],crates[position]
                crates_flag[position],crates_flag[position+1] = not crates_flag[position+1],not crates_flag[position]
            position+=1
            
        if False in crates_flag:
            print("NO")
        else:
            print("YES")
def method2():
    ''' Here i won't do bubble sort, instead i will check how many times a box has to be swapped to be taken to correct sorted position
        if any box is moved odd number of times, just print("NO") '''
    tests = int(input(""))
    for test in range(tests):
        no_crates = int(input()) # number of crates
        crates = input().split(" ")
        for i in range(no_crates):
            crates[i] = (int(crates[i]), i)
      
       
        crates_sorted = sorted(crates, key = lambda x:x[0])
        ans = "YES"
        for crate_index in range(no_crates):
            
            if (crate_index+1-crates_sorted[crate_index][1]+1)%2 == 1:
               
                ans = "NO"
                break
        print(ans)
            
        
