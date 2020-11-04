# 스트링, 리스트, 딕셔너리를 반복문으로 돌면서 인자를 출력하는 함수를 작성해보세요.

# 스트링 반복문
for letter in 'Wecode':
    print(letter)
    print(letter, end=' ')

# 리스트 반복문으로 한 줄씩 출력
netflix_favourites = ['킹덤', '비밀의숲', '사생활', '스타트업']
for favourite in netflix_favourites:
    print(favourite)

# 딕셔너리 반복문으로 dream_team의 이름, 내 마음 속 순위 출력하기
dream_team = {'박보영': '1순위', '태연': '2순위', '수지': '3순위', '강한나': '4순위'}

for key, value in dream_team.items():
    print(key, value)
