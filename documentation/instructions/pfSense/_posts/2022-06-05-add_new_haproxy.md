---
title: Adding new Host to HAProxy
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

- [High-level Procedure](#High-Level-Procedure)
- [Detailed Procedure](#Detailed-Procedure)
  - [Create ACME cert](#Create-Cert-Using-ACME)
  - [Create Backend](#Create-Backend)
  - [Add to Existing Frontend](#Add-to-Existing-Frontend)
  - [Create New Frontend](#Create-New-Frontend)
  - [Add Hostfile Entry](#Add-Hostfile-Entry)
- [Useful Guides](#Useful-Guides)

## Useful Guides

- https://blog.devita.co/pfsense-to-proxy-traffic-for-websites-using-pfsense/#step3createhaproxybackends
- https://www.youtube.com/watch?v=gVOEdt-BHDY
- https://crepaldi.us/2020/06/25/issuing-lets-encrypt-certificates-on-your-pfsense-using-acme/

## High Level Procedure

1.  Create cert for it using [ACME]({% post_url /documentation/systems/servers/2022-06-05-add_new_ACME %})
2.  Create new backend in HAProxy
3.  Add new backend to External and/or Internal frontend, as appropriate
4.  Add entry for it in pihole hosts file

## Detailed Procedure

### Create Cert Using ACME

Preferably clone and edit the hostname of an existing cert. Detailed procedure documented, [here](({% post_url /documentation/systems/servers/2022-06-05-add_new_ACME %})

### Create Backend

Cloning an existing backend, then modifying as below is the easiest method.

1.  Under HAProxy > Backend, either add new, or clone existing.
2.  Add the server to the server list.
    - if the server is capable of SSL, check the encrypt checkbox, but do not check the SSL check checkbox
3.  Select the CA (ACME CEERT)
4.  Select the Client Certificate
5.  Health Check: None
6.  Leave all other options default

### Add to Existing Frontend

If there is no existing frontend, skip to [here](#Create-New-Frontend).

1.  Edit existing frontend
2.  Under access control lists, add new "Host matches" entry, giving it a meaningful name, such as the subdomain
3.  Under actions, add new "Use Backend", using the ACL name entered previously
4.  Add the certificate under "Additional Certificates"
5.  Save, and restart HAProxy

### Create New Frontend

1.  Click the Add button under HAPRoxy > Frontend
2.  Enter a name
3.  Under External Address, fill out as follows:
    1.  Listen address: either WAN or custom address
        - If for external use (WAN), leave custom address blank
        - If for internal use, enter HAProxy virtual IP
    2.  Select the port (80 or 443, or something else)
    3.  If using SSL/certs, check the SSL Offloading checkbox
4.  Under Access Control Lists, add a new entyr:
    1.  Name can be anything, but keep it short, simple, and meaningful. usually the subdomain to be proxied.
    2.  Expression is usually "Host Matches"
    3.  Value is the full domain name, such as `myservice.drak3.io`
5.  Under Actions, add a new entry:
    1.  Action: Use Backend
    2.  ACL name: the name entered in 4.1
    3.  backend: the backend created earlier
6.  SSL offloading:
    1.  Under Certificate:
        - Select the cert for the backend
        - Check both checkboxes
    2.  Under Additional Certificates:
        - Check both checkboxes

### Add Hostfile Entry

In order to use the hostname locally, it must be added to the pihole hostsfile. For example, if I wanted to use `myservice.drak3.io`, i would add the following line to the hostfile:

```conf
192.168.11.5    myservice.drak3.io
```

I would then run the following command to restart DNS on the pihole:

```shell
pihole restartdns
```

#### Notes:

- 182.168.11.5 is the virtual IP for the local HAProxy frontend
