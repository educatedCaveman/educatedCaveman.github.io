---
title: Remote Access VPN
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

in order to have devices use a remote VPN, the following must be satisfied:

- the openvpn client config has been exported from pfSense, and placed on the client
- the client must have the `openvpn-update-resolv-conf-git` package as described [here](https://wiki.archlinux.org/index.php/OpenVPN#The_update-resolv-conf_custom_script)
- verify the client config has the following options, which should have been set by the server:

    ```conf
    script-security 2
    up /etc/openvpn/update-resolv-conf
    down /etc/openvpn/update-resolv-conf
    ```
