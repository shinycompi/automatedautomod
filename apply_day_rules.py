import automoderator_automator as aa
import praw
import argparse
import configparser
import datetime

config = configparser.ConfigParser()
config.read('config.ini')

parser=argparse.ArgumentParser()
parser.add_argument('--username', required=True, help="Reddit's account username")
parser.add_argument('--password', required=True, help="Reddit's account password")
parser.add_argument('--subreddit', required=True, help="The subreddit with the automoderator to be overwritten")
parser.add_argument('--force', action="store_true", help="Run silent")
args=parser.parse_args()

if args.force:
    answer = 'y'
else:
    answer = input("Do you want to rewrite the automoderator page of /r/{}? [y/N] ".format(args.subreddit))

if answer == "y":
    reddit = praw.Reddit(
        client_id=config["reddit"]["client_id"],
        client_secret=config["reddit"]["client_secret"],
        user_agent=config["reddit"]["user_agent"],
        username=args.username,
        password=args.password,       
    )

    page = reddit.subreddit(args.subreddit).wiki["config/automoderator"]

    automod_lines = page.content_md.splitlines()
    rule_blocks = aa.create_rule_blocks(automod_lines)
    automod_lines = aa.apply_rules_to_automod_lines(rule_blocks, automod_lines)
    automod = "\n".join(automod_lines)

    if automod != page.content_md:
        page.edit(automod)
        print(str(datetime.datetime.now()) + " : /r/" + args.subreddit + " changed")
    else:
        print(str(datetime.datetime.now()) + " : No changes made to /r/" + args.subreddit)
else:
    print("Operation aborted")