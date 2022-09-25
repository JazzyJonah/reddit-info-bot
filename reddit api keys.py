import requests
import os

CLIENT_ID = "C61Gmz2FZw7ifb9TjL4jYQ"
REDDIT_SECRET_KEY = os.getenv("REDDIT_SECRET_KEY")

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, REDDIT_SECRET_KEY)
with open("pw.txt", "r") as f:
	pw = f.read()
data = {
	"grant_type": "password",
	"username": "JazzyJonah312"
	"password": pw
}