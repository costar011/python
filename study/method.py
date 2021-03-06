# 040 strip 메소드
# 문자열의 좌우의 공백이 있을 때 이를 제거
# data = "   삼성전자    "
# 문자열에서 strip( ) 메소드를 사용하면 좌우의 공백을 제거할 수 있다 이때 문자열은 그대로 유지되고 공백이 제거된 새로운 문자열이 반환
data = "   삼성전자    "
data1 = data.strip()
print(data1)

# 041 upper 메소드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경
# ticker = "btc_krw"
# upper 메소드를 호출하면 문자열을 대문자로 만들 수 있다. 다만 이 경우에도 원본 문자열은 유지되고 대문자로 변경된 새로운 문자열 객체가 반환
# 반환된 새로운 객체를 새로운 변수로 바인딩한 후 이를 print 함수로 출력
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

# 042 lower 메소드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경
# ticker = "BTC_KRW"
# lower 메서드
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 043 capitalize 메소드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경
a = "hello"
a = a.capitalize()

# 044 endswith 메소드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메소드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인
# file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
file_name.endswith("xlsx")


# 045 startswith 메소드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인
# file_name = "2020_보고서.xlsx"
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

# 046 split 메소드
# 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠라
# a = "hello world"
# 문자열의 split() 메서드를 사용하면 문자열에서 공백을 기준으로 분리
a = "hello world"
a.split()

# 047 split 메소드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠라
# ticker = "btc_krw"
# 문자열에서 split() 메서드는 문자열을 분리할 때 사용 이때 어떤 값을 넘겨주면 그 값을 기준으로 문자열을 분리
ticker = "btc_krw"
ticker.split("_")

# 048 split 메소드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠라
# date = "2020-05-01"
date = "2020-05-01"
date.split("-")

# 049 rstrip 메소드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거
# data = "039490     "
# rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환 그 값을 data라는 변수가 새로 바인딩
# 기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제
data = "039490     "
data = data.rstrip()
