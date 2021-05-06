import requests
from bs4 import BeautifulSoup


def parsing_beautifulsoup(url):
    data = requests.get(url)

    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_blog_naver(soup):

    upload_contents = ''
    new_posts = soup.select(".pc > .post_article")
    url_prefix_naver = "https://d2.naver.com/home"

    for new_post in new_posts:
        blog_title = new_post.select("a")[0].text
        url_suffix = new_post.select("a")[1].attrs['href']        
        created_date = new_post.select("dd")[0].text
        url = url_prefix_naver + url_suffix

        content = f"<a href={url}" + blog_title + "</a>" + ", " + created_date + "<br/>\n"
        upload_contents += content

    return upload_contents

def extract_blog_kakao(soup):
    upload_contents = ''
    new_posts = soup.select(".list_post > li")
    url_prefix_kakao = ""

    for new_post in new_posts:

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

    for new_post in new_posts:

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