# 03score.py 
student = [['박이썬', 30,90,85,70], ['이합격', 100,75,85,30]]
for my in student:
    name = my[0]
    total = sum(my[1:])
    print(f'{name} 총점 {total}점')


# 해결] 박이썬 총점 , 이합격 총점 
# for반복문 한번에 해결가능 
# print('길이 =', len(student))  student.len()틀림
# 11시 10분 정리 실습  
# 01milk.py문서 중첩for반복 이해
# 04star.py문서 중첩for반복 이해