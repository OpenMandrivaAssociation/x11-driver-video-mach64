Name:		x11-driver-video-mach64
Epoch:		1
Version:	6.9.4
Release:	12
Summary:	X.org driver for ATI Mach64 
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM U_Deal-with-pPict-pDrawable-NULL-for-source-only-pictures.patch bnc#865607 -- fixes crash in mach64 driver
Patch0:		U_Deal-with-pPict-pDrawable-NULL-for-source-only-pictures.patch
Patch1:		U_mach64-fix-build-probably-not-required-with-pci-acce.patch
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
%apply_patches

%build
autoreconf -ifs
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/mach64_drv.so

