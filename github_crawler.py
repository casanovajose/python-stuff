from bs4 import BeautifulSoup
import requests

def get_repo_data(cards):
  repositories = []
  for rep in range(len(cards)):
   repositories.append(list(cards[rep].stripped_strings))

  return repositories

# returns a ResultSet from BeautifulSoup HTML Parser
def fetch_company_repos(company):
  page = base_url + "/" + company
  result = requests.get(page)
  source = result.text
  soup = BeautifulSoup(source, "html.parser")

  # what happends if there is a paginator? should iterate over pages (TO DO)

  # other aproaches
  # repositories = soup.find_all("a", attrs={"itemprop":"name codeRepository"})
  # repo_list = soup.find_all("div", class_="repo-list")
  
  cards = soup.find_all("li", attrs={"itemprop": "owns"})
  return cards

# the main program begins
base_url = "https://github.com"
# load a bunch of pofiles you want to observe
companies = ["nayracoop"]
repositories = {}

for company in companies:
  cards =  fetch_company_repos(company)
  repositories[company] = get_repo_data(cards)