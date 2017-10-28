import praw
import config
import time

def authenticate():
	reddit = praw.Reddit(username = config.username, 
		password = config.password, 
		client_id = config.client_id, 
		client_secret = config.client_secret, 
		user_agent = config.user_agent)
	return reddit

def get_comments_replied():
	with open("comments_replied.txt", r) as file:
		comments_replied = file.read()
		comments_replied = comments_replied.split("\n")
		comments_replied = filter(None, comments_replied)
	return comments_replied


def run(reddit, comments_replied):

	for comment in reddit.subreddit('depression').comments(limit=25):
		if "!SuicideHotlines" in comment.body and comment.id not in comments_replied:
			print("Found comment")
			comment.reply("[Here] (http://ibpf.org/resource/list-international-suicide-hotlines) is a list of international suicide hotlines. I am a bot.")
			print("Replied")
			comments_replied.append(comment.id)

			with open("comments_replied.txt", "a") as file:
				file.write(comment.id + "\n")

	time.sleep(60)