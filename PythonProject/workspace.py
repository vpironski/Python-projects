def count_divisible_numbers(a, b, d):
    # Count the numbers divisible by d in the interval [1, b]
    divisible_in_b = b // d

    # Count the numbers divisible by d in the interval [1, a-1]
    divisible_in_a_minus_one = (a - 1) // d

    # The count of numbers divisible by d in the interval [a, b]
    return divisible_in_b - divisible_in_a_minus_one

a = int(input("Enter the start of the interval (a): "))
b = int(input("Enter the end of the interval (b): "))
d = int(input("Enter the divisor (d): "))

if a > b:
    print("Invalid input: a should be less than or equal to b")
else:
    divisible_count = count_divisible_numbers(a, b, d)
    print(f"The number of integers divisible by {d} in the interval [{a}, {b}] is: {divisible_count}")
