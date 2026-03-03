import requests
from bs4 import BeautifulSoup


def scrape():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_jobs = soup.find_all('h2')
    companyName = soup.find_all('h3', class_ = 'subtitle is-6 company')
    location = soup.find_all('p', class_ = 'location')
    applyBtn = soup.find_all('a', class_ = 'card-footer-item')
    return all_jobs, location, applyBtn, companyName


def jobsFun(all_jobs):
    for i, job in enumerate(all_jobs, start=1):
        print(f"{i}. {job.get_text()}")

def companies(companyName):
    for j, comp in enumerate(companyName, start=1):
        print(f"{j}) {comp.get_text().strip()}")

def locationFun(location):
    for spot in location:
        print(spot.get_text().strip())

def display(all_jobs, location):
    for i, (job, spot) in enumerate(zip(all_jobs, location), start=1):
        print(f"{i}. {job.get_text()} in {spot.get_text().strip()}")

def displayAll(all_jobs, location, companyName):
    for i, (job, spot, comp) in enumerate(zip(all_jobs, location, companyName), start=1):
        print(f"{i}. {job.get_text()} in {spot.get_text().strip()} by {comp.get_text()}")

def jobApp(applyBtn):
    userApply = int(input("What is the # of the job you'd like to apply for: "))
    userApply -= 0
    applyIndex = (userApply * 2) - 1
    print(applyBtn[applyIndex].get('href'))


if __name__ == '__main__':
    all_jobs, location, applyBtn, companyName = scrape()
    while True:
        choice = input("\n --------------------------- "
                       "\n What would you like to do?"
                       "\n 1) Apply to jobs"
                       "\n 2) Locations we offer"
                       "\n 3) Open Positions"
                       "\n 4) Companies"
                       "\n 5) Quit"
                       "\n Enter # to select  ----> "
                       "\n --------------------------- ")

        if choice == "5":
            break
        elif choice == "3":
            jobsFun(all_jobs)
        elif choice == '2':
            locationFun(location)
        elif choice == '1':
            displayAll(all_jobs, location, companyName)
            jobApp(applyBtn)
        elif choice == '4':
            companies(companyName)
        else:
            print("Please enter a valid choice")

