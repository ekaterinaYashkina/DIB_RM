import csv
def main():
    unique = []
    users = []
    with open("posts.csv", "r", encoding="utf_8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] in unique:
                users.append(row[1])
            unique.append(row[1])

    with open("us.csv", 'w') as outp:
        writer = csv.writer(outp)
        writer.writerow(users)

if __name__ == "__main__": main()

