---
title: Syncthing
date: 2022-06-04 15:19:00 -400
categories: [docker]
tags: [docker, syncthing]
---

Documentation for Syncthing

| PROPERTY | VALUE                                                                                        |
| -------- | -------------------------------------------------------------------------------------------- |
| Name:    | Syncthing                                                                                    |
| Type:    | App                                                                                          |
| configs: | [https://github.com/educatedCaveman/syncthing](https://github.com/educatedCaveman/syncthing) |
| Purpose: | sync files accross devices                                                                   |

## Networking

### PRD

| Attribute     | PRD                                                                               |
| ------------- | --------------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-sevastopol %}) |
| URL, External | N/A                                                                               |
| URL, Internal | [https://sync.drak3.io](https://sync.drak3.io)                                    |
| IP            | `192.168.12.20`                                                                   |

### DEV

N/A

## Notes:

also runs on Theseus and Carbon as a system service. The source folder is on mobius, which is also accessible via Nextcloud.

folders being synced:

- Documents
- ~~Music~~
- Phone pics
