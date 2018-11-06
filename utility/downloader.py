"""
Downloads a file and returns it to main.py.
Usage:
    python main.py [<url>] 
    or
    python main.py [<url>] [<file_name>]
"""

import os
import sys
from urllib import request as req
from tqdm import tqdm

# For a downloading bar
# import requests
# file_size = int(requests.head(from_url).headers["Content-Length"])
# for row in tqdm(file_name, total = file_size):

def download(from_url, to_file):
    
    if not os.path.isfile(to_file):
        req.urlretrieve(from_url, to_file)
        
        #for data in tqdm(response.iter_content(chunk_size=4096))


def download_file():
    try:
        global file_name
        _, url, file_name = sys.argv
    except:
        try:
            _, url = sys.argv
            file_name = os.path.basename(url)
        except:

            try:

                # open file
                cfg_file = file_name
                with open(cfg_file) as fp:
                    for line in fp:

                        file_name = os.path.basename(line.rstrip())
                        url = line
                        download(url, file_name)
                sys.exit(0)
            except Exception as e:
                print(__doc__)
                sys.exit(1)

    download(url, file_name)
    return file_name