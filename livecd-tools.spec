%define debug_package %{nil}
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Tools for building live CD's
Name: livecd-tools
Version: 013 
Release: 7%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
#Source0: livecd.tar.bz2
Patch0: livecd-tools-013-old-pykickstart.patch
Patch1: livecd-tools-013-try-finally.patch
Patch2: livecd-tools-013-iso-to-disk-path.patch      
Patch3: livecd-tools-013-ksconfigs.patch      
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: util-linux
Requires: coreutils
Requires: e2fsprogs
Requires: yum >= 3.0.0
Requires: mkisofs
Requires: squashfs-tools
Requires: pykickstart
#Requires: dosfstools >= 2.11-8
Requires: dosfstools 
#Requires: isomd5sum
Requires: anaconda-runtime
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
%ifarch ppc ppc64
Requires: yaboot
%endif


%description 
Tools for generating live CD's on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README HACKING
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/image-creator
%dir /usr/lib/livecd-creator
/usr/lib/livecd-creator/mayflower
%dir %{_datadir}/livecd-tools
%{_datadir}/livecd-tools/*
%{python_sitelib}/imgcreate/*

%changelog
* Sun Aug 03 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 013-7
- Fix ksconfigs, fix building and naming of patches

* Tue Jan 29 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 013-5
- Patch livecd-iso-to-disk for checkisomd5 location

* Tue Jan 29 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 013-4
- Use python sitelib macro properly

* Tue Jan 29 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 013-3
- Fix build on x86_64

* Mon Jan 28 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 013-2
- Initial build for EPEL

* Mon Oct 29 2007 Jeremy Katz <katzj@redhat.com> - 013-1
- Lots of config updates
- Support 'device foo' to say what modules go in the initramfs
- Support multiple kernels being installed
- Allow blacklisting kernel modules on boot with blacklist=foo
- Improve bootloader configs
- Split configs off for f8


