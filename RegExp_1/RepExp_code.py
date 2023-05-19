# match()
import re
p = re.compile('[a-z]+')

m = p.match("python")
print(m)

# search()
m = p.search("3 python")
print(m)

# findall()
result = p.findall("life is too short")
print(result)

# finditer()
result = p.finditer("life is too short")
print(result)

print('--------------------------------------------------')

# match 객체의 메서드
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

print('--------------------------------------------------')

# 컴파일 옵션
# DOTALL, S
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE, I
p = re.compile('[a-z]', re.I)
p.match('python')
print(m)

# MULTILINE, M
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

# re.MULTILINE옵션을 추가
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

# ERBOSE, X
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







