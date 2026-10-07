# ---- Reading input ----
# Use these EXACT prompt strings so your program matches the required format.
# How many times you read, and in what order, is up to you.
#
#   the day:   int(input("Enter day (1-8): "))
#   each age:  int(input("Enter age (-1 to stop): "))
#
# Reading stops when the age entered is -1 (the -1 is not counted as a visitor).


# ---- Your program ----
# Read the input and work everything out here. How you structure and order
# the steps is up to you.

# INPUT PROCEDURE

input_day = int(input("Enter day (1-8): "))
day = ""

# 1-5 = weekday, 6-7 = weekend, 8 = holiday
if input_day >= 1 and input_day <= 5:
    day = "weekday"
elif input_day >= 6 and input_day <= 7:
    day = "weekend"
else:
    day = "holiday"

visitor_num = 0
child = 0
adult = 0
senior = 0

input_visitor = int(input("Enter age (-1 to stop): "))

while input_visitor != -1:
    visitor_num += 1

    # 0-12 = child, 13-59 = adult, 60+ = senior
    if input_visitor >= 0 and input_visitor <= 12:
        child += 1
    elif input_visitor <= 59:
        adult += 1
    else:
        senior += 1

    input_visitor = int(input("Enter age (-1 to stop): "))

# GROUP COUNT PROCEDURE

group_num = adult // 5
left_adult = adult % 5

# TICKET PRICE COUNT PROCEDURE

ticket_price = 0.0 # float type

if day == "weekday":
    ticket_price = 30.0 * child + 60.0 * left_adult + 40.0 * senior + 35.0 * (group_num * 5)

if day == "weekend":
    ticket_price = 40.0 * child + 80.0 * left_adult + 50.0 * senior + 65.0 * (group_num * 5)

if day == "holiday":
    ticket_price = 50.0 * child + 100.0 * left_adult + 60.0 * senior + 75.0 * (group_num * 5)

# DISCOUNT PROCEDURE

discount = 0.0 # float type

if group_num != 0 and day != "weekday":
    discount = 0.1 * ticket_price

# SERVICE FEE PROCEDURE

service = 0.0 # float type

if not (day == "weekday" and visitor_num < 3):
    service = visitor_num * 5.0
    if service >= 30.0:
        service = 30.0

# ---- Output ----
# Replace each ??? with the value you computed. Keep every label, space, and
# the "{:.2f}" formatting exactly as shown — your output is compared exactly.

print("Day type:", day)
print("Children:", child)
print("Adults:", adult)
print("Seniors:", senior)
print("Total people:", visitor_num)
print("Groups formed:", group_num)
print("Discount:", "{:.2f}".format(discount))
print("Service fee:", "{:.2f}".format(service))
print("Total cost:", "{:.2f}".format(ticket_price - discount + service))