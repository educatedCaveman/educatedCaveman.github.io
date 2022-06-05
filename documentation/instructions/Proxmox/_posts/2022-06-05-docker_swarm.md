---
title: Docker Swarm Cluster
date: 2022-06-05 08:44:00 -400
categories: []
tags: []
---

some of the instructions are based on this guide: https://dockerlabs.collabnix.com/intermediate/Implementing_High_Availability_with_Docker_Swarm.html

Most of this is now addressed by Ansible playbooks: 

- `hosts/swarm/{env}_swarm.yml` 
- `maintenance/PW_hostname.yml` (run via `PW_hostname.sh`)

1.  Create the VMs
    - manager nodes: minumum 3 for HA. can also run workloads, but not recommended
    - worker nodes: any number (at least 1)
2.  Setup VMs:
    1. install configs (via ansible)
    2. change hostnames
    3. change passwords
    4. expand storage, if necessary
    5. install/configure docker (via ansible)
    6. install/configure NFS mounts (via ansible)
3.  run the following command on one of the manager nodes to initiate the swarm:

    ```shell
    docker swarm init
    ```

    which will output something like the following for joining worker nodes:

    ```shell
    docker swarm join --token <REDACTED_TOKEN> 192.168.13.25:2377
    ```

4.  run the following command:

    ```shell
    docker swarm join-token manager
    ```

    to get the command to add additional managers, which will look something like:

    ```shell
    docker swarm join --token <DIFFERENT_REDACTED_TOKEN> 192.168.13.25:2377
    ```

5.  after joining all the nodes, run `docker node ls` to confirm the cluster:

    ```
    ID                            HOSTNAME               STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
    zn5f0cukfz5ljk54f9hqsmntk *   lv426-manager-01.lab   Ready     Active         Leader           20.10.2
    rybtriehn1qe8zpcacyiwr3rs     lv426-manager-02.lab   Ready     Active         Reachable        20.10.2
    t2py69ncrl0fgd3rwml71v6my     lv426-manager-03.lab   Ready     Active         Reachable        20.10.2
    we71qtkx2ful2znuon67z260f     lv426-worker-01.lab    Ready     Active                          20.10.2
    zw0efzypj6m81c55q8gmiyrua     lv426-worker-02.lab    Ready     Active                          20.10.2
    pk4lvx8v0zs6ifuov0au65bhg     lv426-worker-03.lab    Ready     Active                          20.10.2
    pvqj3sad5cka83facge9ztq4i     lv426-worker-04.lab    Ready     Active                          20.10.2
    ```

6.  To deploy portainer, on one of the manager nodes, run the following command

    ```shell
    curl -L https://downloads.portainer.io/portainer-agent-stack.yml -o portainer-agent-stack.yml
    ```

    and/or create a `portainer-agent-stack.yml` file with the following contents (only the volume mount is changed):

    ```yml
    version: '3.2'

    services:
    agent:
        image: portainer/agent
        volumes:
        - /var/run/docker.sock:/var/run/docker.sock
        - /var/lib/docker/volumes:/var/lib/docker/volumes
        networks:
        - agent_network
        deploy:
        mode: global
        placement:
            constraints: [node.platform.os == linux]

    portainer:
        image: portainer/portainer-ce
        command: -H tcp://tasks.agent:9001 --tlsskipverify
        ports:
        - "9000:9000"
        - "8000:8000"
        volumes:
        - /mnt/gluster:/data
        networks:
        - agent_network
        deploy:
        mode: replicated
        replicas: 1
        placement:
            constraints: [node.role == manager]

    networks:
    agent_network:
        driver: overlay
        attachable: true

    volumes:
    portainer_data:
    ```

7.  then run the following command:

    ```shell
    docker stack deploy -c portainer-agent-stack.yml portainer
    ```
