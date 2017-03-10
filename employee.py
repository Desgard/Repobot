#!/usr/bin/env python
# encoding: utf-8

class Employ:
    def __init__(self, name, commits_tot = 0, commits = []):
        self.name = name
        self.commits_tot = commits_tot

    def __init__(self, name, comments_tot = 0, comments = []) :
        self.name = name
        self.comments_tot = comments_tot
        self.comments = comments

    def add_comments_tot(self):
        self.comments_tot += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def show_issue_tot(self):
        print(self.name)
        for comment in self.comments:
            print()
            print(repr(comment['id']).ljust(15), repr(comment['related_issue_title'].ljust(30)))
            print(repr(comment['url']).ljust(20))
            print()
