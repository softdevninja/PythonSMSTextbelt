#!/usr/bin/env python3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def send_message():
    res = requests.post('https://textbelt.com/text', {
        'phone': PHONE_NUMBER,
        'message': 'Sending SMS message ...',
        'key': 'textbelt', 
    })
    print(res.json())

def main() -> int:
    send_message()
    return 0

if __name__ == '__main__':
    main()