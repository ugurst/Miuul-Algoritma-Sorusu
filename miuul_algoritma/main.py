# 1'den 100'e kadar her sayıyı yeni bir satıra yazdırın.
# 3'ün her katı için sayı yerine "fizz" yazdırın.
# 5'in her katı için sayı yerine "buzz" yazdırın.
# Hem 3'ün hem 5'in katı olan sayılar için sayı yerine "fizzbuzz" yazdırın.



l = list(range(1, 101))




for i in l:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)




