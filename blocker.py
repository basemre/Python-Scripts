# -*- coding: utf-8 -*-

import time
from datetime import datetime as dt

hosts_path="/etc/hosts" # hosts location
redirect="127.0.0.1" # to be redirected site
website_list=["facebook.com", "www.facebook.com", "mail.com"] # to blocked sites

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 0) < dt.now()<dt(dt.now().year,dt.now().month, dt.now().day, 4):
        with open(hosts_path, 'r+') as file:
            content=file.read()
            print("working hours!")
            for website in website_list:
                if website in content:
                    pass #go other lines
                else:
                    file.write("\n"+redirect+" "+website)
                    file.write("\n"+redirect_v6+" "+website)
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("spare time, have fun!")
    time.sleep(5)
