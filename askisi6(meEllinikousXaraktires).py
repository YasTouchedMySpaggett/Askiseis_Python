import calendar
y = int(input("����� ����������: "))
m = int(input("����� ��� ���� : "))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(y, m))

