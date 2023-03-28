"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""

Todo.objects.create(content='실습제출',priority='5',completed='False',deadline='2023-03-28')

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
Todo.objects.create(content='데일리 설문(오후) 제출', deadline='2023-03-28')

"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content='밥먹기', priority='1', deadline='2023-03-28')
Todo.objects.create(content='쳥소하기',completed='True', deadline='2023-03-28')
Todo.objects.create(content='복습하기',deadline='2023-03-28')
Todo.objects.create(content='코딩리뷰하기',deadline='2023-03-28')
Todo.objects.create(content='잠자기',completed='False', deadline='2023-03-28')

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.all().order_by('pk') 

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.all().order_by('-priority')

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""

todo = Todo.objects.get(pk=1) 

print(todo.pk, todo.content, todo.priority, todo.deadline, todo.created_at)
1 실습제출 5 2023-03-28 2023-03-28