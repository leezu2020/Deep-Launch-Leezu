# 13장 모델 성능 검증하기

## 성능 검증
    은닉층(hidden layer)이나 학습 반복 수(epochs)가 많아진다고 완벽한 예측 모델이 만들어지는 것은 아니기 때문에 모델의 성능을 검증하는 과정이 필요

* 과적합
    - 주어진 샘플에는 적합한 예측 정확도를 보이나, 새로운 데이터에 대해서는 그렇지 않은 것을 의미
    - 이유
        - layer가 너무 많음
        - 변수가 복잡
        - 테스트셋과 학습셋이 중복
    - 해결 방법
        - 샘플 데이터를 학습용과 테스트용으로 완벽히 분리

* 모델 성능 향상 방법
    - 데이터 보강
    <br>ex) 사진의 경우 사진 크기를 확대/축소한 것을 추가
    <br>k겹 교차 검증: 가지고 있는 데이터를 반복적으로 학습셋, 데이터셋으로 나누어 학습
    - 알고리즘 최적화
    <br>ex) 다른 구조로 모델을 바꿈


* 파이썬 코드 관련
    - 참고 함수

    | 라이브러리 | 함수명    | 예시 | 사용 목적 | 비고 |
    |-----------|:-----------:|:---------------:|:------------------|:-------------|
    | sklearn.model_selection   | train_test_split | `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True);` | 정해진 비율(test_size)만큼 테스트셋을 설정, 나머지는 학습셋  |
    | tensorflow.keras.models | model | `model.evaluate(X_test, y_test)` | 학습된 모델에 테스트셋을 적용하여 결과 출력 | loss와 accuracy 반환 |
    | sklearn.model_selection | KFold | `kfold = KFold(n_splits=5, shuffle=True)` | 데이터를 원하는 수만큼 나누어 각각 학습셋과 테스트셋으로 사용 | n_splits: 몇 개의 파일로 나눌지, shuffle=True: 샘플이 한쪽으로 치우쳐지지 않게 함 |


