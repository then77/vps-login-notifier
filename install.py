# Script for installation
# Note: this will only work on linux system!

import os, platform
if __name__ == '__main__':
    if platform.system() == "Linux":
        if os.geteuid() == 0:
            print("Donwloading files...")
            os.system("curl -Lo /etc/login.py https://raw.githubusercontent.com/then77/vps-login-notifier/main/login.py >> /dev/null")

            print("Setting up permissions...")
            os.system("chmod 700 /etc/login.py >> /dev/null")

            print("Adding to motd file...")
            content, alreadyadded = [], False
            with open("/etc/update-motd.d/00-header", "r") as f:
                content = f.readlines()
                for x in content:
                    if "zgrep sshd /var/log/auth.log* -h | grep -F 'Accepted' | tail -n 1 | python3 /etc/login.py" in x:
                        alreadyadded = True
                        print("Already added to motd file!")
                        break
        
            if not alreadyadded:
                content.insert(1, "\n# For login system\nzgrep sshd /var/log/auth.log* -h | grep -F 'Accepted' | tail -n 1 | python3 /etc/login.py\n")
                with open("/etc/update-motd.d/00-header", "w") as f:
                    f.writelines(content)

            print(
                """

 #########################################################

              +++ Installation Completed! +++

          Please edit the file /etc/login.py and
        add your own code for sending notification!

         (c) 2023 by Realzzy. All rights reserved.

 #########################################################

                """
            )

        else: print("Please run this script as root!"); exit()
    else: print("This script only works on linux system!"); exit()
else: print("This script is not meant to be imported!"); exit()
