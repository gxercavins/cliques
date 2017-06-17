# Finds maximal cliques of connected developers (i.e. they follow each other in twitter and they have a github
# organization in common). Provide a text file named 'users.txt' containing the developer handles to be checked.
# Don't forget to update this file with your twitter and github credentials.

import tweepy
from clique_algorithm import bron_kerbosch
from github import Github

# minimum size for a clique to be considered
MIN_SIZE = 2

# PLEASE INPUT YOUR CREDENTIALS HERE
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
git_user = ""
git_pwd = ""

# initialize variables
users = []
graph_twitter = {}
graph = {}
friends = {}
orgs = {}
cliques = []

# Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# open file and build user list
with open("users.txt","r") as user_file:
    for line in user_file:
        users.extend([line.strip()])

# retrieve twitter friend list for each listed user
for i in enumerate(users):
    graph_twitter.setdefault(i[1], [])
    friends.setdefault(i[1], [])

    try:
        user = api.get_user(users[i[0]])

        for friend in user.friends():
            friends[i[1]].append(friend.screen_name)
    except tweepy.RateLimitError:
        print 'Twitter API data cap reached'
    except tweepy.TweepError as err:
        continue

# construct graph with Twitter relationships
for i in enumerate(users):
    for j in enumerate(users):
        if j[0] > i[0]:
            # check for reciprocity
            if j[1] in friends[i[1]] and i[1] in friends[j[1]]:
                graph_twitter[i[1]].append(j[1])
                graph_twitter[j[1]].append(i[1])

# Github authentication
g = Github(git_user, git_pwd)

# retrieve organization data for each listed user (with at least one twitter neighbor)
for i in enumerate(users):
    if graph_twitter[i[1]]:
        try:
            organizations = {organization.name for organization in g.get_user(users[i[0]]).get_orgs()}
            organizations = filter(None, organizations)
            orgs.setdefault(i[1], organizations)
        except:
            continue

# users that are connected in twitter and share at least one organization are added to the graph
for i in graph_twitter.keys():
    for j in graph_twitter[i]:
        try:
            if set(orgs[i]) & set(orgs[j]):
                try:
                    graph[i].append(j)
                except:
                    graph.setdefault(i, [])
                    graph[i].append(j)
        except:
            continue

# find cliques for the given adjacency graph
cliques = bron_kerbosch(set(), set(graph.keys()), set(), graph, [])

# filter out smaller cliques and sort users within each one alphabetically. Then, sort cliques by size
cliques = filter(lambda s: len(s) >= MIN_SIZE, cliques)
for i in enumerate(cliques):
    cliques[i[0]] = sorted(i[1])
cliques = sorted(cliques, key=len, reverse=True)

# write results in output file
out_file = open('output.txt','w')

for i in cliques:
    for j in enumerate(i):
        if j[0] > 0:
            out_file.write(' ')
        out_file.write(j[1])
    out_file.write('\n')

out_file.close()
print 'Results have been written to output.txt file successfully'
