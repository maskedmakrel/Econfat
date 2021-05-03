# Econfat
This is a simple python3 program which encrypts files (like art) and bundles the with a license. It uses GPG for the encryption.
I wrote this program so that I could digitally encrypt art files (pngs) using GPG and bundle it with a license text.

This program is intended as proof of concept that using secret keys and public keys people can exchange encrypted art sans digital currency. I tried to #comment on everything so that it will be clear what is happening.

The whole program is so short, I decided to write it like an old C-64 program line by line. Hope you like the retro vibe.

The directory structure is suggested. I did not go with the best-practices of relative file structures, but directed pointers to the specific folders I 
intended to work with.

For more background and useful examples, consider watching Paul Mahon's "GPG Free Data Encryption with Python" on Youtube. 

I tried to keep my program simple. I created a folder called econfat. In that folder, I kept a folder for Code.The art asset was stored in a folder called fatasset. 

I included a generic license text for the work in a folder called (nfatlicense).

I will exclude the license but you can generally look at NFT licenses to get the general gist.

The file outputs the results to a folder called NFAT. If you run the program twice, you will need to delete the NFAT folder and its contents. Again, this is only proof of concept. The NFAT folder is redundant once the zip is created.

The encrypted output is zipped up. The license remains unencrypted because people should always be able to read the licenses before and after they 
purchase goods and services. Nevertheless, whatever the license is, it should be included with the ultimate product.

Anyway, keeping it chill with the 90's encryption tech. 

