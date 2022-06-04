---
title: NextCloud
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for NextCloud

| PROPERTY       | VALUE                                                                           |
| -------------- | ------------------------------------------------------------------------------- |
| Name:          | NextCloud                                                                       |
| Host:          | [Tesseract]({% post_url /documentation/systems/servers/2022-06-04-tesseract %}) |
| Type:          | VM                                                                              |
| IP:            | 192.168.12.10                                                                   |
| URL, internal: | nextcloud.vm                                                                    |
| URL, external: | https://cloud.drak3.io/index.php/login                                          |
| configs:       | N/A                                                                             |
| Purpose:       | cloud document access                                                           |

## Storage

- `/mnt/storage_node/Documents/`
- `/mnt/storage_node/Pictures/`

## Other Notes

- can only be accessed by the external URL
- configs are only located on the host

## New VM notes:

- in order for the NFS mountpoints to work, they have to to be mounted inside NextCloud's default data directory
  - this might be specific to SNAP installs
  - the directory is `/var/snap/nextcloud/common/nextcloud/data/`
