#hanoi tower program

movements=[]
def move(departure, arrival):
    movements.append([departure,arrival])

call_count=0
def hanoi_callcounter(callcounter):
    def wrapper(num, departure, temp, arrival):
        global call_count
        call_count+=1
        callcounter(num, departure, temp, arrival)
    return wrapper

@hanoi_callcounter
def hanoi(num, departure, temp, arrival):
    if num == 1:
        move(departure,arrival)
    else:
        hanoi(num-1,departure, arrival, temp)
        move(departure, arrival)
        hanoi(num-1,temp,departure,arrival)

num=int(input())
hanoi(num,'1','2','3')

print(str(call_count))
for element in movements:
    print("{} {}".format(element[0],element[1]))