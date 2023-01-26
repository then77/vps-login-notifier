<h1 align="center">VPS Login Notifier</h1>
<p align="center">Let you get notified when someone logged in to your vps!</p>

## What is this?
This is a script that can let you know when someone logged in to your linux system via ssh. Mainly used on vps.<br>
This will let you get notified everytime someone is logged in.

## Installation
**⚠️ Note: This will only work on Linux system!**

1. First, install python3 from your package manager (ex. `apt`)
```bash
sudo apt install python3
```

2. You can choose to continue using installation script or keep manually installing.
```bash
sudo curl -Lo install.py https://raw.githubusercontent.com/then77/vps-login-notifier/main/install.py && sudo python3 install.py
```

#### If you continue manually install
1. First, get the script first and save it to somewhere (Ex. `/etc/`)
```bash
sudo curl -Lo /etc/login.py https://raw.githubusercontent.com/then77/vps-login-notifier/main/login.py
```

2. Set permission for the file so it will only accessible to root
```bash
sudo chmod 700 /etc/login.py
```

3. Then open the file, and add your own code for sending notification.
```bash
sudo nano /etc/login.py
```

4. Next, open the header file (Which is used on ssh login)
```bash
sudo nano /etc/update-motd.d/00-header
```

5. Right below `#!/bin/sh`, add this code below and save:
```bash
zgrep sshd /var/log/auth.log* -h | grep -F 'Accepted' | tail -n 1 | python3 /etc/login.py
```

6. It should be like this:
```bash
#!/bin/sh
zgrep sshd /var/log/auth.log* -h | grep -F 'Accepted' | tail -n 1 | python3 /etc/login.py
... (Some other text you should not touch)
```

7. Voila! Now try login back to your vps via ssh. It should sent you notification now.
