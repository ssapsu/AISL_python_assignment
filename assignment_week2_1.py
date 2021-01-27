length,mul = map(int,input("길이와 배수를 입력하세요>").split())
img=[[int(x) for x in input().split()] for y in range(length)]
output=[[0]*length*mul for i in range(length*mul)]
for row in range(mul*length):
    for col in range(mul*length):
        div_row=row//mul
        div_col=col//mul
        output[col][row]=img[div_col][div_row]
for col in output:
    for row in col:
        print(row, end=' ')
    print()