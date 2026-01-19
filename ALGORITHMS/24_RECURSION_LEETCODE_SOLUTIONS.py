# 231. Power of Two

def isPowerOfTwo(n):
    if n == 0:
        return False
    elif n == 1:
        return True 
    elif n % 2 == 0:
        return isPowerOfTwo(n // 2)
    else:
        return False 


# 326. Power of Three

def isPowerOfThree(n):
    if n == 0:
        return False
    elif n == 1:
        return True 
    elif n % 3 == 0:
        return isPowerOfThree(n // 3)
    else:
        return False 
    

result = isPowerOfThree(27)
print(result)


# 342. Power of Four 
def isPowerOfFour(self, n: int) -> bool:
    if n == 0:
        return False
    elif n == 1:
        return True 
    elif n % 4 == 0:
        return self.isPowerOfFour(n // 4)
    else:
        return False   