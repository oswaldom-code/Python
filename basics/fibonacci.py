
    def fib(n):
        """Escribe la serie de Fibonacci hasta n."""
        a, b = 0, 1
        while a < n:
            print(a, " ")
            a, b = b, a+b
            print()

if __name__ == '__main__':
    fib(100)
