# 15장 실제 데이터로 만들어 보는 모델

    실제 데이터에서는 비어있는 값이나, 범위에서 너무 벗어난 값이 들어가 있는 경우가 있고, 혹은 클래스와 관련 없는 정보가 포함되어 있기도 함
* 결측치
    - 측정값이 없는 부분(=누락된 부분)
    - 종류
        - MCAR(Missing Completely At Random): 결측값의 발생이 다른 변수들과 상관 없는 경우<br>
        ex) 데이터 입력 간 누락이나 오류, 전산상의 오류 등<br>
        \> 주로 데이터 삭제로 해결
        - MAR(Missing At Random): 결측치가 결측된 변수와는 무관하지만, 다른 변수와 관련 있는 경우<br>
        ex) '여성이 남성보다 체중을 기입하지 않는다'라고 하면 체중에 결측치가 생기지만 이는 체중 변수가 아닌 성별 변수와 관련
        - MNAR(Missing At Not Random): 결측치가 결측된 변수와 관련 있는 경우<br>
        ex) 서비스에 불만족한 고객들은 만족도 설문에 응답하지 않음

* 결측치 처리 이유
    - 결측 원인에 따른 데이터의 편향
    - 결측치 제거 시, 데이터 축소로 인한 원데이터 훼손 및 검정력 감소
    - 분석 결과의 왜곡 등
    > 출처: https://velog.io/@pong_jin/missing-value-imputation

* 파이썬 코드 관련
    - 참고 함수

        - 판다스의 `fillna` 함수<br>
        \>> 결측치를 채워 주는 함수

