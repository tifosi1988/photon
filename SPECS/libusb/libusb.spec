Summary:        A library which allows userspace access to USB devices
Name:           libusb
Version:        1.0.20
Release:        2%{?dist}
License:        LGPLv2+
URL:            http://sourceforge.net/projects/libusb/
Group:          System Environment/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
Source:         http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2
%define sha1 libusb=9537243f165927bde74ad742e6b3effb0bd50cd2
BuildRequires:  systemd
Requires:       systemd

%description
This package provides a way for applications to access USB devices.

%package        devel
Summary:        Development files for libusb
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description    devel
This package contains the header files, libraries and documentation needed to
develop applications that use libusb.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/libusb*.so.*

%files devel
%{_includedir}/*
%{_libdir}/libusb*.so
%{_libdir}/libusb*.la
%{_libdir}/pkgconfig/*

%changelog
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.0.20-2
-	GA - Bump release of all rpms
* Thu May 05 2016 Nick Shi <nshi@vmware.com> 1.0.20-1
- Initial version

