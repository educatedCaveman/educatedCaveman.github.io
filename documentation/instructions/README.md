# INSTRUCTIONS

- [TrueNAS](#TrueNAS)
  - [Virtual Machines](#VM-admin)
    - [Docker](#Docker)
  - [Jails](#Jail-and-Plugin-Admin)
  - [Services](#Services)
  - [Hardware](#Hardware)
- [Linux](#Linux)
- [pfSense](#pfSense)
- [Certificates](#Certificates)
- [Misc](#Misc)

## TrueNAS

- Generally, referring to [the Docs](https://www.truenas.com/docs/hub/) is preferred. Note, the TrueNAS docs are organized differetly than the legacy FreeNAS docs. Generally, all the same info is there, it may just be harder to find.
- [Replacing a disk](TrueNAS/truenas_replace_disk.md)
- [Adding a disk](TrueNAS/truenas_add_disk.md)
- [VLAN setup](TrueNAS/mobius_VLANs.md) (only applies to [Mobius](../systems/servers/mobius.md))

### VM Admin

- [Creating](TrueNAS/VM/create_VM.md)
- [Resize VM partitions](TrueNAS/VM/vm_resize_partitions.md)
- [Deleting](TrueNAS/VM/delete_VM.md)

#### Docker

All docker instances are currently on either [Sevastopol](../systems/virtual/sevastopol.md) or [LV-426](../systems/virtual/lv-426.md), which are themselves VMs. Both are running [Portaniner](../applications/portainer.md) for ease of management.

**mostly still TODO**

- [Environment Setup](TrueNAS/VM/Docker/environment.md)
- [Promotion](TrueNAS/VM/Docker/promotion.md)
- [Creating](TrueNAS/VM/Docker/creation.md) a new image/stack
- [Removing](TrueNAS/VM/Docker/removal.md) an exisiting image/stack (w/ cleanup)

### Jail and Plugin Admin

All very high-level. Mostly just refers to the existing docs, and adds in a few order of operations stuff.

- [Creating](TrueNAS/jail/create_jail.md)
- [Updating](TrueNAS/jail/update_jail.md)
- [Deleting](TrueNAS/jail/delete_jail.md)

## pfSense

- **TODO**
- HAProxy
  - general setup (link to applications)
  - [adding new host](pfSense/add_new_haproxy.md)
- ACME
  - [add new cert](pfSense/add_new_ACME.md)

## Certificates

- how to create
- how to renew? (maybe not necessary)

## Misc

- [Adding or Replacing other hardware](misc/add_replace_misc_hardware.md)
