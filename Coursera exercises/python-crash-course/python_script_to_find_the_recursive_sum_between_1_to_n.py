def sum_of_positive_numbers(n):
    if n < 1:
        return 0
    
    return n + sum_of_positive_numbers(n-1)

print(sum_of_positive_numbers(3))
print(sum_of_positive_numbers(5))
print(sum_of_positive_numbers(-1))
print(sum_of_positive_numbers(0))