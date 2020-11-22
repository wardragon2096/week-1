hourly_wages = float(input("Enter hourly wage: "))
regular_hours = float(input("Enter total number of regular hours: "))
overtime_hours = float(input("Enter overtime hours: "))
weekly_pay = (hourly_wages * regular_hours) + (1.5 * hourly_wages * overtime_hours)
print ("Total weekly pay:", weekly_pay)
