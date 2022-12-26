---
title: Dilithium
date: 2022-12-26 11:46:00 -500
categories: []
tags: []
---

Documentation for Dilithium

| PROPERTY   | VALUE                                                               |
| ---------- | ------------------------------------------------------------------- |
| Name:      | Dilithium                                                           |
| Model:     | Raspberry Pi 3B                                                     |
| Serial:    | 00000000da566d61                                                    |
| Location:  | [RU_16]({% post_url /documentation/systems/misc/2022-06-04-rack %}) |
| IP:        | `192.168.11.6`                                                      |
| local DNS: | dilithium.srv                                                       |
| Purpose:   | non-virtual backup                                                  |

The general purpose is to act as a place to put repositories and such in the event that tesseract/jenkins is down, and needs reconfiguring.

It also control's the R720's fan speed.

It now also hosts a Gatus docker container, and an associated portainer instance.

## Crontab

handled by ansible

```shell
* * * * * /bin/bash /home/drake/scripts/cron/r720_fan_control.sh
```

## Picture:

![switches, PoE, and shelf](/assets/rack_05_shelf_back.jpg)
