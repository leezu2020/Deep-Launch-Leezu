import random

print('1부터 20까지의 숫자를 맞추는 프로그램')

secretNumber = random.randint(1, 20)

# 숫자 입력받기


def validate_input(prompt):
    while True:
        value = input(prompt)
        if value.isnumeric():
            value = int(value)
            break
        else:
            print("숫자를 입력해주세요.")
    return value

# 유효성 범위 내에서 입력 받기


def guess_input(chance, valid_range_from, valid_range_to):
    count = 0
    now_from = valid_range_from
    now_to = valid_range_to
    while count < chance:
        guess = validate_input("예상하는 숫자를 입력하세요.")
        if now_from < guess < now_to:
            count += 1
            if guess < secretNumber:
                now_from = guess
                print("예상한 숫자보다 큽니다. 남은 기회: ", chance - count)
            elif guess > secretNumber:
                now_to = guess
                print("예상한 숫자보다 작습니다. 남은 기회: ", chance - count)
            else:
                print(str(count) + "번만에 정답" + str(secretNumber) + "을 맞췄습니다.")
                break
        else:
            print("이미 제외된 범위의 숫자입니다. 재입력해주세요.")
    if guess != secretNumber:
        print("6번의 기회를 모두 사용했습니다.")


guess_input(6, 1, 20)
