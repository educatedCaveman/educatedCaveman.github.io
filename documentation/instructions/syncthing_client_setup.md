# Syncthing, client

Assuming the syncthing "server" has been set up, perform the following on the client device:

1. install the following packages:
   - syncthing
   - syncthing-gtk (optional)
2. install the syncthing.service file in `~/.config/systemd/user/syncthing.service`:

        [Unit]
        Description=Syncthing - Open Source Continuous File Synchronization for %I
        Documentation=man:syncthing(1)
        After=network.target

        [Service]
        ExecStart=/usr/bin/syncthing
        Restart=on-failure
        SuccessExitStatus=3 4
        RestartForceExitStatus=3 4

        [Install]
        WantedBy=default.target

3. run `systemctl enable --now syncthing@drake`
