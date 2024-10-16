%define _disable_ld_no_undefined 1
Name:		x11-driver-video-mach64
Epoch:		1
Version:	6.10.0
Release:	1
Summary:	X.org driver for ATI Mach64 
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.xz
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-mach64 is the X.org driver for ATI Mach64.

%prep
%setup -qn xf86-video-mach64-%{version}
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/mach64_drv.so

