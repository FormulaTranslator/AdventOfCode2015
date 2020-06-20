# this code actually finds the answer to the advent problem. However, it takes a good bit of time to complete
min_presents = 33100000  # 6400/10
house_presents = 0
house = int(min_presents/10/10)


def get_factors(number):  # Part 1 function
    """returns all factors of a given number"""
    start_value = int(number/2)
    divisors_set = set()
    for i in range(2, start_value+1):
        if number % i == 0:
            divisors_set.add(i)
            divisors_set.add(int(number/i))
    return divisors_set


def get_factors_50(number):  # Part 2 function
    """returns all factors of a given number
    that go into the number less than 50 times"""
    start_value = int(number/2)
    divisors_set = set()
    for i in range(2, start_value+1):
        if number % i == 0:
            if int(number/i) <= 50:
                divisors_set.add(i)
    return divisors_set


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
    # house_presents = (sum(factors) + 1 + house) * 10
    # Part 2
    factors = get_factors_50(house)
    house_presents = (sum(factors) + house) * 11

print("House number {} got {} presents".format(house, house_presents))
