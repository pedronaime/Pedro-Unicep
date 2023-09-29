import math


def is_a_perfect_square(number):
    root = math.sqrt(number)
    integer_part = int(root)
    return root % integer_part == 0


def sum_of_elements():
    my_sum = 0
    for element in range(1, 20):
        if element % 2 == 0:
            print(-element / (math.factorial(element + 1)))
            my_sum += -element / (math.factorial(element + 1))
        else:
            print(element / (math.factorial(element + 1)))
            my_sum += element / (math.factorial(element + 1))
    return my_sum


print(f"The sum of the elements is {sum_of_elements()}")


def prime_numbers_in_range(starting_number, ending_number):
    prime_numbers = []
    for i in range(starting_number, ending_number):
        times_divided = 0
        for j in range(1, i):
            if i % j == 0:
                times_divided += 1
        if times_divided == 1:
            prime_numbers.append(i)
    return prime_numbers

# for prime in prime_numbers_in_range(1, 100):
#    print(f"{prime} is a prime number")

# typedNumber = 0

# while typedNumber != -1:
#    typedNumber = int(input("Type a number to verify if its square root is an integer "))
#    if is_a_perfect_square(typedNumber):
#        print(f"{typedNumber} is a perfect square")
#    else:
#        print(f"{typedNumber} is not a perfect square")
