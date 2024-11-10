def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
    return seq

def calculate():
        n = int(input("Enter a number to calculate the series: "))
        if n < 0:
            print("Please enter a valid number.")
            return
        
        print("Choose method:\n1. Iterative\n2. Recursive")
        choice = int(input("Enter 1 or 2: "))

        if choice == 1:
            result = fibonacci_iterative(n)
            print(f"Fibonacci series iterative: {result}")
        elif choice == 2:
            result = fibonacci_recursive(n)
            print(f"Fibonacci series recursive: {result}")
        else:
            print("Invalid choice")

calculate()

