Summary: Tools for building live CD's
Name: livecd-tools
Version: 009
Release: 4%{?dist}
License: GPL
Group: System Environment/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
Source1: isotostick.sh
Patch: livecd-tools-009-repository.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: util-linux
Requires: coreutils
Requires: e2fsprogs
Requires: yum >= 3.0.0
Requires: mkisofs
Requires: squashfs-tools
Requires: pykickstart
Requires: syslinux
Requires: dosfstools >= 2.11-8
BuildArch: noarch
ExcludeArch: ppc ppc64

%description 
Tools for generating live CD's on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/livecd-iso-to-disk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README HACKING
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%dir /usr/lib/livecd-creator
/usr/lib/livecd-creator/mayflower
%dir %{_datadir}/livecd-tools
%{_datadir}/livecd-tools/*

%changelog
* Sun May 31 2008 Robert Scheck <robert@fedoraproject.org> - 009-4
- Updated outdated kickstart files (#318811, Christoph Wickert)

* Mon Nov  5 2007 Jeremy Katz <katzj@redhat.com> - 009-3
- And fix to actually work with F7

* Mon Nov  5 2007 Jeremy Katz <katzj@redhat.com> - 009-2
- Push new livecd-iso-to-disk that works with Fedora 8 live images

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

