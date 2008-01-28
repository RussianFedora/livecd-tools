%define debug_package %{nil}

Summary: Tools for building live CD's
Name: livecd-tools
Version: 013 
Release: 3%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
#Source0: livecd.tar.bz2
Patch0: imgcreate-old-pykickstart.patch
Patch1: imgcreate-try-finally.patch      
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
%{_libdir}/python?.?/site-packages/imgcreate/*

%changelog

* Tue Jan 29 Rahul Sundaram <sundaram@fedoraproject.org> - 013-3
  Fix build on x86_64
* Mon Jan 28 2008 Rahul Sundaram <sundaram@fedoraproject.org> - 013-2
- Initial build for EPEL

* Mon Oct 29 2007 Jeremy Katz <katzj@redhat.com> - 013-1
- Lots of config updates
- Support 'device foo' to say what modules go in the initramfs
- Support multiple kernels being installed
- Allow blacklisting kernel modules on boot with blacklist=foo
- Improve bootloader configs
- Split configs off for f8


