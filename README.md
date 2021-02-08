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