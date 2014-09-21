# Simplify vcard (VCF) export

After exporting all my contacts from google as a combined vcf file (contacts.vcf), I had a few problems importing to a Nokia 108.

* First and last name reversed after import
* Any record with a number not in the TEL record was ignored

# simplify.py

* for each vcard, read the ';' separated name and reverse
* allow blank surnames
* for each telephone number, create a new vcard with the correct first and last name
* print to stdout

# How to use

* split the contacts.vcf with [vcard-split.py](vcard-split.py) (I adapted from [here](https://gist.github.com/szczys/1478337#file-vcard-split-py))
* run `simplify.py > backup.dat` to create a file that the Nokia will import
* save backup.dat onto an sd card, insert into Nokia
* Nokia: menu -> contacts -> settings -> restore contacts

