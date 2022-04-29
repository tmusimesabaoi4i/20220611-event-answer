for num in range(1, 101):
    string = ''

    # ここから記述
    remainder3 = num % 3 # remainder divided by 3
    remainder5 = num % 5 # remainder divided by 5
    remainder15 = num % 15 # remainder divided by 15

    if remainder15 == 0:
        string="FizzBuzz"
    elif remainder5 == 0:
        string="Buzz"
    elif remainder3 == 0:
        string="Fizz"
    else:
        string=str(num)
    # ここまで記述

    print(string)
