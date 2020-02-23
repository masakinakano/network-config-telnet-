
import telnetlib

HOST = "ホストのアドレス"

password = "パスワード"

tn = telnetlib.Telnet(HOST)##実際にtelnet通信の開始


tn.read_until(b"Password: ")##passwordという文字が出るまで待機してね
tn.write(password.encode('ascii') + b"\n")##password変数の中身をアスキーでえんこーどしたあとエンター


tn.write(b"enable\n")
tn.write(b"パスワード\n")
tn.write(b"show run\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))##すべての文字入力を移す