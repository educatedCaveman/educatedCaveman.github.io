---
title: Central_Plexus
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for Central_Plexus

| PROPERTY   | VALUE                                                                  |
| ---------- | ---------------------------------------------------------------------- |
| Name:      | Central_Plexus                                                         |
| Model:     | Supermicro X10SLM-F                                                    |
| Serial:    | S15586614313687                                                        |
| Location:  | [RU_24]({% post_url /documentation/systems/servers/2022-06-04-rack %}) |
| IP:        | `192.168.*.1`, `10.13.*.1`                                             |
| URL:       | https://pfsense.drak3.io/                                              |
| local DNS: | router.\*                                                              |
| Purpose:   | Router                                                                 |

## Hardware:

- 2x10Gb/s SFP+ NIC
- E3 1240v3 (3.4GHz)
- 8GB ECC memory
- 120GB SSD

## Pictures:

### Front:

![kvm, router, 10g switch](/assets/rack_01_route.jpg)

### Rear:

![router rear](/assets/central_plexus_back_01.jpg)

![router rear](/assets/central_plexus_back_02.jpg)

## Other Notes:

### VLANs

Note: all the individual VLANs are untagged until they get to the switches, with the exception of Mobius' secondary connection.

| VLAN            | Abbreviation | Network            | VLAN Tag | Use                                                |
| --------------- | ------------ | ------------------ | -------- | -------------------------------------------------- |
| Management      | MGMT_VLAN    | `192.168.1.0/24`   | (native) | network admin devices                              |
| LAN             | LAN_VLAN     | `192.168.10.0/24`  | 10       | main LAN                                           |
| Server          | MGMT_VLAN    | `192.168.11.0/24`  | 11       | physical servers                                   |
| Virtual Machine | VM_VLAN      | `192.168.12.0/24`  | 12       | virtual machines and jails                         |
| Lab             | LAB_VLAN     | `192.168.13.0/24`  | 13       | virtual machines and jails undergoing testing      |
| Guest / IoT     | IOT_VLAN     | `192.168.20.0/24`  | 20       | all Internet of Things devices, and work computers |
| CAM             | CAM_VLAN     | `192.168.200.0/30` | 200      | Security Cameras                                   |
