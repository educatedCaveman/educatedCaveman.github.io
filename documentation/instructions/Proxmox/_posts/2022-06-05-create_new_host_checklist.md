---
title: Creating a New DHCP VM/LXC host
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

This is a checklist of tasks to perform when creating a new VM or LXC with DHCP. The order of these tasks is not super important, but it mostly makes sense to do them in this order.

1. Proxmox tasks:

   - clone or create VM from template in proxmox, noting the MAC address assigned
   - attach the appropriate bridge for the application.
   - add the boot order and boot delay appropriate for the application and add it to the list [here]({% post_url /documentation/systems/servers/2022-06-04-tesseract %}) (also explains the tiers).

2. pfSense tasks:

   - in pfSense, add a static lease to the appropriate DHCP server using the MAC address noted earlier.
   - if you anticipate using a ssl hostname, it would be convenient to do so now: [instructions]({% post_url /documentation/systems/servers/2022-06-05-add_new_haproxy %})
   - add the IP to the appropriate firewall aliases. most likely this will be one or more of `VM_REQUIRE_NFS`, `ssh_servers`, or `web_servers`. it may also be appropriate to create a new alias for it (including a port alias.

3. GitHub tasks:

   - add the local hostname and ip to be used in the Pi-Hole `custom.list` file.
   - if ssl is to be used, add an entry to Pi-Hole's `cname.conf` file.
   - if ansible is to be used, configure the relevant playbooks, and add the host to the `hosts.ini` file. Don't forget the `/maintenance/PW_hostname.sh` script. it contains an array of hostnames.
   - add a Bitwarden entry to `Homelab/ansible/`. copy an existing one, and update as appropriate.
   - create any extra dotfiles needed, such as the specific tmuxp config file.

4. start the VM/LXC
   - run ansible playbook. you may have to wait for the automatic updates to complete first.
   - run the `/maintenance/PW_hostname.sh` script, which will set the hostname, and password for the drake and root users.
   - add an entry to uptime-kuma, if desired.
