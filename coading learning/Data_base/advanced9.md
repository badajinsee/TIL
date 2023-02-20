## Transactions

> 여러 쿼리문을 묶어서 하나의 작업처럼 처리하는 방법
> (다 성공하던지 다 실패하던지 해야하는 )

```SQL

START TRANSACTION;
state_ments;

...

[ROLLBACK | COMMIT];
```

- START TRANSACTION : 트랜잭션 구문의 시작을 알림

- COMMIT : 모든 작업이 정상적으로 완료되면 한꺼번에 DB 반영

- ROLLBACK : 부분적으로 작업이 실패하면 트랜잭션에서 진행한 모든 연산을 취소하고 트랜잭션 실행 전으로 되돌림

## Triggers

> 특정 이벤트에 대한 응답으로 자동으로 실행되는 것

```SQL
DELIMITER //
CREATE TRIGGER trigger_name
    {BEFORE|AFTER} {INSERT| UPDATE| DELETE}
    ON table_name FOR EACH ROW
BEGIN
    trigger_body;
END //
DELEMITER ;
```

- CREATE TRIGGER 키워드 다음에 생성하려는 트리거의 이름을 지정

- 각 레코드의 어느 시점에 트리거가 실행될지 지정 (삽입, 수정 삭제 전/후)

- ON 키워드 뒤에 트리거가 속한 테이블의 이름을 지정

- 트리거가 활성화 될 때 실행할 코드를 trigger_body에 지정

- BEGIN - END 구문 사이에 여러 sql 문 작성 되기 때문에
  하나의 트리거로 작동 될 수 있도록 사용

|        | OLD | NEW |
| ------ | --- | --- |
| INSERT | NO  | YES |
| UPDATE | YES | YES |
| DELETE | YES | NO  |

```SQL
SHOW TRIGGERS ;
-- 트리거 목록 확인

DROP TRIGGER trigger_name;
-- 트리거 삭제
```
