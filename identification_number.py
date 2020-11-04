# 주민번호 지역 판별기

print('당신의 출생의 비밀을 알드립니다!')
name = input('당신의 이름을 입력해주세요: ')
identification_number = input(f'{name}님의 주민등록번호를 띄어쓰기 없이 입력해주세요: ')

birth_year = int(identification_number[0:2])
birth_month = int(identification_number[2:4])
birth_day = int(identification_number[4:6])

unique_location_number = int(identification_number[9:11])
application_order_number = int(identification_number[11:12])
fake_prevention_number = int(identification_number[12:len(identification_number)])

if identification_number[6] == '1' or identification_number[6] == '3':
	sex = '남자'
else:
	sex = '여자'

# 지역 코드
local_code = int(identification_number[7:9])

if 0 <= local_code <= 8:
	local = '서울특별시'
elif 9 <= local_code <= 12:
	local = '부산광역시'
elif 13 <= local_code <= 15:
	local = '인천광역시'
elif 16 <= local_code <= 25:
	local = '경기도'
elif 26 <= local_code <= 34:
	local = '강원도'
elif 35 <= local_code <= 39:
	local = '충청북도'
elif local_code == 40:
	local = '대전광역시'
elif 41 <= local_code <= 43 or 45 <= local_code <= 47:
	local = '충청남도'
elif local_code == 44 or local_code == 96:
	local = '세종특별자치'
elif 48 <= local_code <= 54:
	local = '전라북도'
elif 57 <= local_code <= 66:
	local = '전라남도'
elif local_code == 55 or local_code == 56:
	local = '광주광역시'
elif 67 <= local_code <= 70:
	local = '대구광역시'
elif 71 <= local_code <= 81:
	local = '경상북도'
elif 82 <= local_code <= 84 or 86 <= local_code <= 90:
	local = '경상남도'
elif local_code == 85:
	local = '울산광역시'
else:
	local = '제주특별자치도'

# 출력 - 1
print(f'생년월일: {birth_year}년 {birth_month}월 {birth_day}일')
print(f'성별: {sex}')
print(f'출생지역: {local}')

# 출력 - 2
secret = input("잠깐! 출생의 비밀을 정말 알고 싶으세요? '네', '아니오'로 대답해주세요! ")
if secret == '네':
	print(f'{name}님은 {birth_year}년 {birth_month}월 {birth_day}에 {sex}로 태어나셨습니다.')
	print(f'{name}님은 {local}에서 태어나셨으며 {unique_location_number}의 고유번호를 가진 읍, 면, 또는 동에서 \
{application_order_number}번째로 출생신고를 하셨고 {fake_prevention_number}라는 위조방지 특수번호를 가지고 계십니다')
else:
	print('당신에게 비밀이란 없군요!')
