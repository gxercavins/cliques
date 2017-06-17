# Maximal Cliques
The clique problem consists in finding maximal cliques (i.e. fully connected subsets) in a given adjacency graph. For this example, developer networks are considered.

Two users are considered connected if they:
* Follow each other in Twitter
* They have a Github organization in common

The program implements the `Bron-Kerbosch` algorithm which has been demonstrated as an efficient and performant algorithm for the maximal clique problem and it is widely used in Computer Science.

## Getting Started
Input data must be provided in a text file named `users.txt` and placed in the project's root path. Each line must contain a single developer handle which has to correspond to both Twitter and GitHub usernames.

Social network data is retrieved using Tweepy and PyGithub APIs. For the former, a Twitter account with a valid phone number associated is required. The credentials can be obtained when registering a new app [here](https://apps.twitter.com/). A GitHub account is needed to connect using the PyGitHub API. Update `cliques.py` with your credentials. The project also incorporates a test file (`test.py`) to check for proper API authentication and connectivity.

Please ensure that the mandatory Python libraries, detailed in the next section, are installed.

Once everything is setup, run `cliques.py` and the results will be written to the `output.txt` file.

## Dependencies

Both APIs are needed, as well as OAuth (for authentication) and requests:
* Tweepy
* PyGitHub
* OAuth
* requests

## Troubleshooting

If a warning is raised due to insecure platform and SSL configuration problems, the `security` package needs to be installed:
```
pip install requests[security]
```
The GitHub API was found to be the most time-consuming process. For this reason, first the Twitter app is called for all users in the input list and only those with a Twitter neighbor are probed for a GitHub connection. This is done to optimize the performance of the program, however there is a more stringent data rate cap for the Twitter API. If many calls are needed in a short time frame and speed is not a problem, it could be wise to rewrite the order and mitigate this problem.

Please report any potential issues through the `Issues` tab.



