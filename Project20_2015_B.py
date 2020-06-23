# this code actually finds the answer to the advent problem.
min_presents = 33100000  # 6400/10
house_presents = 0
house = int(min_presents/10/10)


def get_factors(number, limit=0):  # Part 2 function
    """returns all factors of a given number
    that go into the number less than 50 times"""
    divisors_set = set()
    if limit == 0:
        limit = number
    i = 1
    while True:
        if number / i < i:
            return divisors_set
        if number % i == 0:
            divisor2 = number // i
            if divisor2 < limit:
                divisors_set.add(i)
            if i < limit:
                divisors_set.add(int(number / i))
        i += 1


step = 10000
while house_presents < min_presents:
    if house_presents < min_presents/3 and step > 1000:
        step = 10000
    elif house_presents < min_presents / 2 and step > 1:
        step = 1000
    else:
        step = 1
    house += step
    # Part 1
    # factors = get_factors(house)
    # house_presents = sum(factors) * 10
    # Part 2
    factors = get_factors(house, 50)
    house_presents = sum(factors) * 11

print("House number {} got {} presents".format(house, house_presents))
