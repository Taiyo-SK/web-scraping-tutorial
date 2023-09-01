# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/#step-3-parse-html-code-with-beautiful-soup

import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Find the ID of the HTML element containing all the job postings
results = soup.find(id='ResultsContainer')
# print(results.prettify())

# Get the job postings from results
job_elements = results.find_all('div', class_='card-content')

# But since we're Python devs, get the job postings for Python roles
python_jobs = results.find_all(
    'h2', string=lambda text:'python' in text.lower()
    )

# Get the job title, company, and location from each Python posting
# But to do so, we need to grab the parent element that contains 
# the title, company, and location
# (the python_jobs object only contains the title)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job in python_job_elements:
    title_element = job.find('h2', class_='title')
    company_element = job.find('h3', class_='company')
    location_element = job.find('p', class_='location')
    # Use element.text to return only the text content of each HTML ele,
        # rather than the whole element
    # Strip out extra whitespace (I also made the title ALL CAPS for readability)
    link_url = job.find_all('a')[1]['href']
    print(f"""Apply here: {link_url} \n""")
    print(title_element.text.strip().upper())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

