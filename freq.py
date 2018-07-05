import csv
def main():
    occur = []
    users = []
    with open("posts.csv", "r", encoding="utf_8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] not in users:
                users.append(row[1])
                occur.append(0)
                occur[users.index(row[1])] = 1
            else:
                occur[users.index(row[1])] +=1

        el = max(occur)
        occur[occur.index(el)] = 0
        el = max(occur)
        i = occur.index(el)



    with open("user.csv", 'w') as outp:
        writer = csv.writer(outp)
        writer.writerow([users[i]])

if __name__ == "__main__": main()