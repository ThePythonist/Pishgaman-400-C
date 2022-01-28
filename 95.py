import jdatetime

jalali = str(jdatetime.date.fromgregorian(day=23, month=1, year=2022))
print(type(jalali))

day = jalali[-2:]
month = jalali[-5:-3]
year = jalali[:4]
# date = {
#     "Rooz" : day,
#     "Mah" : month,
#     "Sal" : year,
# }
# print(date)

print("Rooz :",day)
print("Mah :",month)
print("Sal :",year)
