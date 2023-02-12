
print('두 수를 입력받아 계산하는 프로그램입니다.')

# 숫자 입력받기


def validate_input(prompt, valid_list):
    while True:
        value = input(prompt)
        if len(valid_list) > 0 and value in valid_list:
            value = int(value)
            break
        elif len(valid_list) == 0 and value.isnumeric():
            value = int(value)
            break
        else:
            print("잘못된 입력입니다. 재입력해주세요.")
    return value


def select_calc(num1, num2):
    print("원하는 연산을 선택하세요.\n1. 더하기\n2. 빼기\n3. 곱하기\n4. 정수나누기\n5. 실수나누기\n6. 나머지 구하기\n7. 계산기 종료")
    calc = validate_input("", ['1', '2', '3', '4', '5', '6', '7'])
    if (calc == 7):
        print("두 개의 값 : ", num1, "와", num2)
    else:
        result = {1: num1 + num2, 2: num1 - num2, 3: num1 * num2, 4: num1 //
                  num2, 5: num1 / num2, 6: num1 % num2}.get(calc, "잘못된 값")
        print("계산 결과:", result, "\n프로그램을 종료합니다.")


num1 = validate_input("계산할 첫번째 값을 입력해주세요 :", [])
num2 = validate_input("계산할 두번째 값을 입력해주세요 :", [])

select_calc(num1, num2)
