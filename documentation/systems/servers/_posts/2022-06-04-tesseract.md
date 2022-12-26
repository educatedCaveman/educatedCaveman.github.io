---
title: Tesseract
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for Tesseract

| PROPERTY     | VALUE                                                               |
| ------------ | ------------------------------------------------------------------- |
| Name:        | Tesseract                                                           |
| Model:       | Dell R720                                                           |
| Service Tag: | 49PJYC1                                                             |
| Serial:      | 9294218569                                                          |
| Location:    | [RU_15]({% post_url /documentation/systems/misc/2022-06-04-rack %}) |
| IP:          | `192.168.11.3`, `192.168.1.8`                                       |
| local DNS:   | tesseract.srv, tesseract.mgmt                                       |
| Purpose:     | Virtualization Server (Proxmox)                                     |

## URLs

- https://tesseract.drak3.io/
- https://ipmi.tesseract.drak3.io/

## Hardware

- 2x Xeon E2690 @3.00 GHz (40-cores)
- 256GB memory

## Drives

### Layout

| DRIVE # | MFTR     | CAPACITY | MODEL #         | SERIAL #          | POOL         |
| ------- | -------- | -------- | --------------- | ----------------- | ------------ |
| b0      | Kingston | 240GB    | SA400S37240G    | 50026B76831671B4  | rpool (boot) |
| b1      | Kingston | 240GB    | SA400S37240G    | 50026B76831675C7  | rpool (boot) |
| f0      | SK Hynix | 1000GB   | SHGS31-1000GS-2 | FJ07N44241110782E | tank         |
| f1      | SK Hynix | 1000GB   | SHGS31-1000GS-2 | FJ07N442411107810 | tank         |
| f2      | SK Hynix | 1000GB   | SHGS31-1000GS-2 | FSA4N84211100554W | tank         |
| f3      | SK Hynix | 1000GB   | SHGS31-1000GS-2 | FDA5N443712005C1H | tank         |
| f4      | Samsung  | 1000GB   | MZ-76E1T0       | S599NZ0NB19643N   | tank         |
| f5      | Samsung  | 1000GB   | MZ-76E1T0       | S599NZ0NB19644Y   | tank         |
| f6      | Samsung  | 1000GB   | MZ-76E1T0       | S599NZ0NB27224H   | tank         |
| f7      | Samsung  | 1000GB   | MZ-76E1T0       | S599NZ0NB27466B   | tank         |
| pcie0.1 | SK Hynix | 500GB    | SHGP31-500GM-2  | FSACN54831050CC5L | nvme_pool    |
| pcie1.1 | SK Hynix | 500GB    | SHGP31-500GM-2  | FSACN54831100CC40 | nvme_pool    |
| pcie2.1 | SK Hynix | 500GB    | SHGP31-500GM-2  | FSACN54831050CC5I | nvme_pool    |
| pcie0.2 | SK Hynix | 500GB    | SHGP31-500GM-2  | FSACN54831100CC46 | nvme_pool    |
| pcie1.2 | SK Hynix | 500GB    | SHGP31-500GM-2  | FSACN54831100CC4O | nvme_pool    |
| pcie2.2 | SK Hynix | 500GB    | SHGP31-500GM-2  | FSACN54831CA4CF0D | nvme_pool    |

#### Other Notes

**2021-12-22: added boot priorities**

- tier 1: (boot order = 10; boot delay = 10)
  - pihole
- tier 2: (boot order = 20; boot delay = 10)
  - jenkins
  - syncthing
- tier 3: (boot order = 30)
  - lv-426
  - nextcloud
  - plex
  - seedbox
  - sevastopol
  - home-assistant

## Pictures

### Front

![switches, PoE, and shelf](/assets/rack_03_server.jpg)

### Rear

![tesseract rear](/assets/tesseract_rear.jpg)
