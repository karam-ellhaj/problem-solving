def myPow( x: float, n: int) -> float:
        j = 1
        if n < 0:
            j = 1/x
        for i in range(abs(n)):
            j*=x
        return j

print(myPow(2,2))