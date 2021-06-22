import pandas as pd
import praw
import datetime

reddit = praw.Reddit(
    client_id = 'q2veOt9-Hq-NtA',
    client_secret = 'A43dU4NkSAUoDyGFRl_TjxyMQ0rX0A',
    user_agent = True
)

subreddit = reddit.subreddit('korea')

post_dict = {
            "title" : [],   #title of the post
            "score" : [],   # score of the post
            "id" : [],      # unique id of the post
            "url" : [],     #url of the post
            "comms_num": [],   #the number of comments on the post
            "created" : [],  #timestamp of the post
            "body" : []         # the descriptionof post
        }
comments_dict = {
            "comment_id" : [],      #unique comm id
            "comment_parent_id" : [],   # comment parent id
            "comment_body" : [],   # text in comment
            "comment_link_id" : []  #link to the comment
        }

for submission in subreddit.top(time_filter='year'):
    post_dict['title'].append(submission.title)
    post_dict['score'].append(submission.score)
    post_dict['id'].append(submission.id)
    post_dict["url"].append(submission.url)
    post_dict["comms_num"].append(submission.num_comments)
    post_dict["created"].append(datetime.datetime.fromtimestamp(submission.created/1000))
    post_dict["body"].append(submission.selftext)
    
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments_dict['comment_id'].append(comment.id)
        comments_dict['comment_parent_id'].append(comment.parent_id)
        comments_dict['comment_body'].append(comment.body)
        comments_dict['comment_link_id'].append(comment.link_id)
        
post_comments = pd.DataFrame(comments_dict)
post_comments.to_csv('Korea_subreddit_comments.csv')
post_data = pd.DataFrame(post_dict)
post_data.to_csv('Korea_subreddit.csv')