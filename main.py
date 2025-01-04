#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Sending SMS using Textbelt free API 

References: 
    https://textbelt.com/

"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

import requests
import os
from dotenv import load_dotenv

load_dotenv()

PHONE_NUMBER : int = os.getenv("PHONE_NUMBER")

def send_message(message : str) -> None:
    """
    Using POST to send SMS over Textbelt free API call.

    Args:
        message (str): Message to send over API

    Returns:
        None: 
    """
    res = requests.post('https://textbelt.com/text', {
        'phone': PHONE_NUMBER,
        'message': message,
        'key': 'textbelt', 
    })
    
    print(f'{res.json()}')

def main() -> int:
    """
    Main entry point.  Send message via function call. 
    
    Returns:
        None: N/A
    """
    send_message("Sending SMS message ...")
    return 0

if __name__ == '__main__':
    main()