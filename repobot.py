#!/usr/bin/env python
# encoding: utf-8

from github import Github

g = Github("desgard-duan", "dhy94113")

for repo in g.get_user().get_repos():
    print(repo.name)
