# p1
def SUM ():
    N = int(input ("Enter number : ")) 
    sum = 0
    if N > 0 :
        sum = N*(N+1)/2
    else :
        N = int(input ("Enter positive number: "))
        sum = N*(N+1)/2    
    print(sum)
SUM()

# p2
def sort ():
    lst = input("Enter three numbers A ,B , C separated by space : ").split(" ")
    lst = list(map(int,lst))
    lst2 = sorted(lst)
    print(lst2)
sort()

# p3
def factorial():
    N = int(input ("Enter number : "))
    fact =1
    for i in range(N):
        i +=1
        fact *= i 
    print(fact)
factorial()

# p4
def rm2 ():
    lst = input('Enter elements of a list separated by space ').split(" ")
    lst = list(map(str,lst))
    lst2 = set(lst)
    print(lst2)
rm2()

# # p5
# # print(round(6.5) - round(3.5) == 3) 
# # the output = false
# # round(6.5) - round(3.5) == 2
# # round function will return the nearest even integer

    
    