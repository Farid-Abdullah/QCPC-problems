'''

The story is of a greedy contestant in a programming competetion

the greedy contestant solves n number of problems and then sells all of them.

The problem can be sold at two price points: the Ai or Bi where Ai is the fair price for i'th problem and Bi
is the highest allowed price for the i'th problem.

if the greedy contestant sells the i'th problem, he gets a strike on his reputation. in total he can afford max_penalty number
of strikes. if he goes over, he gets banned from selling ever again.

Now the greedy contestant has to strategize his strikes, in a way where the end profit is highest possible without getting banned

input:
first line is number of test cases
    for every test case:
        a. first line has n and max_penalty, where n is the number of problems, max_penalty is max_affordable strikes
        b. second line is the lowest price point for the problem Ai where (1<= Ai <= 100)
        c. third line has the lowest price point for the problem where (Ai < Bi <= 101)

ouput:
      print the highest Ci where Ci = Ai or Ci = Bi

example:
input:
2
5 3
2 4 1 8 4
8 7 3 9 6
output:
8 7 1 8 6

(or 8 7 3 8 4, because both give the maximum profit which is 30


'''


testcases = int(input("enter the number of test cases: "))

for test in range(testcases):

    line = input("").split(" ")
    problems, max_penalty = int(line[0]), int(line[1])


    fair_price = input().split(" ")
    fair_price = [int(price) for price in fair_price]
    over_price = input().split(" ")
    over_price = [int(price) for price in over_price]
    index = 0
    diff_price=[]
    while index<len(over_price):
        diff_price.append((index,over_price[index]-fair_price[index]))
        index+=1
    
    ThreePenalTuples = sorted(diff_price, key = lambda x:x[1])[max_penalty*-1:]
    penalty_indexes = {pair[0] for pair in ThreePenalTuples} # extracting the indices where i accept there to be a penalty
    

    answer = ""

    for i in range(len(over_price)):
        if i in penalty_indexes:
            answer+= str(over_price[i])+ " "
        else:
            answer+= str(fair_price[i]) + " "
    print(answer[:-1])
            
    
    
        
    
