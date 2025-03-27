import string

def format_time(date_time):
   date, time = date_time.split()
   day, month, year = date.split()
   hour, min, sec = time.split()

   if int(day) < 1 or int(day) > 31:
      print("day is invalid")
      return
   if int(month) < 1 or int(month) > 12:
      print("month is invalid")
      return
   if int(year) <1 or int(year) > 9999:
      print("year is invalid")
      return
   
   print("->" + date)
   print("->" + month)
   print("->"+ year)
   if int(hour) > 11:
      print("-> p.m")
   else:
      print("-> a.m")



         
      


format_time("21/02/2020 18:06:00")
print()
format_time("37/05/1950 12:00:00")
print()
format_time("01/01/1900 25:06:00")
