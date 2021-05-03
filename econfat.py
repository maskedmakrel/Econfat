import gnupg
import os
import shutil

#find your key
gpg = gnupg.GPG(gnupghome = '~/.gnupg')

#set the directories
path ='/home/maskedmakrel/econfat/fatasset'
artfile= '/awesomeart.png'

with open(path + artfile, 'rb')as f:
	status = gpg.encrypt_file(f, recipients = ['richartcollector@drunkbillionare.com'], output=path + artfile + ".nfat")

#make the directory for the token
os.mkdir('/home/maskedmakrel/econfat/NFAT')

#move the file after encryption
shutil.move('/home/maskedmakrel/econfat/fatasset/awesomeart.png.nfat', '/home/maskedmakrel/econfat/NFAT/awesomeart.png.nfat')

#add the license
shutil.copyfile('/home/maskedmakrel/econfat/nfatlicense/nfatgeneric.txt', '/home/maskedmakrel/econfat/NFAT/nfatgeneric.txt')

#make zipfile

shutil.make_archive('/home/maskedmakrel/econfat/NFAT',
                    'zip',
                    '/home/maskedmakrel/',
                    'econfat/NFAT')

print('Zip file with cryptoart is created successfully!')

print(status.ok)
print(status.stderr)

exit()
