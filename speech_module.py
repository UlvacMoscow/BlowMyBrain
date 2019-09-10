FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number > 100:
        print(number // 100,'hundred')
        tens = number % 100
        print(tens , 'tens')
  number = str(number)
  speech = ''
    number = str(number)
    speech = ''
    if len(number) == 3:
        print(number,'hundred')
    if len(number) == 2:
        print(number,'OTHER_TENS')
    if len(number) == 1:
        print(number)

    #replace this for solution
    return 'string representation of n'


checkio(4)
checkio(14)
checkio(234)
checkio(12)
checkio(40)
checkio(432)
