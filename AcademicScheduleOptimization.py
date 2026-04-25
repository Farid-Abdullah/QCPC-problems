


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
    print(new_list)
    return sorted(new_list, key = lambda x: x[1])
    
    
test_case2 = '''1 3 2
5 8 3
7 12 2
15 18 4
14 20 1'''
test_case_extra = '''5 7 1
2 9 3
6 9 1
8 12 1
14 19 2
20 23 1'''
all_lectures = filter_and_sort(test_case_extra)
def getAllcomb_attempt1():
    '''Brute force to find all possible combinations, flawed attempt, couldn't find all combinations'''
    all_lectures = filter_and_sort(test_case2)
    all_combinations = {}
    combinations_count = 1
    for lec in all_lectures:
    
        if all_combinations == {}:
            all_combinations[combinations_count] = [lec]
            continue
        dict_index = 1
        while dict_index <= len(all_combinations.keys()):
            
            
            combination = all_combinations[dict_index]
                            
            #print(combination, lec[0])
            if combination[-1][1] < lec[0]:
                combination.append(lec)
            else:
                combinations_count+=1
                all_combinations[combinations_count] = [lec]
                if combinations_count>100:
                    break
            dict_index+=1
    return all_combinations



def hasConflict(comb):
    '''takes in lecture combination, checks for conflicts linearly,
      if conflict is found, returns index at the two conflicted lectures'''
    print("processing ", comb)
    for i in range(len(comb)-1):
        if(comb[i][1]>comb[i+1][0]):
            print("conflict found")
            return True, i
    return False,0


def attempt2(lecArray, solution=[0,0]):
    '''start with all lectures in  the array,
    use hasConflict to split the combination recursively on each conflic, 
    when no conflict update solution if better solution was found'''
    bool_index = hasConflict(lecArray)
    if(bool_index[0]):
        print("conflict at:", bool_index[1])
        lecArray1 = lecArray[:bool_index[1]+1]+lecArray[bool_index[1]+2:]
        lecArray2= lecArray[:bool_index[1]]+lecArray[bool_index[1]+1:]
        print("split to",lecArray1,"and", lecArray2)
        attempt2(lecArray1,solution)
        attempt2(lecArray2,solution)
    else:
        
        maxFocus = max(lecArray, key=lambda x:x[2])[2]
        totalLecs = len(lecArray)
        if totalLecs>solution[0]:
            
            solution[0] = totalLecs
            solution[1] = maxFocus
        elif totalLecs == solution[0]:
            solution[1] = min(solution[1],maxFocus)
       

    return solution



print("attempt2 solution:,",attempt2(all_lectures))

    




    








