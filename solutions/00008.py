#!/usr/bin/python

numbers = [
 "73167176531330624919225119674426574742355349194934",
 "96983520312774506326239578318016984801869478851843",
 "85861560789112949495459501737958331952853208805511",
 "12540698747158523863050715693290963295227443043557",
 "66896648950445244523161731856403098711121722383113",
 "62229893423380308135336276614282806444486645238749",
 "30358907296290491560440772390713810515859307960866",
 "70172427121883998797908792274921901699720888093776",
 "65727333001053367881220235421809751254540594752243",
 "52584907711670556013604839586446706324415722155397",
 "53697817977846174064955149290862569321978468622482",
 "83972241375657056057490261407972968652414535100474",
 "82166370484403199890008895243450658541227588666881",
 "16427171479924442928230863465674813919123162824586",
 "17866458359124566529476545682848912883142607690042",
 "24219022671055626321111109370544217506941658960408",
 "07198403850962455444362981230987879927244284909188",
 "84580156166097919133875499200524063689912560717606",
 "05886116467109405077541002256983155200055935729725",
 "71636269561882670428252483600823257530420752963450",
]

def main():
    number = ''.join(numbers)
    total = len(number)
    count = 13
    index = 1
    max_val = 0
    val = 1
    substring = number[:count]
    for i in substring:
        val *= int(i)
    max_val = val
    max_index = 0
    while index < total - count:
        if int(number[index-1]) == 0:
            # For debugging division by zero
            print 'zeroo00 ', index, number[index-1]
        val /= int(number[index-1])
        if int(number[index + count - 1]) != 0:
            val *= int(number[index + count - 1])
        else:
            # Found a zero; find next substring without zeros
            val = 1
            index = index + count
            while index < total - count:
                substring = number[index:index+count]
                zero_index = substring.find('0')
                if zero_index != -1:
                    index = index + zero_index + 1
                    continue
                else:
                    break
            if len(substring) != count:
                # reached end of string
                break
            for i in substring:
                val *= int(i)
        if val > max_val:
            max_val = val
            max_index = index
            # print max_val, max_index, number[max_index:max_index+count]
        index += 1
    s = 1
    ss = ''
    for i in range(max_index, max_index + count):
        s *= int(number[i])
        ss += number[i]
    print s, ss

if __name__ == '__main__':
    main()

