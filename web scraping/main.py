from bs4 import BeautifulSoup
import requests
import time

print("put some skill you are not familiar")
unfamiliar_skills = input(": ")
print('Filtering out...')
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        job_post_time = job.find('span', class_='sim-posted').span.text
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']
        if unfamiliar_skills not in skills:
            with open(f'post/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name} \n")
                f.write(f"Required Skills: {skills} \n")
                f.write(f"More Info: {more_info}")
            print(f"File saved: {index}")

if __name__ == "__main__":
    while True:
        find_jobs()
        usr_chs = int(input('1.Exit\n2.Continue\n (1,2): '))
        if usr_chs == 1:
            print("GoodBye :)")
            break
        elif usr_chs == 2:
            time_wait = 30
            print(f"Wating for {time_wait} Seconds.........")
            time.sleep(time_wait)
        else:
            print("Something went wrong :(")
            break
