import requests
from day22_23 .send_email import send_email


api_key = ""
url = "https://newsapi.org/v2/everything?q=linux&" \
      "sortBy=publishedAt&apiKey=" \
      "890603a55bfa47048e4490069ebee18c"
make_list = []
message = ""

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"][:2]:
    # title = article["title"]
    # description = article["description"]
    # source = article["source"]["name"]
    # link = article["url"]
# Make dictionary and append it to list
    #make_list.append({"title": title, "description": description, "source": source, "link": link})
    nl = "\n"
    message += f"""\
    {nl} Title: {article["title"]}

    Description: {article["description"]} 
    Source: {article["source"]["name"]} 
    URL: {article["url"]} {nl}"""
    # message_list.append(make_string)
   # message += make_string

# Form message for e-mail
# for item in make_list:
#     nl = "\n"
#     make_string = f"""\
# {nl} Title: {item["title"]}<<<<<<<<
#
# Description: {item["description"]}
# Source: {item["source"]}
# URL: {item["link"]} {nl}"""
#     # message_list.append(make_string)
#     message += make_string

send_email(message.encode())
