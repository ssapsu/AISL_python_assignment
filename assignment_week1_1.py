def printMenu():
    print('''---------------------------------------------------------------
“구구단을 외자, 구구단을 외자” 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료
---------------------------------------------------------------''')

while 1:
    printMenu()
    getNum=input("숫자를 입력하세요: ")
    if int(getNum) == 1:
        print()
        for odd in range(3,9+1,2):
            for num in range(1,9+1):
                print("{} * {} = {}".format(odd,num,odd*num))
            print()
    elif int(getNum) ==2:
        print()
        for even in range(2,8+1,2):
            for num in range(1,9+1):
                print("{} * {} = {}".format(even, num, even * num))
            print()
    elif int(getNum) ==3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")