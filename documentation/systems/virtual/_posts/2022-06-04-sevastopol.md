---
title: Sevastopol
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for Sevastopol

| PROPERTY | VALUE                                                                           |
| -------- | ------------------------------------------------------------------------------- |
| Name:    | Sevastopol                                                                      |
| Host:    | [Tesseract]({% post_url /documentation/systems/servers/2022-06-04-tesseract %}) |
| Type:    | Docker Swarm cluster (single node)                                              |
| IP:      | `192.168.12.20`                                                                 |
| URL      | https://portainer.drak3.io                                                      |
| Purpose: | PRD docker host                                                                 |

## Storage:

| SOURCE                     | TARGET               |
| -------------------------- | -------------------- |
| `/mnt/storage_node/Backup` | `/mnt/mobius/Backup` |

## Other Notes:

- running portainer on the manager nodes
- contains ssh keys to be managed by ansible
- services should be accessible via <service>.sevastopol.vm
