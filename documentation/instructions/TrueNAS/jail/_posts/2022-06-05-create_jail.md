---
title: Creating Jail
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

Most jails are created from a [Plugin](https://www.truenas.com/docs/hub/tasks/advanced/plugins/).

## Creation

When creating a jail, there are a few considerations:

1.  before attempting to install a jail, especially from a plugin, first enable the SERVER_VLAN firewall rule for jail installs.
2.  When configuring the jail, leave all networking as-is, but check the DHCP checkbox.
3.  Proceed with the install, [as per the docs](https://www.truenas.com/docs/hub/tasks/advanced/jails/).
4.  If the jail is a plugin jail, perform the initial configuration. Especially perform any login or initial setup.
5.  Shutdown the jail
6.  Assign a static IP in the DHCP server on the appropriate VLAN.
7.  Remove the initial DHCP lease.
8.  Disable the SERVER_VLAN firewall rule for jail installs.
9.  Edit the Jail's networking to attach it to the appropriate bridge for the [desired VLAN]({% post_url /documentation/systems/servers/2022-06-04-central-plexus %}).
10. Start the Jail.

## Documentation

**TODO**: need to fix the virtual host template.

If the Jail is to be kept, document the jail using `[the template](../../../systems/virtual-host-template.md)`.
