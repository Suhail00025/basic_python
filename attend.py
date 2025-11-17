attendance = [18,20,19,15,21]

full_days = 0
total_attendance = 0

for i in attendance:
    if i >= 20:
        print("attendance full")
        full_days += 1
    else:
        print("attendance not full")

    total_attendance += i

print("Total full attendance days:", full_days)
print("Total attendance over the period:", total_attendance)