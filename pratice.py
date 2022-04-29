import random
 
nums = [random.randrange(1, 1000, 1) for i in range(100)]

for num in nums:
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")  
    else:
        print(f"{num} is not prime")