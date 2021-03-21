import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    events = json.loads(
        requests.get(f'https://api.github.com/users/{username}/events').content
    )
    try:
        print(events[0]['created_at'])
    except KeyError:
        print(f'No recent events found for username "{username}"')
    


