def flatten(data):
    output=[]
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output.append(item)
    return output

book_info={
    "HarryPotter1":[[1997],[6],[26]],
    "TheLordOfTheRings":[[1954],[7],[29]],
    "engineering_mathematics1":[[2018],[2],[28]]
}

while True:
    get_book_name=input("원하시는 책을 입력하세요: \n>")
    if not (get_book_name in book_info):
        print("제목을 다시 입력해주세요.")
        continue
    else:
        get_num=input("""\
------------------------
원하시는 정보를 선택해주세요.
1. 년
2. 월
3. 일
4. 종료
------------------------
""")
    if get_num=='1':
        print(flatten(book_info[get_book_name])[0],"년 입니다.")
    elif get_num=='2':
        print(flatten(book_info[get_book_name])[1],"월 입니다.")
    elif get_num=='3':
        print(flatten(book_info[get_book_name])[2],"일 입니다.")
    elif get_num=='4':
        print("프로그램이 종료되었습니다.")
        break
    else:
        print("다시 입력해주세요")