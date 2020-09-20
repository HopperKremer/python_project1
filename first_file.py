import datetime
print("please work")
now = datetime.datetime.now()
# check 1 2 3 4


# test


def some_fn():
    #favColor = input("what's your fav color?")

    #print("Are you sure you like " + favColor + " best?")
    #age = input("How old are you?")
    #print("Huh, I rememember when I was " + age + " years old.")

    # Let's get current year
    # how to accept input for month as a str too

    # birth_month = int(input("what month were you born? Enter as a number 1-12"))
    # birth_day = int(input("What day were you born?"))
    # birth_year = int(input("What year were you born?"))

    # age = 0

    def suffixFinder(num):
        remainder = num % 10

        if num >= 4 and num <= 20:
            return "th"
        elif remainder == 0:
            return "th"
        elif remainder == 1:
            return "st"
        elif remainder == 2:
            return "nd"
        elif remainder == 3:
            return "rd"
        else:
            return "th"

    for i in range(1, 30):
        print (str(i) + suffixFinder(i))


    # if birth_month <= now.month and birth_day < now.day:
    #     print("It's not your birthday yet")
    #     age = now.year - (birth_year + 1)
    # elif birth_month == now.month and birth_day == now.day:
    #     age = now.year - birth_year
    #     # get it to print proper number suffix: 21st 25th birthday
    #     print("Happy " + str(age) + " birthday!")

    # print("you were born around the year " +
    #       str(now.year-int(age)) + " weren't you?")
    # if int(age) > 70:
    #     print("You are too old to drink")
    # elif int(age) > 21:
    #     print("You can drink")
    # elif int(age) > 16:
    #     print("You are too young")
    # else:
    #     print("You are not a valid age")


some_fn()
