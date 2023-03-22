"""
Author: TCPWITHFEELS
Date Written: YYYY/MM/DD
Last Modified By: <Your Name>
Date Last Modified: YYYY/MM/DD
Date Last Tested: YYYY/MM/DD
Result: Pass / Fail
Description: What the script does or is for
Dependencies: <library dependency>
Usage: `python3 python_script.py` or `python3 python_script.py <arguments>`
 All inputs required are in prompt format within the script.
"""

import argparse
import requests
from getpass import getpass

def main(**args: dict) -> None:
    verbose = args['verbose']
    verify = args['verify']
    user = args['user']

    # Get username if not set in arguments
    if user is None: 
        user = input("Username?\n> ")

    # Get password securely to keep it invisible to the screen.
    pwd = getpass()
    # Sample requests call (requires import of requests)
    r = requests.get('hostname', verify=verify, data={'a':'1','b':2})
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", type=str, help="Named Input") # Expect a value after the flat
    parser.add_argument("-i", "--insecure", action="store_true") # Boolean flag style
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    axl_user = args.user if args.user else None # Assign values
    verify = False if args.insecure else True # Assign boolean flag values
    verbose = True if args.verbose else False

    if verbose:
        print("What is going on, what the code is.")

    # Assign values to dictionary and pass to main function
    args = {
        "user": axl_user,
        "verify": verify,
        "verbose": verbose
    }

    # Wrap main function in try/catch to catch keyboard interrupt cleanly.
    try:
        main(**args)
    except KeyboardInterrupt:
        print("Interrupted by keyboard")