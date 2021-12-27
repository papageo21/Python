number = 56
cnt = 0
max_try = 10

player = int(input("Dwse enan arithmo: "))

while player != number:
    cnt += 1
    if cnt == max_try:
        print("Exases..")
        exit()

    if player > number:
        print("o arithmos pou edwses einai megaliteros! ")
    else:
        print("o arithmos pou edwses einai mikroteros! ")

    player = int(input("Dwse enan arithmo: "))


print("Bravo!!")





