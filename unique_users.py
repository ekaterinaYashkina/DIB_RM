import csv
def main():
    unique = []
    #users = []
    with open("comments_karma.csv", "r", encoding="utf_8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] not in unique:
                unique.append(row[1])

    with open("us.csv", 'w') as outp:
        writer = csv.writer(outp)
        writer.writerow([len(unique)])

if __name__ == "__main__": main()

