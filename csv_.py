import csv

#............. Open CSV files................
with open("users_info/users.csv", "w", newline='') as users_data:
    CSV_writer_data = csv.writer(users_data)

    # row 1 >>>>>>>> Table heading 
    CSV_writer_data.writerow(["User Name", "User ID", 'Status'])

    # row 2 ...........
    CSV_writer_data.writerow(['Cools', 111, "welcome"])
    CSV_writer_data.writerow(['Cools', 111, "welcome"])
    CSV_writer_data.writerow(['Cools', 111, "welcome"])
    CSV_writer_data.writerow(['Cools', 111, "welcome"])
    CSV_writer_data.writerow(['Cools', 111, "welcome"])


# Reading Csv
with open("users_info/users.csv") as users_data:
    CSV_writer_data = csv.reader(users_data)
    # print(list(CSV_writer_data))
    for x in CSV_writer_data:
        print(x)