import datetime, csv, math
def main(a, b):
    users = {}
    with open("C:/Users/Ekaterina Yashkina/PycharmProjects/RedditAPI"+"/test_data_comments.csv", "r") as outfile:
        reader = csv.reader(outfile)
        c = 0
        for row in reader:
            if c!=0:
                if not row[1] in users.keys():
                    # print("hi")
                    users.setdefault(row[1], {})
                    users[row[1]] = {row[3]:math.fabs(float(row[-2])-float(row[-1]))}

                else:
                    for key in users[row[1]].keys():
                        if (datetime.datetime.strptime((key), "%Y-%m-%d %H:%M:%S").date()==datetime.datetime.strptime((row[3]), "%Y-%m-%d %H:%M:%S").date()
                            and datetime.datetime.strptime((key), "%Y-%m-%d %H:%M:%S") < datetime.datetime.strptime((row[3]), "%Y-%m-%d %H:%M:%S")):
                                del users[row[1]][key]
                                users[row[1]][row[3]] = math.fabs(float(row[-2])-float(row[-1]))
            c+=1
    sum_us = 0
    for key in users.keys():
        sum_1 = 0
        u = users[key]
        for value in u.values():
            sum_1 += value
        sum_1 = sum_1/float(len(u))
        sum_us +=sum_1

    sum_us = sum_us/(float(len(users)*len(users)))
    out = 1-sum_us
    with open("comparision_comments.txt", "a", newline='') as file:
        file.writelines([str(a) + " " +str(b)+ " " +str(out)+'\n'])

if __name__ == "__main__":
    main(4, 0.99)