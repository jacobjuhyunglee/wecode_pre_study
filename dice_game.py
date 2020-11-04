# random 모듈 사용해서 주사위 게임 만들기

import random

a = input('첫 번째 플레이어, 당신의 이름은? ')
b = input('두 번째 플레이어, 당신의 이름은? ')

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)

print(f'{a}의 주사위는 {dice_1}입니다')
print(f'{b}의 주사위는 {dice_2}입니다')

if dice_1 > dice_2:
    print(f'{a}가 {dice_1 - dice_2} 차이로 이겼습니다')
elif dice_2 > dice_1:
    print(f'{b}가 {dice_2 - dice_1} 차이로 이겼습니다')
else:
    print('비겼네요!')