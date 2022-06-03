def fizzbuzz(n):
    if n % 3 == 0 and n % 5 != 0:
        # global fizz
        # fizz = "Fizz"
        return "Fizz"
    elif n % 3 != 0 and n % 5 == 0:
        # global fizz
        # buzz = "Fizz"
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        # global fizzBuzz
        # fizzBuzz = "fizzBuzz"
        return "fizzbuzz"
    else:
        return n

# print(fizzbuzz(134))
