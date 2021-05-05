import os
from datetime import datetime
from pytz import timezone
from crawling_tech_blog import parsing_beautifulsoup, extract_blog_kakao
from github_utils import get_github_repo, upload_github_issue

if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    access_token = 'nakalicoubae4all!'
    repository_name = "tech-blog-crawling"

    seoul_timezone = timezone('Asia/Seoul')

    today = datetime.now(seoul_timezone)
    today_data = today.strftime("%Y년 %m월 %d일")

    # naver_blog_url = "https://d2.naver.com/home"
    kakao_blog_url = "https://tech.kakao.com/blog/"
    # line_blog_url = "https://engineering.linecorp.com/ko/blog/"

    # soup = parsing_beautifulsoup(naver_blog_url)
    soup = parsing_beautifulsoup(kakao_blog_url)
    # soup = parsing_beautifulsoup(line_blog_url)
    
    issue_title = f"네카라쿠배 기술블로그 새글알림({today_data}"
    # upload_contents = extract_blog_naver(soup)
    upload_contents = extract_blog_kakao(soup)

    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success")
