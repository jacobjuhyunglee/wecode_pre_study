#for in 반복문으로 역대 피파월드컵 출력
for i in range(1950, 2023, 4):
    print(i, 'FIFA World Cup')

#break 사용해서 월드컵의 꽃인 2002년 월드컵에 멈추게 작성
for i in range(1950, 2023, 4):
    print(i, 'FIFA World Cup')
    if i == 2002:
        break

#continue 이용해서 홀수년도 월드컵이 있는지 검사.
for i in range(1950, 2023, 4):
    if i % 2 == 0:
        continue
    print(i, 'FIFA World Cup')