import tarfile
import glob


def create_tarfile():
    tfile = tarfile.open("C:/Temp/MyTarfile.tar", "w")
    for configfile in glob.glob("C:/Users/bwbeckwi/Documents/Scripts/PowerShell/*.ps1"):
        tfile.add(configfile)
    tfile.close()


create_tarfile()
