# three simple tests to check algorithm, twitter api and github api functionality

from data import *
from clique_algorithm import bron_kerbosch
import unittest
import tweepy
from github import Github

cliques = []

# PLEASE INPUT YOUR CREDENTIALS HERE
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
git_user = ""
git_pwd = ""

class TestStringMethods(unittest.TestCase):

    # test the algorithm itself with seed input data
    def test_algorithm(self):
        print 'ALGORITHM TEST'
        print '------------------------'
        print 'Input data: ' + str(graph)

        cliques = bron_kerbosch(set(), set(graph.keys()), set(), graph, [])
        cliques = filter(lambda s:len(s) >= 2, cliques)
        for i in enumerate(cliques):
            cliques[i[0]] = sorted(i[1])
        cliques = sorted(cliques, key=len, reverse=True)

        print 'Expected result: [[\'Arya\', \'Ed\', \'John\', \'Robb\', \'Sansa\'], [\'Cersei\', \'Jaime\', \'Tyrion\']]'

        self.assertEqual(cliques, [['Arya', 'Ed', 'John', 'Robb', 'Sansa'], ['Cersei', 'Jaime', 'Tyrion']])

    # test twitter api authentication and data retrieval
    def test_tweepy(self):
        print 'TWEEPY API TEST'
        print '------------------------'
        print 'Finding user \'Twitter\''

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        user = api.get_user(783214)

        self.assertEqual(user.screen_name, u'Twitter')

    # test pygithub api authentication and data retrieval
    def test_pygithub(self):
        print 'PyGitHub API TEST'
        print '------------------------'
        print 'Finding user \'github\''

        g = Github(git_user, git_pwd)

        user_id = g.get_user('github').id

        self.assertEqual(user_id, 9919)

if __name__ == '__main__':
    unittest.main()