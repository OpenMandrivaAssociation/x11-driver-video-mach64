%define _disable_ld_no_undefined 1
Name:		x11-driver-video-mach64
Epoch:		1
Version:	6.10.0.3
Release:	1
Summary:	X.org driver for ATI Mach64 
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	https://github.com/X11Libre/xf86-video-mach64/archive/refs/tags/xlibre-xf86-video-mach64-%{version}.tar.gz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	autoconf
BuildRequires:	automake
BuildSystem:	autotools
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-mach64 is the X.org driver for ATI Mach64.

%prep -a
NOCONFIGURE=1 ./autogen.sh

%files
%{_libdir}/xorg/modules/xlibre-*/drivers/mach64_drv.so
