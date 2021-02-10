import praw
import urllib.request
import re
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def auth():
	g_login = GoogleAuth()
	g_login.LocalWebserverAuth()
	drive = GoogleDrive(g_login)
	return drive


class ImageCrawler():
	def __init__(self, subreddit, batch, drive):
		self.subreddit = subreddit
		self.batch = batch
		self.drive = drive

	def login(self):
		return praw.Reddit(client_id='',
			client_secret='-uj9G-B8',
			user_agent='',
			username='',
			passward='')

	def reddit(self):
		reddit = self.login()
		subreddit = reddit.subreddit(self.subreddit)
		index = 0
		for submissions in subreddit.hot(limit=self.batch):
			try:
				file_name = str(submissions.title)
				file_name = re.sub(r'[^\w]', ' ', file_name)
				file_format = '.jpg'
				file = file_name + file_format
				urllib.request.urlretrieve(submissions.url, file)
				self.upload(file)
				index = index + 1
				os.remove(file)
				print("{}/{}".format(index,self.batch))
			except:
				print("Error, next img")
				index = index +1
				pass

	def upload(self,file):
		file_drive = self.drive.CreateFile({'title':file })  
		file_drive.SetContentFile(file)
		file_drive.Upload()

if __name__ == "__main__":
	drive = auth()
	os.system('cls')
	lista = [('',75), ('',20), ('',10), ('',15), ('',10), ('',25)]
	for sub, batch in lista:

		print("Subreddit: {}".format(sub))
		crawler = ImageCrawler(sub,batch,drive)
		crawler.reddit()


		os.system('cls')

