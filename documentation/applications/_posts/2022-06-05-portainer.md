---
title: Portainer
date: 2022-06-05 08:44:00 -400
categories: [docker]
tags: [docker]
---

Documentation for Portainer

| PROPERTY | VALUE                           |
| -------- | ------------------------------- |
| Name:    | Portainer                       |
| Type:    | App                             |
| configs: | N/A                             |
| Purpose: | manage docker containers/stacks |

## Networking

### PRD

| Attribute     | PRD                                                                               |
| ------------- | --------------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-sevastopol %}) |
| URL, External | N/A                                                                               |
| URL, Internal | [https://portianer.drak3.io](https://portianer.drak3.io)                          |
| URL, Internal | [http://sevastopol.vm:9000](http://sevastopol.vm:9000)                            |
| IP            | `192.168.12.16`                                                                   |

### DEV

| Attribute     | DEV                                                                           |
| ------------- | ----------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-lv-426 %}) |
| URL, External | N/A                                                                           |
| URL, Internal | [https://portianer.dev.drak3.io](https://portianer.dev.drak3.io)              |
| URL, Internal | [http://lv-426.lab:9000](http://lv-426.lab:9000)                              |
| IP            | `192.168.13.16`                                                               |

## Notes:

- URL is load balanced. **TODO**: confirm this
