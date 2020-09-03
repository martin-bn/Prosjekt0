

def factorial(number):
    if number < 0:
        raise ValueError("Only positive numbers, please")
    elif number == 0:
        raise ValueError("Factorial of zero is 1")
    else:
        fac = 1
        for i in range(1, number + 1):
            fac = fac * i
        return fac

def sin(x, N):
    value = int(0)
    for n in range(0, N+1):
        value += ( (-1)**n * x **(2*n + 1)) / (factorial(2*n + 1))
    return value

def divide(x,y):
    return x / y

def exponent(x,y):
    return x ** y

def transpose(matrix):
    return [[row[i]for row in matrix] for i in range(len(matrix[0]))]
