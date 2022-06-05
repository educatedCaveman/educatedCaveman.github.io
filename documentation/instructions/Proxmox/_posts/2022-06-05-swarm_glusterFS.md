---
title: GlusterFS for Docker swarm
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

2 gGusterFS clusters are created per Swarm cluster:

1.  Portainer persistent data. Runs only on the manager nodes. This is to replace the NFS mount, and have the storage be local.
2.  Docker configs and data. Runs on the worker nodes.

## Creating the clusters:

Generally, I'm following [this](https://medium.com/running-a-software-factory/setup-3-node-high-availability-cluster-with-glusterfs-and-docker-swarm-b4ff80c6b5c3) guide. This needs to happen prior to setting up portainer, or the data needs to be migrated after the fact.

### Migration:

The process would (probably) be:

0.  Snapshot all VMs
1.  Create the Gluster clusters
2.  Copy data over.
3.  Stop/remove all stacks/containers, including Portainer.
4.  Modify portainer stack to use glusterFS mountpoint
    - Test failover
5.  Modify other stacks to use the glusterFS mountpoint
    - Test failover
6.  Snapshot

### Creation:

should look into ansible playbooks

1.  Create new disks and attach to VMs
2.  [Prep drives on VMs](https://techguides.yt/guides/how-to-partition-format-and-auto-mount-disk-on-ubuntu-20-04/):

    - partition

        ```shell
        sudo fdisk /dev/vdb
        ```

    - format

        ```shell
        sudo mkfs.ext4 /dev/vdb1
        ```

    - add to fstab and mount

        ```shell
        sudo blkid /dev/sdv1
        ```
        output:
        ```
        dev/sdv1: LABEL="cloud1" UUID="d19baf53-02e5-4f65-9dc0-7416a5ae9e24" TYPE="ext4" PARTLABEL="primary" PARTUUID="d37fecad-5236-4a52-be97-c11f8abeb8dd"
        ```

        fstab:

        ```conf
        UUID=d19baf53-02e5-4f65-9dc0-7416a5ae9e24 /mnt/cloud1 ext4 defaults 0 0
        ```

3.  follow guide to setup glusertFS
