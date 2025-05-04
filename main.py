from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
import requests

# Making a function for further use on the website
def gettingthemusic(QUERY):
	#  API_KEY
	API_KEY = "YOUR_KEY"


	# Freesound.org URL for particular sound
	URL = f"https://freesound.org/apiv2/search/text/?query={QUERY}&token={API_KEY}"


	# Making the API request
	response = requests.get(URL)


	# Checking if the request was successful
	if response.status_code == 200:
		# Fetching id in JSON response
		music_id = response.json()["results"][0]["id"]
	else:
		print(f"Error: {response.status_code}")


	# URL for downloading the particular sound by id
	DOWNLOADER = f"https://freesound.org/apiv2/sounds/{music_id}/download/"

	return DOWNLOADER


app = Flask(__name__)
Bootstrap5(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		QUERY = request.values
		return redirect(gettingthemusic(QUERY=QUERY))
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
