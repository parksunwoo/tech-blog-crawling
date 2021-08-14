import requests
from bs4 import BeautifulSoup
import feedparser

#https://github.com/jamjam0109/notion/blob/16be770832b49d9855b94f7d13c6fc517db22b98/crawling_selenium.py
#https://github.com/namgunghyeon/bot/blob/2831138f11251a08b02cc938f477ff0a51937b6b/tech_bot/src/crawling/naver.py
def parsing_beautifulsoup(url):
    data = requests.get(url)
    html = data.text
    
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def parsing_feedparse(url):
    feed = feedparser.parse(url)
    return feed

def extract_blog_naver(feed):
    upload_contents = ''
    for post in feed.entries:
        blog_title = post.title
        created_date = post.updated
        url = post.id

        content = f"<a href={url}" + blog_title + "</a>" + ", " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents

def extract_blog_kakao(soup):
    upload_contents = ''
    new_posts = soup.select(".list_post > li")
    url_prefix_kakao = ""

    for new_post in new_posts[:5]:

        blog_title = new_post.select('strong')[0].text
        created_date = new_post.select('span')[0].text
        url_suffix = new_post.select_one(".link_post")['href']
        url = url_prefix_kakao + url_suffix

        content = f"<a href={url}>" + blog_title + "</a>" + " " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents    


def extract_blog_line(soup):
    upload_contents = ''
    new_posts = soup.select(".ast-row > article")
    # url_prefix_line = "https://engineering.linecorp.com/ko/blog/"

    for new_post in new_posts[:5]:

        blog_title = new_post.select('h2')[0].text
        created_date = new_post.select_one('.published').text
        url_suffix = new_post.select('a')[0].attrs['href']
        url = url_suffix

        content = f"<a href={url}>" + blog_title + "</a>" + " " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents   


def extract_blog_baemin(soup):
    upload_contents = ''
    new_posts = soup.select(".list > .list-module")
    url_prefix_baemin = "https://woowabros.github.io/"

    for new_post in new_posts[:5]:

        blog_title = new_post.select('h2')[0].text
        created_date = new_post.select('span')[0].text  
        url_suffix = new_post.select('a')[0].attrs['href']
        url = url_prefix_baemin + url_suffix

        content = f"<a href={url}>" + blog_title + "</a>" + " " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents


def extract_blog_daan(soup):
    upload_contents = ''
    new_posts = soup.select(".u-size8of12 > .postArticle")

    for new_post in new_posts[:3]:

        blog_title = new_post.select('h3')[0].text
        created_date = new_post.select('time')[0].text  
        url_suffix = new_post.select('a')[2].attrs['href'].split('?')[0]
        url = url_suffix

        content = f"<a href={url}>" + blog_title + "</a>" + " " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents


def extract_blog_toss(soup):
    upload_contents = ''
    new_posts = soup.select("#load_list > .list-card__item")

    for new_post in new_posts[:5]:

        blog_title = new_post.select('h4')[0].text
        created_date = new_post.select('.list-card__date')[0].text  
        url_suffix = new_post.select('a')[0].attrs['href']
        url = url_suffix

        content = f"<a href={url}>" + blog_title + "</a>" + " " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents


def extract_blog_spoqa(soup):
    upload_contents = ''
    new_posts = soup.select(".posts > .post-item")

    for new_post in new_posts[:5]:
        blog_title = new_post.select('.post-title-words')[0].text
        created_date = new_post.select('.post-date')[0].text  
        url_suffix = new_post.select('a')[0].attrs['href']
        url = url_suffix

        content = f"<a href={url}>" + blog_title + "</a>" + " " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents