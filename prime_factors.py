def prime_factors(num):
    lst = []

    for i in range(2, num + 1):
        while num % i == 0:
            lst.append(i)
            num /= i

    return lst

#print(prime_factors(630))
#print(prime_factors(13))
