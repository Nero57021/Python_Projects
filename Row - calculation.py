try:
    number = int(input("Some number:"))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
