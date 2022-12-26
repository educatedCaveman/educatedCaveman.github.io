---
title: Event Horizon
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for Event Horizon

| PROPERTY   | VALUE                                                               |
| ---------- | ------------------------------------------------------------------- |
| Name:      | Event Horizon                                                       |
| Model:     | Raspberry Pi 3B                                                     |
| Serial:    | 000000009cfa8f93                                                    |
| Location:  | [RU_16]({% post_url /documentation/systems/misc/2022-06-04-rack %}) |
| IP:        | `192.168.11.4`                                                      |
| local DNS: | event-horizon.srv                                                   |
| URL:       | https://pihole2.drak3.io/admin/index.php                            |
| Purpose:   | Run Pi-hole                                                         |

## Crontab

```shell
*/15 * * * * /bin/bash /home/drake/gravity-sync/gravity-sync.sh smart > /home/drake/gravity-sync/gravity-sync.cron
0 2 * * * /bin/bash /home/drake/gravity-sync/gravity-sync.sh backup >/dev/null 2>&1
```

## Picture:

![switches, PoE, and shelf](/assets/rack_05_shelf_back.jpg)
