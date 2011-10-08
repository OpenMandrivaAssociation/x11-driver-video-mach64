Name: x11-driver-video-mach64
Version: 6.9.0
Release: %mkrel 2
Epoch: 1
Summary: X.org driver for ATI Mach64 
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.bz2

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0
Conflicts: x11-driver-video-ati <= 1:6.8.0

%description
x11-driver-video-mach64 is the X.org driver for ATI Mach64.


%prep
%setup -q -n xf86-video-mach64-%{version}

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/mach64_drv.la
%{_libdir}/xorg/modules/drivers/mach64_drv.so
