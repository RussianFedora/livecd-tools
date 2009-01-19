%{!?python_sitelib: %define python_sitelib %(%{__python} -c "import distutils.sysconfig as d; print d.get_python_lib()")}

%define debug_package %{nil}

Summary: Tools for building live CD's
Name: livecd-tools
Version: 021
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: util-linux
Requires: coreutils
Requires: e2fsprogs
Requires: yum >= 3.2.18
Requires: mkisofs
Requires: squashfs-tools
Requires: pykickstart >= 0.96
Requires: dosfstools >= 2.11-8
Requires: isomd5sum
Requires: rhpl
Requires: python-urlgrabber
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
%ifarch ppc
Requires: yaboot
%endif
BuildRequires: python
BuildRequires: /usr/bin/pod2man


%description 
Tools for generating live CD's on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README HACKING API
%doc config/livecd-fedora-minimal.ks
%{_mandir}/man*/*
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_bindir}/image-creator
%dir %{python_sitelib}/imgcreate
%{python_sitelib}/imgcreate/*.py
%{python_sitelib}/imgcreate/*.pyo
%{python_sitelib}/imgcreate/*.pyc

%changelog
* Mon Jan 19 2009 Jeremy Katz <katzj@redhat.com> - 021-1
- Start of support for hybrid GPT/MBR usb sticks (Stewart Adam)
- Fix for udev deprecated syntax (#480109)
- Keep cache with --cache (Jan Kratochvil, #479716)
- Use absolute path to cachedir (#479716)
- Support UDF for large ISO spins (Bruno Wolf, #476696)
- Improvements for encrypted /home setup (mdomsch, #475399)
- Don't allow spaces in labels (#475834)
- Fix --tmpdir relative path (dhuff)
- Support ext4 rootfs
- Fix device command version check (apevec)
- Allow URLs for specifying the kickstart config (bkearney)
- Fix macro name for excludedocs (bkearney)
- Fix up --base-on (#471656)

* Wed Nov 12 2008 Jeremy Katz <katzj@redhat.com> - 020-1
- Support setting up a swap file
- Verify integer args in livecd-iso-to-disk (#467257)
- Set up persistent /home on internal mtd0 for XO
- Default to resetting the overlay on XO
- Support copying the raw ext3fs to the usb stick instead of the squash
- Mactel fixes
- Align initrd properly on XO (#467093)
- Make initrd load addr work on newer XO firmwares
- Fix up Xen paths for Xen live images (Michael Ansel)
- Support --defaultdesktop (Orion Poplawski)

* Fri Oct 10 2008 Jeremy Katz <katzj@redhat.com> - 019-1
- livecd-iso-to-disk: Various other XO fixes
- Cleanup rpmdb locks after package installation
- Fix traceback due to lazy rhpl.keyboard import
- Fix using groups with options (jkeating)
- Support persistent /home on XO's internal flash
- Fix ramdisk load addr in boot/olpc.fth for XO
- Fix up boot from SD
- Fix extracting boot parameters for pxe (apevec)
- Make rpm macro information persist into the image (bkearney)
- Support %packages --instLangs (bkearney)

* Thu Aug 28 2008 Jeremy Katz <katzj@redhat.com> - 018-1
- Use logging API for debugging messages (dhuff)
- Some initial support for booting live images on an XO
- Refactoring of mount code for appliance-creator (danpb, dhuff)
- Make --base-on actually work again
- Drop the image configs; these are now in the spin-kickstarts repo
- plymouth support
- Listen to bootloader --append in config
- Add man pages (Pedro Silva)
- Support booting from Intel based Macs via EFI on USB (#450193)
- Fixes for SELinux enforcing (eparis)
- Eject the CD on shutdown (#239928)
- Allow adding extra kernel args with livecd-iso-to-disk
- Support for persistent /home (#445218)
- Copy timezone to /etc/localtime (#445624)
- Ensure that commands run by livecd-creator exist
- Mount a tmpfs for some dirs (#447127)

* Tue May  6 2008 Bill Nottingham <notting@redhat.com> - 017-1
- fix F9 final configs

* Thu May  1 2008 Jeremy Katz <katzj@redhat.com> - 016-1
- Config changes all around, including F9 final configs
- Fix up the minimal image creation
- Fix odd traceback error on __del__ (#442443)
- Add late initscript and split things in half
- livecd-iso-to-disk: Check the available space on the stick (#443046)
- Fix partition size overriding (kanarip)

* Thu Mar  6 2008 Jeremy Katz <katzj@redhat.com> - 015-1
- Support for using live isos with pxe booting (Richard W.M. Jones and 
  Chris Lalancette)
- Fixes for SELinux being disabled (Warren Togami)
- Stop using mayflower for building the initrd; mkinitrd can do it now
- Create a minimal /dev rather than using the host /dev (Warren Togami)
- Support for persistent overlays when using a USB stick (based on support 
  by Douglas McClendon)

* Tue Feb 12 2008 Jeremy Katz <katzj@redhat.com> - 014-1
- Rework to provide a python API for use by other tools (thanks to 
  markmc for a lot of the legwork here)
- Fix creation of images with ext2 filesystems and no SELinux
- Don't require a yum-cache directory inside of the cachedir (#430066)
- Many config updates for rawhide
- Allow running live images from MMC/SD (#430444)
- Don't let a non-standard TMPDIR break things (Jim Meyering)

* Mon Oct 29 2007 Jeremy Katz <katzj@redhat.com> - 013-1
- Lots of config updates
- Support 'device foo' to say what modules go in the initramfs
- Support multiple kernels being installed
- Allow blacklisting kernel modules on boot with blacklist=foo
- Improve bootloader configs
- Split configs off for f8

* Tue Sep 25 2007 Jeremy Katz <katzj@redhat.com> - 012-1
- Allow %%post --nochroot to work for putting files in the root of the iso
- Set environment variables for when %%post is run
- Add progress for downloads (Colin Walters)
- Add cachedir option (Colin Walters)
- Fixes for ppc/ppc64 to work again
- Clean up bootloader config a little
- Enable swaps in the default desktop config
- Ensure all configs are installed (#281911)
- Convert method line to a repo for easier config reuse (jkeating)
- Kill the modprobe FATAL warnings (#240585)
- Verify isos with iso-to-disk script
- Allow passing xdriver for setting the xdriver (#291281)
- Add turboliveinst patch (Douglas McClendon)
- Make iso-to-disk support --resetmbr (#294041)
- Clean up filesystem layout (Douglas McClendon)
- Manifest tweaks for most configs

* Tue Aug 28 2007 Jeremy Katz <katzj@redhat.com> - 011-1
- Many config updates for Fedora 8
- Support $basearch in repo line of configs; use it
- Support setting up Xen kernels and memtest86+ in the bootloader config
- Handle rhgb setup
- Improved default fs label (Colin Walters)
- Support localboot from the bootloader (#252192)
- Use hidden menu support in syslinux
- Have a base desktop config included by the other configs (Colin Walters)
- Use optparse for optino parsing
- Remove a lot of command line options; things should be specified via the
  kickstart config instead
- Beginnings of PPC support (David Woodhouse)
- Clean up kernel module inclusion to take advantage of files in Fedora
  kernels listing storage drivers

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 010-1
- Separate out configs used for Fedora 7
- Add patch from Douglas McClendon to make images smaller
- Add patch from Matt Domsch to work with older syslinux without vesamenu
- Add support for using mirrorlists; use them
- Let livecd-iso-to-disk work with uncompressed images (#248081)
- Raise error if SELinux requested without being enabled (#248080)
- Set service defaults on level 2 also (#246350)
- Catch some failure cases
- Allow specifying tmpdir
- Add patch from nameserver specification from Elias Hunt

* Wed May 30 2007 Jeremy Katz <katzj@redhat.com> - 009-1
- miscellaneous live config changes
- fix isomd5 checking syntax error

* Fri May  4 2007 Jeremy Katz <katzj@redhat.com> - 008-1
- disable screensaver with default config
- add aic7xxx and sym53c8xx drivers to default initramfs
- fixes from johnp for FC6 support in the creator
- fix iso-to-stick to work on FC6

* Tue Apr 24 2007 Jeremy Katz <katzj@redhat.com> - 007-1
- Disable prelinking by default
- Disable some things that slow down the live boot substantially
- Lots of tweaks to the default package manifests
- Allow setting the root password (Jeroen van Meeuwen)
- Allow more specific network line setting (Mark McLoughlin)
- Don't pollute the host yum cache (Mark McLoughlin)
- Add support for mediachecking

* Wed Apr  4 2007 Jeremy Katz <katzj@redhat.com> - 006-1
- Many fixes to error handling from Mark McLoughlin
- Add the KDE config
- Add support for prelinking
- Fixes for installing when running from RAM or usb stick
- Add sanity checking to better ensure that USB stick is bootable

* Thu Mar 29 2007 Jeremy Katz <katzj@redhat.com> - 005-3
- have to use excludearch, not exclusivearch

* Thu Mar 29 2007 Jeremy Katz <katzj@redhat.com> - 005-2
- exclusivearch since it only works on x86 and x86_64 for now

* Wed Mar 28 2007 Jeremy Katz <katzj@redhat.com> - 005-1
- some shell quoting fixes
- allow using UUID or LABEL for the fs label of a usb stick
- work with ext2 formated usb stick

* Mon Mar 26 2007 Jeremy Katz <katzj@redhat.com> - 004-1
- add livecd-iso-to-disk for setting up the live CD iso image onto a usb 
  stick or similar

* Fri Mar 23 2007 Jeremy Katz <katzj@redhat.com> - 003-1
- fix remaining reference to run-init

* Thu Mar 22 2007 Jeremy Katz <katzj@redhat.com> - 002-1
- update for new version

* Fri Dec 22 2006 David Zeuthen <davidz@redhat.com> - 001-1%{?dist}
- Initial build.

