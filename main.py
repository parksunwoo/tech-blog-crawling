import os
from datetime import datetime
from pytz import timezone
from crawling_tech_blog import parsing_feedparse
from crawling_tech_blog import parsing_beautifulsoup, \
                               extract_blog_naver, extract_blog_kakao, extract_blog_line, extract_blog_baemin, extract_blog_toss, \
                               extract_blog_spoqa
                               
from github_utils import get_github_repo, upload_github_issue

if __name__ == "__main__":
    # access_token = os.environ['MY_GITHUB_TOKEN']
    access_token = "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"
    repository_name = "tech-blog-crawling"

    seoul_timezone = timezone('Asia/Seoul')

    today = datetime.now(seoul_timezone)
    today_data = today.strftime("%Y년 %m월 %d일")

    blog_url_naver = "https://d2.naver.com/d2.atom"
    blog_url_kakao = "https://tech.kakao.com/blog/"
    blog_url_line = "https://engineering.linecorp.com/ko/blog/"
    blog_url_baemin = "https://woowabros.github.io/"
    blog_url_toss = "https://blog.toss.im/category/allabouttoss/tossteam/1"
    blog_url_spoqa = "https://spoqa.github.io/"

    feed_naver = parsing_feedparse(blog_url_naver)
    # soup_kakao = parsing_beautifulsoup(blog_url_kakao)
    # soup_line = parsing_beautifulsoup(blog_url_line)
    # soup_baemin = parsing_beautifulsoup(blog_url_baemin)
    # soup_toss = parsing_beautifulsoup(blog_url_toss)
    # soup_spoqa = parsing_beautifulsoup(blog_url_spoqa)
    
    issue_title = f"네카라쿠배 기술블로그 새글알림({today_data})"
    upload_contents = ''
    upload_contents += f'### 네이버 <br/>\n'
    upload_contents += extract_blog_naver(feed_naver)
    # upload_contents += f"### 카카오 <br/>\n"
    # upload_contents += extract_blog_kakao(soup_kakao)
    # upload_contents += f"### 라인 <br/>\n"
    # upload_contents += extract_blog_line(soup_line)
    # upload_contents += f"### 배달의민족 <br/>\n"
    # upload_contents += extract_blog_baemin(soup_baemin)
    # upload_contents += f"### 토스 <br/>\n"
    # upload_contents += extract_blog_toss(soup_toss)
    
    # upload_contents += f"### 스포카 <br/>\n"
    # upload_contents += extract_blog_spoqa(soup_spoqa)               
    
    # repo = get_github_repo(access_token, repository_name)
    # upload_github_issue(repo, issue_title, upload_contents)
    # print("Upload Github Issue Success")
    
