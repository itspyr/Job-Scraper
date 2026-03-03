import requests
from bs4 import BeautifulSoup


def scrape():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_jobs = soup.find_all('h2')
    companyName = soup.find_all('h3', class_='subtitle is-6 company')
    location = soup.find_all('p', class_='location')
    applyBtn = soup.find_all('a', class_='card-footer-item')
    return all_jobs, location, applyBtn, companyName


def divider():
    print("\n" + "=" * 50)


def header(title):
    divider()
    print(f"  {title}")
    divider()


def jobsFun(all_jobs):
    header("OPEN POSITIONS")
    for i, job in enumerate(all_jobs, start=1):
        print(f"  {i}. {job.get_text()}")
    divider()


def companies(companyName):
    header("COMPANIES HIRING")
    for j, comp in enumerate(companyName, start=1):
        print(f"  {j}. {comp.get_text().strip()}")
    divider()


def locationFun(location):
    header("JOB LOCATIONS")
    for i, spot in enumerate(location, start=1):
        print(f"  {i}. {spot.get_text().strip()}")
    divider()


def displayAll(all_jobs, location, companyName):
    header("ALL JOB LISTINGS")
    for i, (job, spot, comp) in enumerate(zip(all_jobs, location, companyName), start=1):
        print(f"  [{i}] {job.get_text()}")
        print(f"       Company  : {comp.get_text().strip()}")
        print(f"       Location : {spot.get_text().strip()}")
        print()
    divider()


def jobApp(applyBtn):
    try:
        userApply = int(input("  Enter job # to apply --> "))
        applyIndex = (userApply * 2) - 1
        link = applyBtn[applyIndex].get('href')
        divider()
        print(f"\n  Apply here: {link}\n")
        divider()
    except (ValueError, IndexError):
        print("\n  Invalid selection. Please try again.")


def menu():
    print("\n" + "=" * 50)
    print("           JOB SEARCH CONSOLE")
    print("=" * 50)
    print("  1. Browse & Apply to Jobs")
    print("  2. View Locations")
    print("  3. View Open Positions")
    print("  4. View Companies")
    print("  5. Quit")
    print("=" * 50)


if __name__ == '__main__':
    all_jobs, location, applyBtn, companyName = scrape()
    print("\n  Loading jobs...")

    while True:
        menu()
        choice = input("\n  Enter your choice --> ").strip()

        if choice == "5":
            print("\n  Goodbye!\n")
            break
        elif choice == "3":
            jobsFun(all_jobs)
        elif choice == "2":
            locationFun(location)
        elif choice == "1":
            displayAll(all_jobs, location, companyName)
            jobApp(applyBtn)
        elif choice == "4":
            companies(companyName)
        else:
            print("\n  Invalid choice. Please enter 1-5.")