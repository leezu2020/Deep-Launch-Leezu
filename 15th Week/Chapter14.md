# 14장 모델 성능 향상시키기

## 성능 검증
    은닉층(hidden layer)이나 학습 반복 수(epochs)가 많아진다고 완벽한 예측 모델이 만들어지는 것은 아니기 때문에 모델의 성능을 검증하는 과정이 필요

* 검증셋 vs 테스트셋
    - 검증셋(validation set)은 학습이 완료된 모델을 검증하기 위한 set(중간 점검)<br>
    학습에 일정 부분 관여
    - 테스트셋(test set)은 학습과 검증이 끝난 모델의 최종 성능 평가용

* 과적합을 현상을 피하기 위해 epochs를 조절<br>
\>> 검증셋의 오차가 커지기 직전까지 학습한 모델 = 최적의 횟수로 학습한 모델


* 파이썬 코드 관련
    - 참고 함수

        - model.fit() 함수 내의 `validation_split` 옵션<br>
        \>> 학습셋 내의 검증셋 설정 비율
        - ModelCheckpoint()의 `save_best_only` 옵션<br>
        \>> 최고의 모델 하나만 저장

    | 라이브러리 | 함수명    | 예시 | 사용 목적 | 비고 |
    |-----------|:-----------:|:---------------:|:------------------|:-------------|
    | tensorflow.keras.callbacks   | ModelCheckpoint | `checkpointer = ModelCheckpoint(filepath=modelpath, verbose=1)` | 학습 중인 모델을 저장하는 함수  | verbose: 모델이 저장될 곳을 정하고 진행되는 현황을 모니터
    | tensorflow.keras.callbacks   | EarlyStopping | `early_stopping_callback = EarlyStopping(monitor='val_loss', patience=20)` | 테스트셋 오차가 줄어들지 않으면 학습을 자동으로 멈추게 하는 함수  | monitor: model.fit()의 실행 결과 중 이용할 값, patience: 몇번까지 향상되지 않으면 종료시킬지


