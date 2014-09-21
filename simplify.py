import glob
import re

#print a simple vcard
def make_vcard(firstname,surname,number):
    print("BEGIN:VCARD")
    print("VERSION:3.0")
    print("N:%s;%s;" % (firstname, surname))
    print("TEL:%s" % number)
    print("END:VCARD")

#for all vcards
cards = glob.glob('./cards/*vcf')
for card in cards:
    with open(card) as fh:
        for r in fh.readlines():
            #get the name
            if r.startswith('N:'):
                r = r.replace('N:','')
                names = r.split(';')
                #ok to have blank surname
                surname = ''
                if names[1]:
                    #for some reason they are reversed when exported from google
                    first_name = names[1]
                    surname = names[0]
                else:
                    first_name = names[0]
                #print(first_name + "," + surname)
            #for each record that's a telephone number:
            elif 'TEL' in r:
                m = re.match('item.*TEL:([0-9-]+)', r)
                if m:
                    #make a vcard
                    make_vcard(first_name,surname,m.group(1))
                m = re.match('^TEL;.*:([0-9-]+)', r)
                if m:
                    #make a vcard
                    make_vcard(first_name,surname,m.group(1))
