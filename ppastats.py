#!/usr/bin/env python

from __future__ import print_function
from six import string_types
import argparse
from launchpadlib.launchpad import Launchpad


def parse_arguments():
    parser = argparse.ArgumentParser(prog='ppastats',
                                     description='Get statistics for personal package archives'
                                                 '(PPA) for any Ubuntu release/architecture')
    parser.add_argument('-r', '--release', nargs='+',
                        help='Releases to get PPA for. This is the first word of the release, such'
                             'as "trusty" or "vivid". Additionally, a version number can be given'
                             '(14.04) and this will be translated to the proper release name.'
                             'Defaults to trusty.', default='trusty')
    parser.add_argument('-a', '--arch', nargs='+',
                        help='Architecture to consider (amd64 or i386). Defaults to amd64.',
                        default='amd64')
    parser.add_argument('ppa', nargs='+', help='PPAs to get stats for. Should be in the format of '
                                               '"owner:package" (ex: ondrej:php).')

    args = parser.parse_args()
    if isinstance(args.release, string_types):
        args.release = [args.release]
    if isinstance(args.arch, string_types):
        args.arch = [args.arch]
    return args.release, args.arch, args.ppa


def get_stats(releases, archs, ppas):
    lp_login = Launchpad.login_anonymously('ppastats', 'edge', "~/.launchpadlib/cache/",
                                           version='devel')  # Login into Launchpad Anoymously
    for ppa in ppas:
        ppa = ppa.split("/")
        ppa_owner = ppa[0]
        ppa_name = ppa[1]
        owner = lp_login.people[ppa_owner]  # PPA owner
        archive = owner.getPPAByName(name=ppa_name)  # PPA name
        for release in releases:
            for arch in archs:
                distro = 'https://api.launchpad.net/devel/ubuntu/' + release + '/' + arch
                print('Download stats for ' + str(ppa_owner) + '/' + str(ppa_name) + ' PPA')
                print('----------------------------------------------')
                print('')
                print(release + ' ' + arch + ' builds:')
                print('---------------')
                for individual_archive in archive.getPublishedBinaries(status='Published',
                                                                       distro_arch_series=distro):

                    # Write the package name, version and download count to the log file
                    print(individual_archive.binary_package_name + "\t" +
                          individual_archive.binary_package_version + "\t" + arch + "\t" +
                          str(individual_archive.getDownloadCount()))


if __name__ == "__main__":
    get_stats(*parse_arguments())
