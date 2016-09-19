from __future__ import print_function
import sys, os
import time, datetime
from launchpadlib.launchpad import Launchpad

# For reference: "ppa:ownername/archivename" or "https://launchpad.net/~ownername/+archive/archive-name"
PPAOWNER = 'ondrej' # Name of the owner of the ppa you would like the stats for.
PPANAME = 'php' # Name of the PPA you would like the stats for.
ARCH = 'amd64' # System CPU architecture you would like the stats for. E.g. amd64, i386, etc.

lp_login = Launchpad.login_anonymously('ppastats', 'edge', "~/.launchpadlib/cache/", version='devel') # Login into Launchpad Anoymously
owner = lp_login.people[PPAOWNER] # PPA owner
archive = owner.getPPAByName(name=PPANAME) # PPA name

# Be sure to COMMENT OUT OR DELETE LINES NOT SUPPORTED BY THE PPA in question. For example if the PPA doesn't
# have Precise (12.04) or i386 support than you wouldn't use that version.

trusty_amd64 = 'https://api.launchpad.net/devel/ubuntu/' + 'trusty' + '/' + ARCH

# Declare a desination in home folder for the log files based on date
home = os.getenv("HOME") 
dirname = "/logs/"+PPANAME+'/'
year = time.strftime("%Y")+'/'
month = time.strftime("%m")+'/'
destination = home+dirname+year+month

print('Download stats for '+PPANAME+' PPA')
print('----------------------------------------------')
print('')
print('Trusty builds:')
print('---------------')

# For loop to write the log files with download statistics from the PPA
for individual_archive in archive.getPublishedBinaries(status='Published',distro_arch_series=trusty_amd64):

    x = individual_archive.getDownloadCount() # Get download count
    packagevers='~'.join(individual_archive.binary_package_version.split('~')[:-1]) # Get the package version
    #sys.stdout = open(destination+time.strftime("%Y-%m-%d-%I:%M-")+packagevers+'.txt',
    # 'w+') # Open the log file
    # Print heading
    if x > 0:
        # Write the package name, version and download count to the log file
        print(individual_archive.binary_package_name + "\t" +
              individual_archive.binary_package_version + "\t" + ARCH + "\t" + str(
            individual_archive.getDownloadCount()))
    elif x < 1:
        # If no stats are found print 'No data'
        print('No data')
