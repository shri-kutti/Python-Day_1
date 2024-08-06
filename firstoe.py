
#prime number in a range
def prime(n):
    if n == 1:
            print("nil")
            return
    cnt = 0
    for x in range(2,n): 
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0:
            print(x)
        cnt = 0

n = 100
prime(int(n))

print('going through the list : ')
for i in [2,23,8,12,44,9,0,3]:
     print(f"This is the {n} th element : {i}")
     n+=1

# for i in range(2,x):
        #     if x % i == 0:3
        #         cnt += 1

#fibonacci series
print("To print Fibonacci Like:-")

print("0 1 2 3 5 8 ...")

n= int(input("Enter the number(limit): "))

num = 0
prev = 1
added = 0
for i in range(0,n):
    print(added)
    added = num + prev
    num = prev
    prev = added

# #using list
# my_frnds = ["Shri","venkat","vicky"]
# jai_frnds = ["Tilak","sushi","vinayak",'vicky']

# common = []
# for i in my_frnds:
#     if i in jai_frnds:
#         common.append(i)
        
# combined = list(set(my_frnds + jai_frnds))
# print(" Combined ->",combined)

# print(common)

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# set1 = set(list1)
# set2 = set(list2)

# difference = set1 ^ set2 #this is used for removing common `-` is used for removing common and returning first
# print(difference) 

#list,set,dictionary comprenhension
# squares = [x**2 for x in range(10)]
# print(squares)

# even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares)

# squared_dict = {x: x**2 for x in range(5)}

# squared_set = {x**2 for x in range(5)}

#using dictionary
poll = ["red", "J", "blue", "red", "blue", "red", "C", "red", "red", "C", "blue"]
 
vote = {}
for language in poll:
    if language in vote:
        vote[language] += 1
    else:
        vote[language] = 1
 
print("Vote Tally:", vote)
