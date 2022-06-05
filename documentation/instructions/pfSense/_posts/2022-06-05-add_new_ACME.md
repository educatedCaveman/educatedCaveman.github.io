---
title: Adding a New ACME cert
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

The following was mostly taken from [here](https://crepaldi.us/2020/06/25/issuing-lets-encrypt-certificates-on-your-pfsense-using-acme/)

## Initial Setup

1.  Obtain your Cloudflare keys. Currently, these are stored in LastPass. We'll need the following:
    - Zone ID
    - Account ID
    - Global API Key
    - API Token
    - email address: j.drake.hoffman@gmail.com
2.  Add a DNS record:
    - Type: CAA
    - Name: @
    - Tag: "Only Allow Specific Hostnames"
    - CA Domain Name: letsencrypt.org

## ACME in pfSense

It is easier to copy an existing cert, and modify

1.  Add new cert
2.  Give it a meaningful name and description
3.  Use the testing or PRD acme account, as appropriate
4.  Under Domain SAN list:
    1.  Enter the full domain name
    2.  Use the DNS-Cloudflare method
    3.  Fill in the keys
5.  Under Actions, addthe following 2 actions:
    1.  webgui:
        - Mode: Enabled
        - Command: `/etc/rc.restart_webgui`
        - Method: Shell Command
    1.  haproxy:
        - Mode: Enabled
        - Command: `/usr/local/etc/rc.d/haproxy.sh`
        - Method: Shell Command
6.  Save
7.  Click Issue/Renew
