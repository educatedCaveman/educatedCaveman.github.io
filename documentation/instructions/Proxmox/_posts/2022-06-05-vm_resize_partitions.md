---
title: Resizing a VM's partitions
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

The following digest is based on [this](https://www.golinuxcloud.com/extend-resize-primary-partition-non-lvm-linux/#Method_2_Change_size_of_partition_using_fdisk_utility) guide. It has only been tested with Ubuntu, thusfar.

For proxmox, if VirtIO is used, there are some extra steps, as outlined here: https://blog.dgprasetya.com/promox-extend-lvm-partition-ofly/

## Expanding a VM

0.  Allocate more space to the Zvol in TrueNas:

    1.  In the TrueNAS web interface, navigate to Storage > Pools
    2.  Expand the `jail-VM` pool, then the `VM` dataset.
    3.  Find the relevant Zvol, click the 3 dots at the far right of the row, then click the Edit Zvol option
    4.  In the Edit Zvol window that appears, change the size, then click submit

1.  Run the following command, and note which partition needs to be expanded

        fdisk -l /dev/sda

2.  Run the previous command w/o the `-l` option

3.  in the `fdisk` menu, type `p` to reprint the existing partition table. it should look something like the following:

    ```shell
    Disk /dev/sda: 15 GiB, 16106127360 bytes, 31457280 sectors
    Units: sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disklabel type: dos
    Disk identifier: 0x5290bf38

    Device     Boot    Start      End  Sectors  Size Id Type
    /dev/sda1  *        2048  1050623  1048576  512M 83 Linux
    /dev/sda2        1050624 22022143 20971520   10G 83 Linux
    ```

4.  Still within the `fdisk` menu, use option `n` to expand the previously noted partition.

    1.  You will be asked to confirm the Partition type. It is a primary partition, which should be the default option. Select it with option `p`.
    2.  Select the number of the partition you noted earlier. It will likely be `2`.
    3.  Use the default start sector (lowest value possible).
    4.  Use the default end sector (largest value possible).
    5.  Confirm you **DO NOT** want to remove the drive signature, by selecting option `N`.
    6.  Re-print the new partition table with `p`, to confirm the changes were made.

5.  Run the following command to notify the OS of the change:

    ```shell
    partprobe /dev/sda
    ```

6.  Run the following command (replacing the drive letter and partition number as necessary) to resize the filesystem to take advantage of the new space:

    ```shell
    resize2fs /dev/sda2
    ```

7.  If the volume to be expanded is managed by LVM, the following commands are needed/useful. The first command has the `VG_NAME`. The second command yeilds the `volume_name`. The `/path/to/drive` is the `PV_NAME` reported by the first command.

    ```shell
    sudo pvdisplay
    ll /dev/<VG_NAME>
    sudo pvresize /path/to/drive
    sudo lvresize --extents +100%FREE --resizefs /dev/<VG_NAME>/<volume_name>
    ```

    Most often, the following command can be run after running fdisk:

    ```shell
    sudo pvresize $(sudo pvdisplay | grep "PV Name" | awk '{print $3}') && \
            sudo lvresize --extents +100%FREE --resizefs /dev/ubuntu-vg/ubuntu-lv && \
            df -h
    ```

# Shrinking a VM

**TODO**, but its basically the reverse of this. I don't expect this to ever happen.
