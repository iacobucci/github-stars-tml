import requests
import argparse

parser = argparse.ArgumentParser(description='list starred repos in vml')
parser.add_argument('-t', '--token', required=True, help='GitHub personal access token')
parser.add_argument('-u', '--username', required=True, help='GitHub username')
args = parser.parse_args()

token = args.token
username = args.username
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}


def export_starred_repos():
    repos = []
    url = f'https://api.github.com/users/{username}/starred'
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            r = response.json()
            for repo in r:
                repos.append(repo['full_name'])
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                break
        else:
            print("failed to fetch starred repositories")
            break

    repos = sorted(repos)
    for repo in repos:
        print(repo)

if __name__ == '__main__':
    export_starred_repos()
