---
title: Retiring a VM/LXC host
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

This is a checklist of tasks to perform when retiring an existing VM or LXC with DHCP. This is essentially the opposite of [this]({% post_url /documentation/systems/servers/2022-06-05-create_new_host_checklist %}) document.

1. Misc.:

   - stop and delete the VM
   - remove/pause entry in uptime-kuma

2. GitHub tasks:

   - ansible:
     - retire any host-specific ansible playbooks
     - remove host from inventory (`hosts.ini`)
     - remove any other explicit mentions of the host from other playbooks not to be retired.
     - remove entry from `PW_hostname.sh`
   - Pi-Hole: remove entries from `custom.list` and `cname.conf`
   - misc: 
     - retire any dotfiles specifically for the host.
     - remove relevant entries from gatus

3. pfSense tasks:
   - remove static DHCP lease
   - remove from HAproxy
   - remove firewall rules specifically for this host
   - remove entry in all firewall aliases
