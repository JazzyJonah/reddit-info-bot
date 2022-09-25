import requests
from requests.structures import CaseInsensitiveDict


def check_reddit_account(reddit_account):
	url = "https://www.reddit.com/user/" + reddit_account + ".json?limit=1"
	headers = CaseInsensitiveDict()
	headers["User-Agent"] = "chrome"
	resp = requests.get(url, headers=headers)
	post = resp.json()
	resp = (post['data']['children'][0]['data']['title'])
	if resp != 'Update 1.6 is Coming Soon - Update Notes!':
		return [True, resp, (post['data']['children'][0]['data']['permalink'])]
	else:
		return False
