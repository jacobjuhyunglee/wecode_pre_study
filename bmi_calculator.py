# BMI 수치 계산기
print('당신의 BMI 수치를 측정해드립니다!')

name = input('이름을 입력해 주세요: ')
sex = input('성별을 입력해 주세요: ')
age = input('나이를 입력해 주세요: ')
height = int(input('신장을 입력해 주세요: ')) * 0.01
weight = int(input('몸무게를 입력해 주세요: '))

print('<검사 결과 입니다>')
bmi = weight / (height * height)
print(f'{name}님의 BMI 수치는 {bmi:.1f} 입니다.')

if bmi < 18.5:
    print('저체중이시네요? 수치가 너무 낮아요!')
elif 18.5 <= bmi <= 22.9:
    print('정상이시네요? 수치가 보통이에요!')
elif 23 <= bmi <= 24.9:
    print('비만 전 단계시네요? 수치가 약간 높아요!')
elif 25 <= bmi <= 29.9:
    print('1단계 비만이시네요? 수치가 높아요!')
elif 30 <= bmi <= 34.9:
    print('2단계 비만이시네요? 수치가 매우 높아요!')
else:
    print('3단계 비만이시네요? 수치가 울트라 높아요!')

print('괜찮아요.... 맛있으면 0 칼로리잖아요....')

