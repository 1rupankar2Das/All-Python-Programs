#WAP to display the terms of a Fibonacci series.
def fibonacci_series(num_terms):
    fib_series = [0, 1]
for i in range(2, num_terms):
    next_term = fib_series[i - 1] + fib_series[i - 2]
    fib_series.append(next_term)
    return fib_series
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
if num_terms <= 0:
    print("Number of terms should be a positive integer.")
fib_series = fibonacci_series(num_terms)
print("Fibonacci series:")
for term in fib_series:
    print(term, end=" ")
