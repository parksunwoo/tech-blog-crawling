import os
from datetime import datetime
from pytz import timezone
from crawling_tech_blog import parsing_beautifulsoup, extract_blog_naver, extract_blog_kakao, extract_blog_line, extract_blog_baemin
from github_utils import get_github_repo, upload_github_issue

if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "tech-blog-crawling"

    seoul_timezone = timezone('Asia/Seoul')

    today = datetime.now(seoul_timezone)
    today_data = today.strftime("%Y년 %m월 %d일")

    # naver_blog_url = "https://d2.naver.com/home"
    blog_url_kakao = "https://tech.kakao.com/blog/"
    blog_url_line = "https://engineering.linecorp.com/ko/blog/"
    blog_url_baemin = "https://woowabros.github.io/"

    # soup = parsing_beautifulsoup(naver_blog_url)
    soup_kakao = parsing_beautifulsoup(blog_url_kakao)
    soup_line = parsing_beautifulsoup(blog_url_line)
    soup_baemin = parsing_beautifulsoup(blog_url_baemin)

    
    issue_title = f"네카라쿠배 기술블로그 새글알림({today_data})"
    upload_contents = ''
    # upload_contents = extract_blog_naver(soup)
    upload_contents += extract_blog_kakao(soup_kakao)
    upload_contents += extract_blog_line(soup_line)
    upload_contents += extract_blog_baemin(soup_baemin)

    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success")
