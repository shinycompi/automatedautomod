import time
import praw
import argparse
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

parser=argparse.ArgumentParser()
parser.add_argument('--username', required=True, help="Reddit's account username")
parser.add_argument('--password', required=True, help="Reddit's account password")
parser.add_argument('--subreddit', required=True, help="The subreddit to create the posts in")
parser.add_argument('--force', action="store_true", help="Run silent")
args=parser.parse_args()

if args.force:
    answer = 'y'
else:
    answer = input("Do you want to create posts in /r/{}? [y/N] ".format(args.subreddit))

if answer == "y":
    reddit = praw.Reddit(
        client_id=config["reddit"]["client_id"],
        client_secret=config["reddit"]["client_secret"],
        user_agent=config["reddit"]["user_agent"],
        username=args.username,
        password=args.password,       
    )

    posts = []
    # posts.append({"title": "Monday post", "selftext": "This is a Monday post", "flair_id": "2cd88b18-8f89-11ec-affe-c257ee8a170d" })
    # posts.append({"title": "Tuesday post", "selftext": "This is a Tuesday post", "flair_id": "31e95cae-8f89-11ec-9487-de8c0a743a65" })
    # posts.append({"title": "Wednesday post", "selftext": "This is a Wednesday post", "flair_id": "3923e066-8f89-11ec-b7f1-92c892ff4388" })
    # posts.append({"title": "Thursday post", "selftext": "This is a Thursday post", "flair_id": "3ce37216-8f89-11ec-99f5-a6dbfaae1a62" })
    # posts.append({"title": "Friday post", "selftext": "This is a Friday post", "flair_id": "4074e7ac-8f89-11ec-b856-ae8840cec4a2" })
    # posts.append({"title": "Saturday post", "selftext": "This is a Saturday post", "flair_id": "43a500a6-8f89-11ec-a5da-061a91d2266e" })
    # posts.append({"title": "Sunday post", "selftext": "This is a Sunday post", "flair_id": "464b6d0e-8f89-11ec-bb23-92943ba1c250" })

    posts.append({"title": "A help post", "selftext": "This is a help post.", "flair_id": "8eef76ac-86a3-11ec-a75f-26934a07f0e5"})
    posts.append({"title": "A meme post", "selftext": "This is a meme post", "flair_id": "928f2da2-86a3-11ec-8628-a6b4cfaf41d8"})
    posts.append({"title": "A concept post", "selftext": "This is a concept post", "flair_id": "95d37900-86a3-11ec-b263-62b3a353c815"})
    posts.append({"title": "An other post", "selftext": "This is an other post", "flair_id": "95d37900-86a3-11ec-b263-62b3a353c815"})
    posts.append({"title": "An unflaired post", "selftext": "This is an unflaired post", "flair_id": ""})

    for post in posts:
        reddit.subreddit(args.subreddit).submit(post["title"], selftext=post["selftext"], flair_id=post["flair_id"])
        time.sleep(1)

else:
    print("abort")



