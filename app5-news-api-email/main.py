import requests
from day22_23 .send_email import send_email


api_key = ""
url = "https://newsapi.org/v2/everything?q=Jesus&" \
      "sortBy=publishedAt&apiKey=" \
      "KEY"

message = ""

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    if article["description"] is not None:
        message += f"""\
        \n Title: {article["title"]}
        
        Description: {article["description"]}
        Source: {article["source"]["name"]}
        URL: {article["url"]} \n"""

send_email(message.encode("utf-8"))
