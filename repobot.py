#!/usr/bin/env python
# encoding: utf-8

from github import Github
from employee import EmployCommit
from employee import EmployIssue
import datetime

input_username = input("Github username: ")
input_password = input("password: ")
github_obj = Github(input_username, input_password)

while True:
    print("You can input these command to get useful message: \n")
    print(repr("contribution").ljust(15), "- Get all authors' commits")
    print(repr("issue").ljust(15), "- Get all people's issues")
    print(repr("exit").ljust(15), "- Quit repobot\n")
    func_command = input()
    if func_command == "contribution":
        contributions = {}
        repo_name = input("repo: ")
        repo_obj = github_obj.get_user().get_repo(repo_name)
        print('In', repo_obj.name, ', we need to choose a branch: ')
        branch_name = input("branch: ")
        commites = repo_obj.get_commits(sha = branch_name, since = datetime.datetime.now() - datetime.timedelta(days = 7), until = datetime.datetime.now())
        for commit in commites:
            author_name = commit.author.name
            commit_dic = {
                "author":   commit.author.name,
                "sha":      commit.sha,
                "time":     commit.last_modified,
                "url":      commit.html_url,
                "message":  commit.commit.message,
            }

            if author_name in contributions:
                contributions[author_name].add_commits_tot()
                contributions[author_name].add_commit(commit_dic)
            else:
                contributions[author_name] = EmployCommit(name = author_name, commits_tot = 1, commits = [commit_dic])

        for key in contributions:
            contributions[key].show_commit_tot()
            contributions[key].write_2_md()
        print("\n")

    elif func_command == "issue":
        repo_name = input("repo: ")
        repo_obj = github_obj.get_user().get_repo(repo_name)
        issues = repo_obj.get_issues(assignee = "*", since = datetime.datetime.now() - datetime.timedelta(days = 7))
        issue_contributions = {}
        for issue in issues:
            if issue.comments != 0:
                comments = issue.get_comments()
                for comment in comments:
                    name = comment.user.name

                    comment_dic = {
                        "id":       comment.id,
                        "body":     comment.body,
                        "url":      comment.html_url,
                        "update":   comment.updated_at,
                        "related_issue_title":  issue.title,
                        "related_issue_body":   issue.body,
                        "related_issue_id":     issue.id,
                        "realted_issue_url":    issue.html_url,
                    }

                    if name in issue_contributions:
                        issue_contributions[name].add_comments_tot()
                        issue_contributions[name].add_comment(comment_dic)
                    else:
                        issue_contributions[name] = EmployIssue(name = name, comments_tot = 1, comments = [comment_dic])

        for key in issue_contributions:
            issue_contributions[key].show_issue_tot()
            issue_contributions[key].write_2_md()

    elif func_command == "exit" :
        break

    print("*" * 60)

