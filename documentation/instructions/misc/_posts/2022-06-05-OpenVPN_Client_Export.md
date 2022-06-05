---
title: pfSense OpenVPN Client Export Utility
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

1. log in to pfSense
2. navigate to VPN > OpenVPN > Client Export
3. select the appropriate "Remote Access Server"
4. Export the appropriate Client:
   - for android, choose the "OpenVPN Connect (iOS/Android)" option
   - for laptop, choose the "Most Clients" option
5. Determine how to send it securely
6. Ensure the file has a .ovpn file extension
7. Import the config file into OpenVPN Connect:
   - change the profile name to something less verbose (opptional)
   - enter the username
   - check the "Save password" checkbox
   - enter the password
8. Connection should work automagically at this point.


Notes:
    - usernames and passwords are stored in Bitwarden