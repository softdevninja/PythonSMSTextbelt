#!/usr/bin/env python3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

PHONE_NUMBER : int = os.getenv("PHONE_NUMBER")

def send_message(message : str) -> None:
    res = requests.post('https://textbelt.com/text', {
        'phone': PHONE_NUMBER,
        'message': message,
        'key': 'textbelt', 
    })
    
    print(f'{res.json()}')

def main() -> int:
    send_message("Sending SMS message ...")
    return 0

if __name__ == '__main__':
    main()