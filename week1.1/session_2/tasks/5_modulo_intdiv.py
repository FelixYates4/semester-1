# this program takes a file which contains students IDs and the hours late that work was submitted
# it needs to convert the minutes late into days, hours and minutes
# all file handling has been done - the section you need to edit is marked by comments below

with open("_data/lateness_data.csv") as f:
    data = f.readlines()

data = [line.strip().split(",") for line in data]

for row in data:
######### This is the section where you will need to make some changes #############


    # minutes_late is the number of minutes late a submission was made
    minutes_late = int(row[1])
    days = minutes_late // 1440
    minutes_late -= days * 1440
    hours = minutes_late // 60
    minutes_late -= hours * 60
    minutes = minutes_late

    
    print(f"Student {row[0]}: {days}D {hours}H {minutes}M")

