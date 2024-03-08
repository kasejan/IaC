import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv('environment.env')

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPO = os.getenv('GITHUB_REPO')

GITHUB_URL = 'https://api.github.com/'

def get_projects(github_token):
    url = GITHUB_URL + 'users/{}/repos'.format(GITHUB_USERNAME)
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': github_token}
    response = requests.get(url, headers=header, verify=True)
    projects_list = response.json()
    return projects_list
# API Link
# https://api.github.com/users/USER/repos

def get_repository_tree(project_name, github_token):
    url = GITHUB_URL + 'repos/{}/{}/contents'.format(GITHUB_USERNAME,project_name)
    header = {'Accept': 'application/json', 'PRIVATE-TOKEN': github_token}
    response = requests.get(url, headers=header, verify=True)
    tree_info = response.json()
    return tree_info
# API Link
# https://api.github.com/repos/USERS/REPO/contents/PATH

project_list = get_projects(GITHUB_TOKEN)

project_exist = False

for project_item in project_list:
    print('Project Name: ' + project_item['name'] + ', Project ID: ' + str(project_item['id']))
    if project_item['name'] == GITHUB_REPO:
        print('Project ' + project_item['name'] + ' exists')
        project_exist = True
        project = project_item
        break

if not project_exist:
    print('Project ' + GITHUB_REPO + ' not found')
    logging.info('Project ' + GITHUB_REPO + ' not found')
else:
    repository_tree = get_repository_tree(GITHUB_REPO,GITHUB_TOKEN)
    for file in repository_tree:
        print(file['name'])
