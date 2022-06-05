---
title: Handbrake
date: 2022-06-05 08:44:00 -400
categories: [docker]
tags: [docker]
---

Documentation for Handbrake

| PROPERTY | VALUE                                                                                        |
| -------- | -------------------------------------------------------------------------------------------- |
| Name:    | Handbrake                                                                                    |
| Type:    | App                                                                                          |
| configs: | [https://github.com/educatedCaveman/handbrake](https://github.com/educatedCaveman/handbrake) |
| Purpose: | convert video files                                                                          |

## Networking

### PRD

| Attribute     | PRD                                                                               |
| ------------- | --------------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-sevastopol %}) |
| URL, External | N/A                                                                               |
| URL, Internal | [https://hb.drak3.io](https://hb.drak3.io)                                        |
| URL, Internal | [http://hb.sevastopol.vm:5800](http://hb.sevastopol.vm:5800)                      |
| IP            | `192.168.12.16`                                                                   |

### DEV

| Attribute     | DEV                                                                           |
| ------------- | ----------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-lv-426 %}) |
| URL, External | N/A                                                                           |
| URL, Internal | [https://hb.dev.drak3.io](https://hb.dev.drak3.io)                            |
| URL, Internal | [http://hb.lv-426.lab:5800](http://hb.lv-426.lab:5800)                        |
| IP            | `192.168.13.16`                                                               |

## Storage:

| SOURCE                                  | DESTINATION |
| --------------------------------------- | ----------- |
| `/mnt/mobius/docker/handbrake`          | `/config`   |
| `/mnt/mobius/staging/handbrake/output`  | `/output`   |
| `/mnt/mobius/staging/handbrake/storage` | `/storage`  |
| `/mnt/mobius/staging/handbrake/watch`   | `/watch`    |
