# Update Certifi Certificates
Replaces the SSL certificates of the python-certifi package 
    https://github.com/certifi/python-certifi
with the most recent one from Mozilla from
    https://mkcert.org/generate/

 This helps fixing certificate / SSL errors in case the certifi package is lagging behind.

**Warning:** If the process of downloading the certificates is compromised, the entire SSL 
mechanism is at risk!

## Usage
1. Activate the environment you want to apply this to [OPTIONAL, but recommended]

        conda activate my_environment

**Note:** If you run the script in your base environment, the changes will apply to the base installation. If you run it from within a conda (or other) environment, the changes will only apply to the later. An update of the certifi package will overwrite the changes.

2. Run the script

        python update_certifi_certificates.py

The script renames the orginal file to <old_filename>-backup.


## Troubleshooting
If the script fails after renaming the current certificate file, you have to reverse the renaming of the original file, like so:

    $ cd /Users/xyz/anaconda3/envs/name/lib/python3.8/site-packages/certifi/
    $ mv cacert.pem-backup cacert.pem

The correct path to be used for the `cd`command is shown in the output of the script.

## Missing Intermediate Certificates in Python SSL / Requests / Reppy 

This script does not solve the issue of missing **intermediate certificates** in Python.

It is a common flaw in SSL server configurations to provide an incomplete chain of certificates, often omitting intermediate certificates. Because this configuration flaw is common, most but not all modern browsers implement a technique called "AIA Fetching" to fix this on the fly (see e.g. https://www.thesslstore.com/blog/aia-fetching/).

Python's SSL support does not support AIA Fetching and depends on a complete chain of certificates from the server; otherwise it throws an exception, like so

    SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)')))

I wrote a longer [piece for StackOverflow on how to add such missing intermediate certificates to `certifi`.](https://stackoverflow.com/a/66111417/516699)

## License and Disclaimer
Written in 2021 by Martin Hepp, martin.hepp@unibw.de
LICENSE: CC0, http://creativecommons.org/publicdomain/zero/1.0/
To the extent possible under law, the author has waived all copyright and related or 
neighboring rights to this work. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.