# Recursion: Function that calls itself from within. Complex problem  can be solved iteratively (using for and while loops) or recursively 

#Iterative:
def walk(steps):
    for step in range(1, steps+1):
        print(f"You take step {step}")
        
# walk(3)

# Recursive
def walk_r (steps):
    if steps == 0: #base case
        return
    walk_r(steps-1)
    print(f"You take step {steps}")
    
# walk_r(3)

#factorial
#iterative 
def factorial(n):
    result = 1
    # while n>=1:
    #     result = result*n
    #     n=n-1
    # return result
    
    if n > 0:
        for y in range(1, n+1):
            result = result*y 
    return result
    
print(factorial(5))
        

#recursive
def factorial_r(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial_r(x-1)
    
print(factorial_r(3))