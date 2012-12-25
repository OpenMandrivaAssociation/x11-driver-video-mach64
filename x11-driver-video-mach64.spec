Name: x11-driver-video-mach64
Epoch: 1
Version: 6.9.4
Release: 1
Summary: X.org driver for ATI Mach64 
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.bz2

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1
BuildRequires: pkgconfig(gl)

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0
Conflicts: x11-driver-video-ati <= 1:6.8.0

%description
x11-driver-video-mach64 is the X.org driver for ATI Mach64.

%prep
%setup -qn xf86-video-mach64-%{version}
%apply_patches

%build
autoreconf -ifs
%configure
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/mach64_drv.so
