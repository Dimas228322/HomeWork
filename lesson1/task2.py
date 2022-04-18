# Техническое задание:
# Для всех нечетных чисел диапазона [1, 1000]
# вычислить их куб
# вычислить сумму цифр куба
# если сумма цифр куба делится нацело на 7, то добавить в накопительную сумму исходное число.
num = 0
summall = 0

while int(num := num+1) <= 1000:
    summa = 0
    if num % 2 == 0:
        nums = num-1
        kybnum = (nums**3)
        resultkyb = kybnum
        #print(nums)
        #print(kybnum)
        while kybnum != 0:
            p = kybnum % 10
            summa += p
            kybnum = kybnum // 10
            #print(summa)
        while summa % 7 == 0:
            summall += nums
            print (nums,'^3=',resultkyb,'[',summa,']','Накопительная сумма: ',summall)
            break
# Использовал подсказку из документов яндекс диска




    # while kybnum != 0:
    # p = kybnum % 10
    # summa += p
    # kybnum = kybnum // 10
    # summa = 0
    # print(summa)







