---
title: Containers
date: 2022-06-05 08:44:00 -400
categories: [docker]
tags: [docker]
---

## Create New or Update Existing

 1. start in the dev_test branch.
 2. make make the initial changes/commits to that branch
 3. repeat 2 as necessary
 4. create the urls (at any time prior to promoting to PRD):
    - internal DNS:
        - `<thing>.sevastopol.vm`
        - `<thing>.lv-426.lab`
    - external DNS (using ACME and HAproxy):
        - `https://<thing>.drak3.io`
        - `https://<thing>.dev.drak3.io`
 5. merge dev branch into PRD