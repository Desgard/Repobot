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

    def write_2_md(self):
        file_name = self.name + '-commit-list.md'
        f = open(file_name, "w")
        print("#", self.name, "的 commit 周报\n", file = f)
        print("##", self.name, "在本周共有", self.commits_tot, "次 commits \n", file = f)
        index = 1
        for commit in self.commits:
            print("%d. [%s](%s) - %s \n" % (index, commit['message'], commit['url'], commit['time']), file = f)
            index += 1
        print("---", file = f)

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

    def write_2_md(self):
        file_name = self.name + '-issue-list.md'
        f = open(file_name, "w")
        print("#", self.name, "的 issue 周报\n", file = f)
        print("##", self.name, "在本周共参与", self.comments_tot, "个 issue \n", file = f)
        for comment in self.comments:
            print("Update: **%s**\nStatus: **%s** \n" % (comment['update'], comment['status']), file = f)
            print("* %s - [%s](%s)\n" % (comment['id'], comment['related_issue_title'], comment['url']), file = f)
        print('---', file = f)
