---
title: Grafana Apps
date: 2022-06-05 08:44:00 -400
categories: [docker]
tags: [docker]
---

Documentation for Grafana Apps

| PROPERTY | VALUE                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------- |
| Name:    | Grafana Apps                                                                                       |
| Type:    | App                                                                                                |
| configs: | [https://github.com/educatedCaveman/grafana_apps](https://github.com/educatedCaveman/grafana_apps) |
| Purpose: | dashboards                                                                                         |

## Networking

### PRD

| Attribute     | PRD                                                                               |
| ------------- | --------------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-sevastopol %}) |
| URL, External | N/A                                                                               |
| URL, Internal | [https://grafana.drak3.io](https://grafana.drak3.io)                              |
| IP            | `192.168.12.16`                                                                   |

### DEV

| Attribute     | DEV                                                                           |
| ------------- | ----------------------------------------------------------------------------- |
| HOST          | [Sevastopol]({% post_url /documentation/systems/virtual/2022-06-04-lv-426 %}) |
| URL, External | N/A                                                                           |
| URL, Internal | [https://grafana.dev.drak3.io](https://grafana.dev.drak3.io)                  |
| IP            | `192.168.13.16`                                                               |

## Notes:

The following services are hosted in the stack:

- Grafana
- Promtail
- Loki
