import csv, datetime
from operator import itemgetter
global a
a = 8
global b
b = 0.9
path = "C:/Users/Ekaterina Yashkina/Downloads"+"/comments.csv"
global ta, an, n
ta = 3600
global Ib
Ib = 1

def trust(dn, In):
    global n, b
    trust =[None]*n
    trust[0] = In[0]
    for i in range(1, n):
        trust[i] = trust[i-1]*pow(b, dn[i])+In[i]
    return trust

def newPost():
    h = 0
    input = open(path, 'r', encoding='utf_8_sig')
    output = open("postInf.csv", 'w', newline='', encoding='utf_8_sig')
    writer = csv.writer(output)
    for row in csv.reader(input):
        #row = bytes(row, 'utf-8').decode('utf-8', 'ignore')
        if row and len(row)>8:
            writer.writerow(row)
    input.close()
    output.close()


def retrieve (username):
    user_data  = []
    with open ("postInf.csv", "r", encoding="utf_8_sig") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_data_full = []
            if row[-6]==username:
                #print(row)
                if row not in row_data_full:
                    row_data = []
                    row_data_full.append(row)
                    row_data.extend([row[-10], datetime.datetime.fromtimestamp(float(row[-7])), row[-6], int(row[-5]), int(row[-4]), int(row[-3]), int(row[-2])])
                    user_data.append(row_data)
    #user_data = sorted(user_data, key = itemgetter(1))
    global n
    n = len(user_data)
    #print(n)
    return user_data

def cum_part(user_data):
    global a, n, ta
    periods = []
    for row in user_data:
        if row [1] not in periods:
            periods.append(row[1])
    An = len(periods)
    cum = [None]*n
    dn = [None]*n
    for i in range(0, n):
        data = user_data[i]
        cum[i] = (data[3]-data[4])*a*(1-1/(An+1))+data[3]-data[4]
        if i ==0:
            dn[i] = 1
        else:
            #print((data[1]-user_data[i-1][1]).total_seconds())
            dn[i] = ((data[1]-user_data[i-1][1]).total_seconds())/float(ta)
    print(cum)
    print(dn)

    return cum, dn

def all_users_exp():



if __name__ == "__main__":
    #newPost()
    user_data = retrieve("CRCbot")
    print(user_data)
    In, dn = cum_part(user_data)
    trust = trust(dn, In)
    print(trust)

