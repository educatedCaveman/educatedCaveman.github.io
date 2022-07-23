---
title: Privateer
date: 2022-07-23 10:44:00 -400
categories: [docker]
tags: [docker, radarr, sonarr, lidarr, prowlarr, bazarr]
---

Documentation for Grafana Apps

| PROPERTY | VALUE                                                                                        |
| -------- | -------------------------------------------------------------------------------------------- |
| Name:    | \*Arrs                                                                                       |
| Type:    | App                                                                                          |
| configs: | [https://github.com/educatedCaveman/privateer](https://github.com/educatedCaveman/privateer) |
| Purpose: | automate downloads                                                                           |

## Networking

### PRD

| Attribute     | PRD                                                                               |
| ------------- | --------------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-sevastopol %}) |
| URL, External | N/A                                                                               |
| URL, Internal | [https://prowlarr.drak3.io](https://prowlarr.drak3.io)                            |
| URL, Internal | [https://bazarr.drak3.io](https://prowlarr.drak3.io)                              |
| URL, Internal | [https://radarr.drak3.io](https://prowlarr.drak3.io)                              |
| URL, Internal | [https://sonarr.drak3.io](https://prowlarr.drak3.io)                              |
| URL, Internal | [https://lidarr.drak3.io](https://prowlarr.drak3.io)                              |
| IP            | `192.168.12.20`                                                                   |

### DEV

| Attribute     | DEV                                                                           |
| ------------- | ----------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-lv-426 %}) |
| URL, External | N/A                                                                           |
| URL, Prowlarr | [http://lv-426:9696](http://lv-426:9696)                                      |
| URL, Bazarr   | [http://lv-426:6767](http://lv-426:6767)                                      |
| URL, Radarr   | [http://lv-426:7878](http://lv-426:7878)                                      |
| URL, Sonarr   | [http://lv-426:8989](http://lv-426:8989)                                      |
| URL, Lidarr   | [http://lv-426:8686](http://lv-426:8686)                                      |
| IP            | `192.168.13.20`                                                               |

## Notes:


