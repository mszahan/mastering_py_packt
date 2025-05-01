primes = []
upto = 100

for num in range(2, upto +1):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    # if is_prime:
    #     primes.append(num)
    else:
        primes.append(num)

print(f"Prime numbers up to {upto}: {primes}")
