


'''
Qassem is not a fan of coffee, but he is facing challenge that might require him to drink it.
He is a student in the engineering faculty, where many important lectures are scheduled.
Each lecture is defined by when it starts, when it ends, and the level of focus it demands.

To join a lecture, Qassem needs to have a focus level at least as high as the lecture's requirement.
His goal is to attend as many lectures as possible with the least amount of coffee,
So he wants to keep his focus level just enough to meet the highest requirement among the lectures he attends.


Qassemn cannot attend overlapping lectures no two lectures he attends can overlap at any single point in time.
That is, if one lecture ends at time t, the next lecture must start strictly after t.
Your task is to help Qassem plan which lectures to attend to maximize the total number while minimiling his required focus level.

Input
The first line contains an integer T (1 < T < 100), the number of test cases.
The first line of each test case contains an integer N (1 < N < 105), representing the number of lectures.
The next N lines of each test case describe each lecture with three integers: S, E, C (1 < S < E < 101%), (1 < C < 1018),
representing start time, end time, and the focus level required.
It is guaranteed that the sum of N over all test cases doesn't exceed 10^5 Output
For each test case, output two integers:
the maximum number of lectures Qassem can attend and the minimum possible focus level required to attend them.
If there are multiple ways to attend the maximum number of lectures, choose the one that requires the least focus level

extra test case:

unsorted:
5
5 9 3
14 19 2
9 12 1
20 23 1
5 7 1
2 9 3

sorted by endtimes:
5
5 7 1
2 9 3
8 9 1
9 12 1
14 19 2
20 23 1


'''
# hardcoding test case for simplicity
all_inputs = '''2
5
1 3 2
5 8 3
7 12 2
15 18 4
3
1 3 2
2 4 3
3 5 2
'''
test_cases = int(all_inputs[0])

for test in range(test_cases):
    















'''
def filter_and_sort(test_case):
    all_lines = test_case.split("\n")
    new_list = [tuple(map(int,line.split(" "))) for line in all_lines]
    return sorted(new_list, key = lambda x: x[1])
    
    


all_lectures = filter_and_sort(test_case_extra)
all_combinations = {}
combinations_count = 1
for lec in all_lectures:
   
    if all_combinations == {}:
        all_combinations[combinations_count] = [lec]
        continue
    dict_index = 1
    while dict_index <= len(all_combinations.keys()):
        
        
        combination = all_combinations[dict_index]
                           
        print(combination, lec[0])
        if combination[-1][1] < lec[0]:
            combination.append(lec)
        else:
            combinations_count+=1
            all_combinations[combinations_count] = [lec]
            if combinations_count>100:
                break
        dict_index+=1
        
            

print(all_combinations)
    '''




    








