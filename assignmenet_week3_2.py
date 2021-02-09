limit = 100
people = [70, 80, 50]
count = 0

i=len(people)-1

#리스트 내림차순 정렬
people.sort(reverse=True)

#짝을 지을 수 있는 최대값 찾기
#maxWeight를 최소값(내림차순이므로 리스트의 마지막 항)으로 설정하고 리스트 전체를 돌려서 조건에 부합하는 maxWeight찾기
maxWeight = people[-1]
for element in range(len(people)):
    if people[element]+maxWeight <= limit and maxWeight < people[element]:
        maxWeight = people[element]

for element in range(len(people)):
    if element > i:                            #같은 요소에 접근하기 전까지 실행
        break
    if people[element] > maxWeight:             #내림차순이므로 maxWeight보다 큰 값은 짝을 지을 수 없기에 카운트에 +1을 하고
        count += 1          #완
    elif people[element]+people[i] <= limit:    #maxWeight보다 작으면서 짝을 지을 수 있는 리스트의 마지막 항을 짝을 지어줄 수 있다면 짝을 지어주고
        i -= 1
        count += 1
    else:                                       #짝을 지을 수 없는 element라면 짝을 짓지 않고 count+=1을 하고 넘어간다.
        count += 1

print(str(count))