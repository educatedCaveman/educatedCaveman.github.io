---
title: Adding a Disk
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

Currently, all drive pools contian mirror Vdevs, thus, drives must be added in pairs to systems. If the drives are Data drives, it is preferable to add them in pairs to both Mobius and Tesseract at the same time.

0.  Note the following information for both drives prior to inserting the drive into the system:
    1.  Manufacturer
    2.  Capacity
    3.  Model Number
    4.  Serial Number
1.  Follow [this guide](https://www.truenas.com/docs/hub/tasks/advanced/extendpool/) from the official docs on how to replace the disk.
2.  Next, uptdate the documentation.
    1.  [Mobius]({% post_url /documentation/systems/servers/2022-06-04-mobius %}) if the drives are in the front of the server.
    2.  [DAS]({% post_url /documentation/systems/misc/2022-06-04-das %}) if the drives are data drives in the DAS.
    3.  [Tesseract]({% post_url /documentation/systems/servers/2022-06-04-tesseract %}) if the drives are in Tesseract.
