ls = 'PySide2.QtCore.QDate(2022, 1, 6)'
# 29-1-2022
# date = list((ls.split('(')[1].split(')')[0]).split(','))
# print(date)
# r_date = f"{date[2]}-{date[1]}-{date[0]}"
# print(r_date)
date = ls.split('(')[1].split(')')[0].split(' ')
r_date = f"{date[2]}-{date[1][0]}-{date[0][0:4]}"
print(r_date)
