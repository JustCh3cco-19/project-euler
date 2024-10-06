def problem3(n):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            n -= 1
        else:
            n += 1
    return n

n = 600851475143
print(problem3(n))