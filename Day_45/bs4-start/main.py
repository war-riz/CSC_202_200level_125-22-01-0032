from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/newest")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find(name = "a", rel = "nofollow")
article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvote = soup.find(name = "span", class_ = "score").getText()

print(article_text)
print(article_link)

# with open("website.html") as file:
#     content = file.read()

# soup = BeautifulSoup(content, 'html.parser')

# print(soup.title.name)
# # soup.title.string
# # soup.p
# # soup.prettify()
# # soup.find_all(name = "a")

# # for tag in all_anchor_tags:
# #    print(tag.getText())
# #    print(tag.get("href"))

# # soup.find(name = "h1", class_ = "heading")
# # soup.select_one(selector = "p a")
# # soup.select(".heading") 