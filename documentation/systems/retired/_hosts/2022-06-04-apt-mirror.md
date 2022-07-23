---
title: Apt Mirror
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for Apt Mirror

| PROPERTY      | VALUE                                                                           |
| ------------- | ------------------------------------------------------------------------------- |
| Name:         | Apt Mirror                                                                      |
| Host:         | [Tesseract]({% post_url /documentation/systems/servers/2022-06-04-tesseract %}) |
| Type:         | LXC Container                                                                   |
| IP:           | 192.168.12.6                                                                    |
| URL, internal | apt-mirror.vm                                                                   |
| URL, external | https://apt-mirror.drak3.io                                                     |
| configs:      | `/etc/apt/mirror.list`                                                          |
| storage:      | `/mnt/mobius/APT`                                                               |
| Purpose:      | local APT mirror                                                                |

## Other Notes:

- only apt-cache uses this directly. all other hosts just point to the cache
- [this](https://www.linuxtechi.com/setup-local-apt-repository-server-ubuntu/) is the general guide followed to create it.

Retired.