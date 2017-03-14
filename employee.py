#!/usr/bin/env python
# encoding: utf-8

class EmployCommit:
    def __init__(self, name, commits_tot = 0, commits = []):
        self.name = name
        self.commits_tot = commits_tot
        self.commits = commits

    def add_commits_tot(self):
        self.commits_tot += 1

    def add_commit(self, commit):
        self.commits.append(commit)

    def show_commit_tot(self):
        print("\t", self.name)
        for commit in self.commits:
            print()
            print(repr(commit['sha']).ljust(20), repr(commit['time']).ljust(30))
            print(repr(commit['url']).ljust(20))
            print()

class EmployIssue:
    def __init__(self, name, comments_tot = 0, comments = []) :
        self.name = name
        self.comments_tot = comments_tot
        self.comments = comments

    def add_comments_tot(self):
        self.comments_tot += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def show_issue_tot(self):
        print("\t", self.name)
        for comment in self.comments:
            print()
            print(repr(comment['id']).ljust(15), repr(comment['related_issue_title'].ljust(30)))
            print(repr(comment['url']).ljust(20))
            print()
