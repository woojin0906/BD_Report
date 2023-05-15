# 1. 정규표현식(Regular Expression)이란?
#   - 정규 표현식이란 문자열을 처리하는 방법 중의 하나로 특정한 조건의 문자를 ‘검색’하거나 ‘치환’하는 과정을 매우 간편하게 처리할 수 있도록 하는 수단이다.
#   - Python 뿐만 아니라 문자열을 처리하는 모든 곳에 사용된다.

# 정규 표현식의 특징
#  - 대소문자 구분
#  - 띄어쓰기 수 구분

# 정규표현식의 필요성
# 정규 표현식을 이용하면 직관적이고 간편한 코드를 짤 수 있고 복잡한 문자열의 규칙 등을 쉽게 치환할 수 있다.

# 정규표현식 메타문자

# 문자 클래스, [ ] 
# 문자 클래스인 []는 "[] 사이의 문자들과 매치"라는 의미를 가지며, []사이에는 어떤 문자도 들어갈 수 있다.
# [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"를 뜻한다.
# 예시) [abc]와 "a", "before", "dude"의 매치
#     - a는 정규식과 일치하는 문자인 a가 있으므로 매치
#     - before는 정규식과 일치하는 문자인 b가 있으므로 매치
#     - dude는 정규식과 일치하는 문자인 a, b, c중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

# 하이픈(-), 캐럿(^)
# 하이픈(-)은 두 문자 사이의 범위(from - to)를 의미, 캐럿(^)은 반대를 의미
# [a-zA-Z]: 알파벳 모두 매치
# [0-9]: 숫자 매치
# [^0-9]: 숫자가 아닌 문자만 매치
# []안에서는 부정의 의미로 사용
# []가 없으면 문자열의 처음을 뜻함(끝은 $로 표시)
# 문자클래스 []안에는 어떤 문자나 메타 문자도 사용할 수 있지만 ^는 반대(not)의 의미로 사용되기 때문에 조심해야한다.

# \(역슬래쉬)
# [0-9]또는 [a-zA-Z]와 같은 정규표현식은 \역슬래쉬를 이용해 간단하게 표현할 수 있다. 

# 자주 사용하는 문자 클래스
# [0-9] → 숫자와 매치, \d
# [^0-9] → 숫자가 아닌 것과 매치, \D
# [ \t\n\r\f\v] → whitespace 문자와 매치(맨 앞의 빈칸은 공백문자(space)를 의미, \s
# [^ \t\n\r\f\v] → whitespace 문자가 아닌 것과 매치, \S
# [a-zA-Z0-9_] → 문자 + 숫자와 매치, \w
# [^a-zA-Z0-9_] → 문자+숫자가 아닌 문자와 매치, \W

# Dot(.)
# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미
# a.b → 정규식의 의미는 "a + 모든문자 + b"와 같다.
# 즉 a와b라는 문자 사이에 어떤 문자가 들어가도 모두 매치가 된다는 의미
# 예시) "aab", "a0b", "abc"
#       aab는 가운데 문자 a가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치됨
#       a0b도 동일하게 가운데 문자 0이 모든 문자를 의미하는 .과 일치하므로 정규식과 매치됨
#       abc는 a와 b사이에 어떤 문자가 존재하지 않기 때문에 위 정규식과 매치되지 않음

# * + ? {} (반복 관련 메타 문자)

# 반복 (*)
# 메타문자 *은 * 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다는 의미

# ca*t -> c + a(0번 이상 반복) + t
# ct → Yes(매치 여부) → a가 0번 반복되어 매치
# cat → Yes(매치 여부) → a가 0번 이상 반복되어 매치(1번 반복)
# caaat → Yes(매치 여부) → a가 0번 이상 반복되어 매치(3번 반복)
# ct, cat, caaaat 모두 매치

# 반복 (+)
# +는 *과 달리 최소 1번 이상 반복될 때 사용
# 즉, *은 반복횟수가 0부터 시작, +는 반복횟수가 1부터 시작

# ca+t -> c + a(1번 이상 반복) + t
# ct → No(매치 여부) → a가 0번 반복되어 매치되지 않음
# cat → Yes(매치 여부) → a가 1번 이상 반복되어 매치(1번 반복)
# caaat → Yes(매치 여부) → a가 1번 이상 반복되어 매치(3번 반복)
# ct, cat, caaat중 ct는 매치되지 않음

# 반복 ({m,n})
# {}는 원하는 반복횟수를 지정하고 싶을 때 사용됩니다. m에서 n까지 반복, m이상인 경우, n이하인 경우 등 자유롭게 원하는 만큼 조절이 가능합니다.
# 1. {m}: 반드시 m번 반복
#   - ca{2}t: c + a(반드시 2번 반복) + t
# 2. {m, n}: m~n회 반복
#   - ca{2, 5}t: c + a(2~5회 반복) + t
# 3. {m,}, {,n}: m회 이상 반복, n회 이하 반복

# 반복(?)
# ?는 반복은 아니지만 비슷한 개념으로 {0, 1}과 같은 의미
# 즉, 문자가 있거나 없거나 둘 다 매치 되는 경우
# ab?c : a + b(있어도 되고 없어도 된다) + c

# *, +, ? 메타 문자는 모두 {m, n} 형태로 고쳐 쓰는 것이 가능하지만 가급적 이해하기 쉽고 간결한 *, +, ? 메타 문자를 사용하는 것이 좋다.

# ---------------------------------------------------------------------------------------------------------------------------------------------

# 파이썬에서 기본 사용법

# 파이썬은 정규표현식을 지원하기 위해 re(regular expression) 모듈 제공
# import re
# pattern = re.compile("정규식")

# re.compile을 사용하여 정규 표현식을 컴파일
# re.compile의 결과인 객체 `pattern`에 입력한 정규식의 대한 정보가 담겨있음

# ex) 이 코드를 실행해 생성된 객체 p로 메서드 살펴보기
import re
p = re.compile('[a-z]+')

# 1. match()
#    문자열의 처음부터 정규식과 매치되는지 조사

m = p.match("python")
print(m)

# <re.Match object; span=(0, 6), match='python'>
# -> python문자열은 [a-z]+정규식에 부합되므로 match 객체를 돌려줌

# 2. search()
#    문자열 전체를 검색하여 정규식과 매치되는지 조사

m = p.search("3 python")
print(m)

# <re.Match object; span=(2, 8), match='python'>
# -> 3 python문자열은 첫번째 문자가 숫자이므로 match메서드에서는 None을 반환합
#    하지만 search메서드는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색하기 때문에 “python”문자열과 매치돼서 match객체를 반환

# 3. findall()
#    정규식과 매치되는 모든 문자열을 리스트로 돌려줌

result = p.findall("life is too short")
print(result)

# ['life', 'is', 'too', 'short']
# → 정규식과 일치하는 부분인 각 단어들이 반환되는 것을 확인할 수 있음

# 4. finditer()
#    정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려줌

result = p.finditer("life is too short")
print(result)

# <callable_iterator object at 0x000002579639BF40>
# → 반복 가능한 객체가 포함하는 각각의 요소는 match 객체
print('--------------------------------------------------')

# match 객체의 메서드
# 1. group()
#    매치된 문자열 돌려줌
# 2. start()
#    매치된 문자열의 시작 위치를 돌려줌
# 3. end()
#    매치된 문자열의 끝 위치를 돌려줌 
# 4. span()
#    매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려줌

m = p.match("python")
print('매치된 문자열 : ', m.group())
print('매치된 문자열의 시작 위치 : ', m.start())
print('매치된 문자열의 끝 위치 : ', m.end())
print('매치된 문자열의 (시작, 끝) : ', m.span())

m = p.search("3 python")
print('매치된 문자열 : ', m.group())
print('매치된 문자열의 시작 위치 : ', m.start())
print('매치된 문자열의 끝 위치 : ', m.end())
print('매치된 문자열의 (시작, 끝) : ', m.span())

# 축약된 형태
m = re.match('[a-z]+', "python")
print(m)
# <re.Match object; span=(0, 6), match='python'>
print('--------------------------------------------------')

# 컴파일 옵션
# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 함
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 함
# MULTILINE(M) - 여러줄과 매치할 수 있도록 함(^, $ 메타문자의 사용과 관계가 있는 옵션)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 함(정규식을 보기 편하게 만들수 있고 주석 등을 사용할 수 있게됨)
# → 옵션을 사용할 때는 re.DOTALL처럼 전체 옵션이름을 써도 되고, re.S처럼 약어를 써도 됨

# DOTALL, S
# .메타 문자가 줄바꿈 문자\n도 포함시키도록 하고 싶다면 re.DOTALL 또는 re.S 옵션을 사용해 정규식을 컴파일하면 됨
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
# <re.Match object; span=(0, 3), match='a\nb'>
# → re.DOTALL옵션으로 \n도 매치시키는 것을 확인할 수 있음

# IGNORECASE, I
# re.IGNORECASE 또는 re.I 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션
p = re.compile('[a-z]', re.I)
p.match('python')
print(m)
# <re.Match object; span=(0, 3), match='a\nb'>
# → [a-z] 정규식은 소문자만을 의미하지만 re.I옵션으로 대소문자 구별없이 매치되는 것을 볼 수 있음

# MULTILINE, M
# `^`은 문자열의 처음, `$`은 문자열의 마지막을 의미
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
# ['python one']
# → 결과를 보면 알겠지만 ^ 메타 문자에 의해 python이라는 문자열을 사용한 첫 번째 줄만 매치

# 하지만 ^ 메타 문자를 문자열 전체의 처음이 아니라 각 라인의 처음으로 인식시키고 싶은 경우가 있을 것임.
# 이럴 때 사용하는 옵션이 바로 re.MULTILINE 옵션임
# re.MULTILINE옵션을 추가
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
# ['python one', 'python two', 'python three']
# → 다음과 같이 ^메타 문자가 문자열의 각 줄마다 적용되는 것을 확인

# ERBOSE, X
# 여태 봐왔듯이 정규식은 굉장히 가독성이 안좋은 것을 알 수 있음
# 이런 정규식의 가독성을 조금이나마 해결해주기 위한 옵션이 바로 VERBOSE

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
print(charref)
# 첫 번째와 두 번째 예를 비교해보면 패턴 객체인 charref는 모두 동일한 역할을 함
# 하지만 두번째처럼 주석을 적고 여러 줄로 표현하는 것이 가독성이 좋은 것
# → re.VERBOSE옵션은 문자열에 사용된 whitespace가 컴파일시 제거되며, #을 이용해 주석문을 달 수 있음