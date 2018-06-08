import praw, prawcore
import datetime
import pprint
import csv

reddit = praw.Reddit(client_id='Kasrtqpem2xOFQ',
                     client_secret='tPFanD4UTe5qLeWwunsBqt7BpLs',
                     password='48151623423004Sfk',
                     user_agent='experimentData',
                     username='catherinesatan')

postInfo = "C:/Users/Ekaterina Yashkina/PycharmProjects/RedditAPI"+"/posts.csv"
commentInfo = "C:/Users/Ekaterina Yashkina/PycharmProjects/RedditAPI"+"/comments_karma.csv"
global limit
limit = 0
subreddits = ('all', 'learnpython', 'programming', 'javahelp', 'soccer', 'BlackPeopleTwitter','security','funny')
fields_sub = ('id', 'created_utc', 'score')
fields_com = ('id', 'parent_id', 'score', 'created_utc')

post_dict = {
        "author_id":[],
        "author_name":[],
        "author_karma":[],
        "author_karma_com":[],
        "id":[],
        "created_utc":[],
        "score":[]
    }

comment_dict = {
        "id":[],
        "author_id":[],
        "parent_id":[],
        "created_utc":[],
        "score":[],
        "karma":[]
    }


def main():
    for elem in subreddits:
        getAll(elem)
    write_to_csv(post_dict, comment_dict)




def getAll(subreddit):
    submissions = reddit.subreddit(subreddit).hot(limit=1000)
    submissionList = []
    counter = 0
    commentsList = []
    for submission in submissions:
        try:
            if submission.author is not None and \
                    datetime.datetime.fromtimestamp(submission.created).date()==datetime.datetime.now().date()-datetime.timedelta(1):
                post_dict['author_id'].append(submission.author.id)
                post_dict['author_name'].append(submission.author.name)
                post_dict['author_karma'].append(submission.author.link_karma)
                post_dict['author_karma_com'].append(submission.author.comment_karma)
                to_dict = vars(submission)
                for field in fields_sub:
                    post_dict[field].append(to_dict[field])
                counter+=1
                print(counter)
                submission.comments.replace_more(limit=0)
                comments = submission.comments
                lim = 0
                for comment in comments:
                    global limit
                    limit = 0
                    if (lim>10):
                        break
                    if comment.author is not None:
                        comment_dict['author_id'].append(comment.author)
                        comment_dict['karma'].append(comment.author.comment_karma)
                        lim += 1
                        to_dict = vars(comment)
                        for field in fields_com:
                            comment_dict[field].append(to_dict[field])
        except prawcore.exceptions.NotFound:
            continue



def getSubComments(comment,verbose=True):
    global limit
    if comment.author is not None:
        to_dict = vars(comment)
        for field in fields_com:
            comment_dict[field].append(to_dict[field])
        comment_dict['author_id'].append(comment.author.id)
        limit+=1
    if not hasattr(comment, "replies"):
        replies = comment.comments()
    else:
        replies = comment.replies
    for child in replies:
        if (limit>5):
            break
        getSubComments(child, verbose=verbose)



def write_to_csv(dictionary_posts, dictionary_comments):
    with open(postInfo, "a", newline='' ) as outfile:
        writer = csv.writer(outfile)
        #writer.writerow(dictionary_posts.keys())
        writer.writerows(zip(*dictionary_posts.values()))

    with open(commentInfo, "a", newline='') as outfile1:
        writer = csv.writer(outfile1)
        #writer.writerow(dictionary_comments.keys())
        writer.writerows(zip(*dictionary_comments.values()))


if __name__ == "__main__": main()
