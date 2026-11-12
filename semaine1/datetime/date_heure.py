from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "Fr_CA.utf8") # Trvailler ne français


maintenant = datetime.now()
print(maintenant.year)
print(maintenant.month)
print(maintenant.day)
print(maintenant.strftime("%d/%m/%y"))
print(maintenant.strftime("%B% %d Y% %I %M% %p"))


date1 = datetime(200,12,25)
print(date1.date())

str_date2= staetime.strptime(strptime)