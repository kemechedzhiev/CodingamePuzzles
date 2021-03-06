from datetime import timedelta
from datetime import datetime

# Your program must print formatted string with the number of full years
# and full months (if there are any greater than 0) and the total number
# of days between BEGIN and END dates in dd.mm.yyyy format.
# Example 1:
# Input:
# 01.01.2000
# 01.01.2016
# Output:
# 16 years, total 5844 days

print("Mission started")
date1 = input()
date2 = input()
date1_datetime = datetime.strptime(date1, '%d.%m.%Y')
date2_datetime = datetime.strptime(date2, '%d.%m.%Y')
result = timedelta(date1_datetime, date2_datetime)
print(result)
