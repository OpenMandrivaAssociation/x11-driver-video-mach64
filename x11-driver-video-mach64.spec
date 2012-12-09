Name: x11-driver-video-mach64
Epoch: 1
Version: 6.9.3
Release: 2
Summary: X.org driver for ATI Mach64 
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-mach64-%{version}.tar.bz2
Patch0:	5eb7fec958bc6ba8a1a2b0be4916cac818866e1c.patch

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1
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
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/mach64_drv.so



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:6.9.3-1
+ Revision: 810709
- version update 6.9.3

* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:6.9.2-2
+ Revision: 808344
- rel up
- version update 6.9.2

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.9.1-2
+ Revision: 787232
- Rebuild for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:6.9.1-1
+ Revision: 786712
- version update 6.9.1

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:6.9.0-3
+ Revision: 748418
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:6.9.0-2
+ Revision: 703653
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:6.9.0-1
+ Revision: 683670
- New version 6.9.0.
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1:6.8.2-5
+ Revision: 671153
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1:6.8.2-4mdv2011.0
+ Revision: 595719
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1:6.8.2-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 1:6.8.2-2mdv2010.1
+ Revision: 464338
- rebuild for new xserver

* Sat Aug 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1:6.8.2-1mdv2010.0
+ Revision: 407093
- update to new version 6.8.2

* Thu Apr 30 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.8.1-1mdv2010.0
+ Revision: 369180
- New version 6.8.1

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1:6.8.0-4mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1:6.8.0-3mdv2009.1
+ Revision: 308168
- rebuild for new X server

* Fri Jul 04 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.8.0-2mdv2009.0
+ Revision: 231810
- Correct wrong conflicts field.

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:6.8.0-1mdv2009.0
+ Revision: 219468
- import x11-driver-video-mach64

