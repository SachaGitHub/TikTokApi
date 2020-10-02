from bs4 import *
import requests
import time
import json

class Api:
	def __init__(self):
		self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
	def get_likes(self, name):
		name = name
		link = "https://www.tiktok.com/node/share/user/" + str(name)
		try:
			r = requests.get(link, headers=self.headers).json()
			jtopy = json.dumps(r)
			infos =json.loads(jtopy)
			heart = infos["body"]["userData"]["heart"]
			return heart
		except:
			print("Can't get hearts, not found !")
	def get_infos(self, name):
		name = name
		link = "https://www.tiktok.com/node/share/user/" + str(name)
		try:
			r = requests.get(link, headers=self.headers).json()
			jtopy = json.dumps(r)
			infos =json.loads(jtopy)
			status = infos["body"]["userData"]
			return status
		except:
			print("Can't get status, not found !")
	def get_followers(self, name):
		name = name
		link = "https://www.tiktok.com/node/share/user/" + str(name)
		try:
			r = requests.get(link, headers=self.headers).json()
			jtopy = json.dumps(r)
			infos =json.loads(jtopy)
			followers = infos["body"]["userData"]["fans"]
			return followers
		except:
			print("Can't get followers, not found !")
	def get_videos(self, name):
		try:
			name = name
			link = "https://www.tiktok.com/node/share/user/" + str(name)
			r = requests.get(link, headers=self.headers).json()
			jtopy = json.dumps(r)
			infos =json.loads(jtopy)
			videos = infos["body"]["userData"]["video"]
			return videos
		except:
			print("Can't get videos, not found !")
	def download_video(self, link):
		link = link
		request_download = requests.get(link, headers=self.headers)
		soup = BeautifulSoup(request_download.text, "html.parser")
		video = soup.find("video").get("src")
		return video


