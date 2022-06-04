---
title: qBittorrent
date: 2022-06-04 15:19:00 -400
categories: []
tags: []
---

Documentation for qBittorrent

| PROPERTY      | VALUE                                                                           |
| ------------- | ------------------------------------------------------------------------------- |
| Name:         | qBittorrent                                                                     |
| Host:         | [Tesseract]({% post_url /documentation/systems/servers/2022-06-04-tesseract %}) |
| Type:         | LXC                                                                             |
| IP:           | `192.168.12.15`                                                                 |
| URL, internal | qbittorrent.vm                                                                  |
| configs:      | on host                                                                         |
| Purpose:      | torrent manager/downloader                                                      |

## URLs

- https://qbt.drak3.io/
- https://radarr.drak3.io/
- https://sonarr.drak3.io/
- https://lidarr.drak3.io/
- https://bazarr.drak3.io/
- https://jackett.drak3.io/

## Storage

- `/mnt/storage_node/Video/`
- `/mnt/storage_node/Music/iTunes/iTunes Media/Music/`
- `/mnt/storage_node/staging/qbittorrent/`

## Other Notes:

- also runs the scripts to convert .flac to .ogg (via cron)

- new changes as of 2021-12-18:

  - background: there was some kind of a network leak and my IP was associated with torrenting. thus, i've decided additional safeguards are necessary.
  - I've added a VPN to run on the host (express VPN - Amsterdam 2) starting at boot.
  - I've modified the host config with the following additional lines

    ```conf
    auth-user-pass /etc/openvpn/client/login.conf
    script-security 2
    up /etc/openvpn/update-systemd-resolved
    down /etc/openvpn/update-systemd-resolved
    dhcp-option 'DOMAIN-ROUTE .'
    down-pre
    route 192.168.0.0 255.255.0.0 net_gateway
    ```

    - `auth-user-pass`, `script-security 2`: for automating the login to the VPN.
    - `up/down /etc/openvpn/update-systemd-resolved`: sets and resets the DNS resolution when the tunnel starts and exits
    - `down-pre`, `dhcp-option ...`: relate to the DNS resolution
    - `route ...`: allows local connections to be made (for ssh, NFS, etc.)

  - the VPN config is located at `/etc/openvpn/client/amsterdam_2.conf`
  - the systemd service is `openvpn-client@amsterdam_2.service`
    - more generally, it is `openvpn-client@<profile>.service`, where `<profile>` is the name of the VPN .conf file, without the .conf.
  - I've added firewall rules which prohibit any outgoing traffic from the VM_VLAN not on port 1195 (ExpressVPN uses 1195 instead of 1194 for OpenVPN)
  - This aims to ensure the following:
    - all internet traffic from this host (torrents, mostly) are always VPNed
    - if the host VPN drops or otherwise failes silently, the firewall will prevent any internet traffic
    - if the FW VPN fails while still allowing traffic (ExpressVPN - Amsterdam 1) the internet traffic is still encrypted.
  - additionally, the config has been bound to the tun0 interface. this, combined with the above, should mean there is never a leak again

- the following services are also run on the container:
  - Radarr (movies)
  - Sonarr (TV)
  - Lidarr (music)
  - Bazarr (Subtitles)
  - Jackett (indexer)
  - they are all for automating downloads. makes it much easier. i should have done that YEARS ago.
