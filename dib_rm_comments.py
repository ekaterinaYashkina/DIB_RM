import csv, datetime
from operator import itemgetter
#global a
#a = 1
#global b
#b = 0.9
path = "postInfo4.csv"
output = "test_data.csv"
global ta, an
ta = 3600*24
global Ib
Ib = 1

data = {
        "id":[],
        "author_id":[],
        "parent_id":[],
        "created_utc":[],
        "score":[],
        "karma":[],
        "dib_rm":[]
    }

def trust(dn, In, n, b):
    #global b
    trust =[None]*n
    trust[0] = In[0]
    for i in range(1, n):
        trust[i] = trust[i-1]*pow(b, dn[i])+In[i]
    return trust

def retrieve (a, b):
    with open("test_data_comments.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data.keys())
    users = {}
    with open ("comments_karma.csv", "r", encoding="utf_8") as csvfile:
        reader = csv.reader(csvfile)
        c = 0
        for row in reader:
            print(row)
            if c!=0:
                row[3] = datetime.datetime.fromtimestamp(float(row[3]))
                if not row[1] in users.keys():
                    users.setdefault(row[1], [])
                    users[row[1]].append(row)
                else:
                    users[row[1]].append(row)
                users[row[1]] = sorted(users[row[1]], key = itemgetter(3))
            c+=1
    for key in users:
        In, dn, n = cum_part(users[key], a)
        #print (users[key], In, dn, n)
        trust1 = trust(dn, In, n, b)
        u = users[key]
        for i in range(len(u)):
            data["id"].append(u[i][0])
            data["author_id"].append(u[i][1])
            data["parent_id"].append(u[i][2])
            data["created_utc"].append(u[i][3])
            data["score"].append(u[i][4])
            data["karma"].append(u[i][5])
            data["dib_rm"].append(trust1[i])


    with open("test_data_comments.csv", "a", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(zip(*data.values()))





def cum_part(user_data,a):
    n = len(user_data)
    global ta
    periods = []
    for row in user_data:
        if row [3] not in periods:
            periods.append(row[3])
    An = len(periods)
    cum = [None]*n
    dn = [None]*n
    for i in range(0, n):
        data = user_data[i]
        cum[i] = (float(data[-2]))*a*(1-1/(An+1))+float(data[-2])
        if i ==0:
            dn[i] = 1
        else:
            #print((data[1]-user_data[i-1][1]).total_seconds())
            dn[i] = ((data[3]-user_data[i-1][3]).total_seconds())/float(ta)

    return cum, dn, n



if __name__ == "__main__":

    user_data = retrieve(4, 0.99)
    #print(user_data)