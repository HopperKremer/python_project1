print("please work")
# check 1 2 3 4

# test


def some_fn():
    favColor = input("what's your fav color?")

    print("Are you sure you like " + favColor + " best?")
    age = input("How old are you?")
    print("Huh, I rememember when I was " + age + " years old.")
    # Let's figure out how to get current year with python
    print("you were born around the year " +
          str(2020-int(age)) + " weren't you?")
    if int(age) > 70:
        print("You are too old to drink")
    elif int(age) > 21:
        print("You can drink")
    elif int(age) > 16:
        print("You are too young")
    else:
        print("You are not a valid age")


some_fn()
# test
# test 2
# test 3
