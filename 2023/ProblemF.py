


def RMQ(n,n_array,q):
    output = ""
    temp_array = []
    q_array = []
    for i in range(q):
        query = input("Enter the space separated query:")
        query = query.split(" ")
        query = [int(query[0]), int(query[1])]
        q_array.append(query)
        
        temp_array = n_array[query[0]:query[1]+1]

        temp_message = ''
        pre_length = 0
        required_length = len(temp_array)/2
        
        for j in temp_array:
                j_count = temp_array.count(j)
                
                if j_count >= required_length and j_count>pre_length:
                    temp_message = f'Yes\n{str(j)}'
                    pre_length = j_count
                    break
                else:
                    temp_message = 'No'
        print(temp_message)


n = int(input("Enter the n (length of the array): "))

array_string = input("enter the space separated numbers: ")

q = int(input("Enter the number of queries: "))

array = []

for i in array_string:
    if i.isdigit():
        array.append(int(i))



RMQ(n,array,q)


