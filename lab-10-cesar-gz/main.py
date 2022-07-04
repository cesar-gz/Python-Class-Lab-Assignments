# -*- coding: utf-8 -*-
"""
cesar gutierrez
CPSC 223P-01
Mon Apr 18, 2021
cesarg7@csu.fullerton.edu
"""


import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_names, stars = [], []

#Alternate way to delcare these variables
# repo_names = []
# stars = []

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

#for key in sorted(repo_dict.keys()):
#    print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type': 'bar',
    'x' : repo_names,
    'y' : stars,
    'marker' : {
        'color' : 'rgb(60, 100, 150)'
    }
}]

my_layout = {
    'title' : 'Most Starred Python Projects on GitHub',
    'xaxis' : {'title':'Repository'},
    'yaxis' : {'title': 'Stars'},
}

fig = {'data' : data, 'layout': my_layout}
offline.plot(fig, filename='Class Lab Assignments\lab-10-cesar-gz\python_repos.html')