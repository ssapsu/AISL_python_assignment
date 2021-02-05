"""
구조체로 Stack 구현
FILO 이므로 pop함수에서는 첫번째로 리스트가 비었는지 예외처리를 해주고 비어있지 않다면 pop함수로 배열 마지막 부분을 지운다.
"""
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)     #list 끝에 원소 붙이는 방식
    def pop(self):
        if not self.items:
            print("-1")
        else:
            print(self.items[-1])
            self.items.pop()
    def size(self):
        print(len(self.items))
    def empty(self):
        if not self.items:
            print("1")
        else:
            print("0")
    def top(self):
        print(self.items[-1])

"""execute함수에서는 input으로 받아온 문자열을 split함수를 이용 리스트로 바꾼 후
요소의 1번째 원소를 이용해 목록에 있는 함수를 불러오고 push함수의 경우 2번째 원소까지 불러와 함수를 실행하게끔 도와준다.
"""
def execute(func):
    funcName=func.split()
    if funcName[0]== "push":
        element=funcName[1]
        stk.push(element)
    elif funcName[0]=="pop":
        stk.pop()
    elif funcName[0]=="size":
        stk.size()
    elif funcName[0]=="empty":
        stk.empty()
    else:
        stk.top()

stk=Stack()

num=int(input())
for count in range(num+1):
    func=input()
    execute(func)