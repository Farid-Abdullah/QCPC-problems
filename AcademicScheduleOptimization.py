


'''
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

def filter_and_sort(test_case):
    all_lines = test_case.split("\n")
    new_list = [tuple(map(int,line.split(" "))) for line in all_lines]
    return sorted(new_list, key = lambda x: x[1])
    
    
test_case2 = '''1 3 2
5 8 3
7 12 2
15 18 4'''
test_case_extra = '''5 7 1
2 9 3
8 9 1
9 12 1
14 19 2
20 23 1'''


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
    




    








