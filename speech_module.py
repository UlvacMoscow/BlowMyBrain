FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


FIRST_TEN_DICT = { x + 1:FIRST_TEN[x] for x in range(0,len(FIRST_TEN))}
SECOND_TEN_DICT = { x+10:SECOND_TEN[x] for x in range(0,len(SECOND_TEN))}
OTHER_TENS_DICT = { ((x+2)*10):OTHER_TENS[x] for x in range(0,len(OTHER_TENS))}

def checkio(number):
    speech = ''
    hundred = number // 100
    if hundred > 0:
        speech +='{} {} '.format(FIRST_TEN_DICT[hundred], HUNDRED) 
        if number % 100 == 0:
            return print(speech.strip())
        else:
            number = number - hundred * 100
    if number in SECOND_TEN_DICT:
        speech += '{}'.format(SECOND_TEN_DICT[number])
        return print(speech.strip())
    tens = number // 10
    if tens > 1:
        tens = tens * 10
        speech += '{}'.format(OTHER_TENS_DICT[tens])
        if number % 10 == 0:
            return print(speech.strip())
        number -= tens
        speech += ' {}'.format(FIRST_TEN_DICT[number])
    else:
        speech += '{}'.format(FIRST_TEN_DICT[number])

    return print(speech.strip())


checkio(4)
checkio(14)
checkio(234)
checkio(12)
checkio(40)
checkio(432)
