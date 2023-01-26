from sys import stdin
from re import compile as comp

# Should have the right stdin input or else this will make the process stuck.
raw = stdin.read()

# Parsing the ip
pat = comp(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ip = pat.search(raw)[0] or None

"""

Your code goes here
For example:

import requests
from platform import uname
from datetime import datetime

requests.post(
    'https://api-server.example.com/vps-login',
    data={
        'ip': ip, 
        'node': uname().node, 
        'time': datetime.now().isoformat()
    }
)

"""
