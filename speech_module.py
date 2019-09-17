FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    test = { x + 1:FIRST_TEN[x] for x in range(0,len(FIRST_TEN))}
    hundred = number // 100
    if hundred > 0:
        if number % 100 == 0:
            return print()
        number = number - hundred * 100


    tens = number // 10
    if tens > 0:
        num = number - tens * 10
    else:
        num = number

  print(test)

    #replace this for solution
    return 'string representation of n'


checkio(4)
checkio(14)
checkio(234)
checkio(12)
checkio(40)
checkio(432)
