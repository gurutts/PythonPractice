filename = input("파일 이름을 입력하시오 : ")
delete = input("삭제할 문자열을 입력하시오 : ")
t = open(filename, "r+")
s = t.read()
a = s.replace("delete", "")
a = a.replace(" ", "")
t.seek(0)
t.write(a)
t.truncate()
t.write(s)
t.close()
