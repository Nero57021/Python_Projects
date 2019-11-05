def coin_change(cents):
    c = cents
    print(c//25, "quarters")
    c = c % 25
    print(c//10, "dimes")
    c = c % 10
    print(c//5, "nickles")
    c = c % 5
    print(c//1, "pennies")

coin_change(43)