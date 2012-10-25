Name:		x11-driver-video-mach64
Epoch:		1
Version:	6.9.3
Release:	2
Summary:	X.org driver for ATI Mach64 
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.bz2
# from Fedora: rhbz#472687
Patch0:		mach64-6.8.1-defaultdepth.patch
# from Fedora: fix tvout code only building on 32-bit
Patch1:		0001-mach64-fix-build-on-32-bit.patch

BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(gl)

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0
Conflicts:	x11-driver-video-ati <= 1:6.8.0

%description
x11-driver-video-mach64 is the X.org driver for ATI Mach64.

%prep
%setup -qn xf86-video-mach64-%{version}
%patch0 -p1 -b .depth~
%patch1 -p1 -b .fix32~
autoreconf -ifs

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/mach64_drv.so
