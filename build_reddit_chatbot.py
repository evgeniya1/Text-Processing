import praw
from datetime import datetime, timedelta

## read posos from subreddit and save in txt
reddit = praw.Reddit(user_agent=True,
                     client_id="client_id",
                     client_secret="client_secret",
                     username="username",
                     password="password")

subreddit = reddit.subreddit("glassblowing")

posts_24h = []

with open('reddit_output.txt', 'w') as file:
for post in subreddit.new():
  current_time = datetime.utcnow()
  post_time = datetime.utcfromtimestamp(post.created)

  delta_time = current_time - post_time

  if delta_time <= timedelta(hours=48):
    print(post.title, post.selftext)
    posts_24h.append((post.title, post.selftext, post.created))
    file.write(f"{post.title}\n{post.selftext}\n\n")

    ##add post reply
    # if "christmas" in post.title.lower():
    #   post.reply("Hey guys, Christmas is coming!")
    
    ##add comment reply
    for comment in post.comments:
      for comment in comment.body.lower():
        comment.reply("Yes, it is comming")



##write a post to pythonsandlot
title = "This is my Python Bot submission"
text = """
Hey, I am just trying Python Bot.
This is my first post!"""

subreddit = reddit.subreddit("pythonsandlot")
subreddit.validate_on_submit = True
subreddit.submit(title=title, selftext=text)

