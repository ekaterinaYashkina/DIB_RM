import praw
import prawcore
import csv

fields_com = ('id','author_id' 'parent_id', 'score', 'created_utc', 'karma')
commentInfo = "C:/Users/Ekaterina Yashkina/PycharmProjects/RedditAPI"+"/comments_karma.csv"

reddit = praw.Reddit(client_id='Kasrtqpem2xOFQ',
                     client_secret='tPFanD4UTe5qLeWwunsBqt7BpLs',
                     password='48151623423004Sfk',
                     user_agent='experimentData',
                     username='catherinesatan')

comment_dict = {
        "id":[],
        "author_id":[],
        "parent_id":[],
        "created_utc":[],
        "score":[],
        "karma":[]
    }

def get_karma():
    with open ("comments.csv", 'r', newline='') as file:
       reader = csv.reader(file)
       c = 0
       for row in reader:
           print(c)
           if c!=0:
               users = row
               id = row[1]
               karma = 0
               try:
                   karma = reddit.redditor(id).comment_karma
               except AttributeError as error:
                   karma = 0
               except prawcore.exceptions.NotFound:
                   karma = 0
               comment_dict["id"].append(users[0])
               comment_dict["author_id"].append(users[1])
               comment_dict["parent_id"].append(users[2])
               comment_dict["created_utc"].append(users[3])
               comment_dict["score"].append(users[4])
               comment_dict["karma"].append(karma)
           c+=1

def write_to_csv():
    with open(commentInfo, "a", newline='') as outfile1:
        writer = csv.writer(outfile1)
        writer.writerow(comment_dict.keys())
        writer.writerows(zip(*comment_dict.values()))

def main():
    get_karma()
    write_to_csv()

if __name__ == "__main__": main()
