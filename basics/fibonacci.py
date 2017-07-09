
# Run with python3
#Escribe la serie de Fibonacci hasta n

def fib(n):
    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

if __name__ == '__main__':
    fib(100)
