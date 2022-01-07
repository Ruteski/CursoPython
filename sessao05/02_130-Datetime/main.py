# https://docs.python.org/3.10/library/datetime.html

from datetime import datetime, timedelta

# data = datetime(2022,7,22,23,29,15)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

# data = datetime.strptime('22/07/2022', '%d/%m/%Y')
# print(data)
# print(data.timestamp())

# data = datetime.fromtimestamp(1658458800.0)
# print(data)

# data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# data = data + timedelta(days=5, seconds=2*60*60)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))


d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

diff = d2 - d1
print(diff.seconds)
print(diff.total_seconds())
print(diff.days)
print(d1.time())
print(d2 > d1)

