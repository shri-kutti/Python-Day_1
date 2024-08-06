

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