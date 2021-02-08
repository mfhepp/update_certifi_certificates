# update_certifi_certificates.py
# Replaces the SSL certificates of the python-certifi package 
#     https://github.com/certifi/python-certifi
# with the most recent one from Mozilla from
#    https://mkcert.org/generate/
#
# This helps fixing certificate / SSL errors in case the certifi package is lagging behind.
#
# Warning: If the process of downloading the certificates is compromised, the entire SSL 
# mechanism is at risk!
#
# USAGE:
# 1. Activate the environment you want to apply this to [OPTIONAL, but recommended]
#     conda activate my_environment
# 2. Run the script
#     python update_certifi_certificates.py
#
# Written in 2021 by Martin Hepp, martin.hepp@unibw.de
# LICENSE: CC0, http://creativecommons.org/publicdomain/zero/1.0/
# To the extent possible under law, the author has waived all copyright and related or 
# neighboring rights to this work. 
#
import os
import urllib.request
import certifi

MOZILLA_URL = 'https://mkcert.org/generate/'


def strip_non_ascii(line):
    '''Strips non-ascii characters from PEM files, 
    replacing them with escaped backslashes.
    Adapted from 
    https://github.com/certifi/python-certifi/blob/master/strip-non-ascii'''
    line = line.decode('utf-8')
    line = line.encode('ascii', errors='backslashreplace')
    return line


ca_file = certifi.where()
os.rename(ca_file, ca_file + '-backup')
new_certificates = urllib.request.urlopen(MOZILLA_URL)
with open(ca_file, 'wb') as outfile:
    for line in new_certificates:
        clean_line = strip_non_ascii(line)
        outfile.write(line)
print(f'Replaced {ca_file} with certificates from {MOZILLA_URL}.')
