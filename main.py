def get_own_divisors_sum(num):
    divisors = [1]
    for i in range(2, num):
        if (num % i)==0:
            divisors.append(i)
            i = i + 1
    return sum(divisors)

def get_perfect_numbers(max):
    perfect_numbers = []
    for a in range(0, (max+1)):
        divisors_sum = get_own_divisors_sum(a)
        if (divisors_sum == a):
            perfect_numbers.append(a)
    print(perfect_numbers)

get_perfect_numbers(int(input("Max number: ")))
