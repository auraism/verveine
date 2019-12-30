def mask_security_number(security_number):
    # 변경하려는 주민등록번호가 ''안에 들어가 있는 문자열입니다.
    # mask_security_number()함수 에서 들어간 문자열인 주민등록 번호를
    # 우선 리스트 형식으로 변경합니다
    # list형식으로 변경하면 ['8','8','8','8','8','8'...]이런식으로 변경됨
    # 변경된 리스트의 [-4]끝에서 4번째 숫자로부터 끝까지 문자열 '****'으로 변경
    # 그런데 여기까지는 list에요, 다시문자열로 변경하지않으면 ['8','8','8','8','..] 으로 출력
    # 그래서 result = '' 라는 비어있는 문자열을 하나 생성해준 뒤
    # for 문으로 list에 담겨있는 문자열인 주민등록번호와 뒷자리 4개가 *로 변경될 텍스트를
    # 순서대로 담아준다.
    # for문은 하나씩 불러와서 result 변수에 문자를 쌓아주는거죠. 문자와 문자가 계속 붙어져서 문자열이 됩니다.
    # ['8','8','8','8',' 형태가 '88888' 이런식으로
    # 그렇게 한바퀴 돌아서 다 옮겨지면 return 명령으로 변환된 문자열 주민등록 번호를 반환
    # 그걸 프린트해보면 뒷자리4개가 별로 변경된 결과물을 볼수 있다.
    list_number =list(security_number)
    list_number[-4:] = '****'
    result = ''

    for i in list_number:
        result = result + i
    return result

    # return (security_number[0:-4]) + '****'
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
