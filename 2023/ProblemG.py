
'''
first_line = input("first line: ")
second_line = input("second line: ")
n,m = first_line.split(" ")

array = second_line.split(" ")
dict_gcd = {}

'''
def gcd(num1, num2):
    h = 0
    if num1>num2:
        num = num1
    else:
        num = num2
    for i in range(1,num+1):
        if num1%i == 0 and num2%i == 0 :
            h=i
    return h
x = int(input("Enter a number: "))

y = int(input("Enter a number: "))

print(gcd(x,y))


'''
for i in array:
    dict_gcd[i] = 
   ''' 
