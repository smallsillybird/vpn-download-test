import wget
import tarfile
import os
wget.download(vpn.lfq5.eu.org/profiles,out=profiles.txt)
tar=tarfile.open(profiles.txt)
tar.extractall()
