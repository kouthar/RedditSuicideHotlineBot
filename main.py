import praw
import bot

comments_replied = bot.get_comments_replied()

reddit = bot.authenticate()

while True:
	bot.run(reddit, comments_replied)