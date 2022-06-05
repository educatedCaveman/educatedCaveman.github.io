---
title: Create New Git Repo
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

This is a checklist of tasks to perform when creating a new GitHub repository.

The order of these tasks is not super important, but it mostly makes sense to do them in this order.

1. Create the new Repo in GitHub
   - check the README.md box
2. Add a jenkins webhook in the repo
   - located under settings/webhooks
   - payload url: `https://jenkins.drak3.io/github-webhook/`
   - content type: `application/json`
   - enable SSL: checked
   - event: just the push event
3. Add the following template files
   - `Jenkinsfile`
   - `git-save.sh`
4. Edit the Jenkinsfile as needed
5. Create/update any ansible playbooks required.
6. Ad the repository path to the `/etc/gitconfig` file on all VMs
7. Add the repository to jenkins
   - Multibranch pipeline
   - GitHub source/check, using the github credentials
8. Add the repo to any relevant view.
