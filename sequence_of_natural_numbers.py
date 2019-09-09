 # 42 can be expressed as such a sum in four different ways:(a) 3+4+5+6+7+8+9, (b) 9+10+11+12, (c) 13+14+15 and (d) 42.

count = 0
new_list = []
gen_count = 0

def minion(num = 99):
    control = []
    rec = 0
    count = 0
    temp = 0
    for x in range(1, num + 1):
        for y in range(x, num + 1):
            temp += y
            control.append(y)
            # count = count + minion(x, many + 1)
            if temp == num:
                print('*********** BINGO summa = ', temp,' ***********')
                count += 1
                temp = 0
                print('control = ', control)
                control = []
                break
            if temp > num:
                temp = 0
                print('control = ', control)
                control = []
                break
    return count

gen_count = minion(99)
print(new_list, gen_count)
