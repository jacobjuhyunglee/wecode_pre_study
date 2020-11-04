# if와 else를 이용해 조건문을 작성해보세요.
# if, elif, else를 이용한 간단한 점수 계산기

# A = 90점 이상
# B = 80점 이상
# C = 70점 이상
# D = 60점 이상
# F = 60점 미만

score = int(input('당신의 점수는? ')) #점수 입력

if score >= 90:
    print("You've got A")
elif score >= 80:
    print("You've got B")
elif score >= 70:
    print("You've got C")
elif score >= 60:
    print("You've got D")
else:
    print("Do better next time")