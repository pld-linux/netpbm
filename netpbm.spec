Summary: A library for handling different graphics file formats.
Name: netpbm
Version: 9.5
Release: 5
Copyright: freeware
Group: System Environment/Libraries
Source0: ftp://download.sourceforge.net/pub/sourceforge/netpbm/netpbm-%{version}.tgz
Source1: jpeg-to-pnm.fpi
Source2: pnm-to-ps.fpi
Source3: bmp-to-pnm.fpi
Source4: gif-to-pnm.fpi
Source5: rast-to-pnm.fpi
Source6: tiff-to-pnm.fpi
Source7: png-to-pnm.fpi
Patch0: netpbm-9.5-install.patch
Patch1: netpbm-9.5-pktopbm.patch
Patch2: netpbm-9.5-pnmtotiff.patch
Patch3: netpbm-9.5-pstopnm.patch
Buildroot: %{_tmppath}/%{name}-root
BuildPrereq: libjpeg-devel, libpng-devel, libtiff-devel
Obsoletes: libgr

%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%package devel
Summary: Development tools for programs which will use the netpbm libraries.
Group: Development/Libraries
Requires: netpbm = %{version}
Obsoletes: libgr-devel

%description devel
The netpbm-devel package contains the header files and static libraries,
etc., for developing programs which can handle the various graphics file
formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries.  You'll also need
to have the netpbm package installed.

%package progs
Summary: Tools for manipulating graphics files in netpbm supported formats.
Group: Applications/Multimedia
Requires: netpbm = %{version}
Obsoletes: libgr-progs

%description progs
The netpbm-progs package contains a group of scripts for manipulating the
graphics files in formats which are supported by the netpbm libraries.  For
example, netpbm-progs includes the rasttopnm script, which will convert a
Sun rasterfile into a portable anymap.  Netpbm-progs contains many other
scripts for converting from one graphics file format to another.

If you need to use these conversion scripts, you should install
netpbm-progs.  You'll also need to install the netpbm package.

%prep
%setup -q
%patch0 -p1 -b .install
%patch1 -p1 -b .pktopbm
%patch2 -p1 -b .pnmtotiff
%patch3 -p1 -b .pstopnm

%build
make \
	CC=%{__cc} \
	CFLAGS="$RPM_OPT_FLAGS -fPIC" \
	JPEGINC_DIR=%{_includedir} \
	PNGINC_DIR=%{_includedir} \
	TIFFINC_DIR=%{_includedir} \
	JPEGLIB_DIR=%{_libdir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFLIB_DIR=%{_libdir}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
PATH="`pwd`:${PATH}" make install \
	JPEGINC_DIR=$RPM_BUILD_ROOT%{_includedir} \
	PNGINC_DIR=$RPM_BUILD_ROOT%{_includedir} \
	TIFFINC_DIR=$RPM_BUILD_ROOT%{_includedir} \
	JPEGLIB_DIR=%{_libdir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFLIB_DIR=%{_libdir} \
	INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INSTALLBINARIES=$RPM_BUILD_ROOT%{_bindir} \
	INSTALLHDRS=$RPM_BUILD_ROOT%{_includedir} \
	INSTALLLIBS=$RPM_BUILD_ROOT%{_libdir} \
	INSTALLMANUALS1=$RPM_BUILD_ROOT%{_mandir}/man1 \
	INSTALLMANUALS3=$RPM_BUILD_ROOT%{_mandir}/man3 \
	INSTALLMANUALS5=$RPM_BUILD_ROOT%{_mandir}/man5

mkdir -p $RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters
for filter in $RPM_SOURCE_DIR/*.fpi ; do
    install -m755 $filter \
	$RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters
done

# Install header files.
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m644 pbm/pbm.h $RPM_BUILD_ROOT/%{_includedir}/
install -m644 pbmplus.h $RPM_BUILD_ROOT/%{_includedir}/
install -m644 pgm/pgm.h $RPM_BUILD_ROOT/%{_includedir}/
install -m644 pnm/pnm.h $RPM_BUILD_ROOT/%{_includedir}/
install -m644 ppm/ppm.h $RPM_BUILD_ROOT/%{_includedir}/

# Install the static-only librle.a
install -m644 urt/{rle,rle_config}.h $RPM_BUILD_ROOT/%{_includedir}/
install -m644 urt/librle.a $RPM_BUILD_ROOT%{_libdir}/

# Fixup symlinks.
ln -sf gemtopnm $RPM_BUILD_ROOT%{_bindir}/gemtopbm
ln -sf pnmtoplainpnm $RPM_BUILD_ROOT%{_bindir}/pnmnoraw

# Fixup perl paths in the two scripts that require it.
perl -pi -e 's^/bin/perl^%{__perl}^' \
$RPM_BUILD_ROOT%{_bindir}/{ppmfade,ppmshadow}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYRIGHT.PATENT GPL_LICENSE.txt HISTORY README README.CONFOCAL
%{_libdir}/lib*.so.%{version}

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files progs
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/rhs/rhs-printfilters/jpeg-to-pnm.fpi
%{_libdir}/rhs/rhs-printfilters/pnm-to-ps.fpi
%{_libdir}/rhs/rhs-printfilters/bmp-to-pnm.fpi
%{_libdir}/rhs/rhs-printfilters/gif-to-pnm.fpi
%{_libdir}/rhs/rhs-printfilters/rast-to-pnm.fpi
%{_libdir}/rhs/rhs-printfilters/tiff-to-pnm.fpi
%{_libdir}/rhs/rhs-printfilters/png-to-pnm.fpi
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Wed Aug  9 2000 Crutcher Dunnavant <crutcher@redhat.com>
- added a png-to-pnm.fpi filter

* Wed Aug  2 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new libpng

* Mon Jul 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- move netpbm-progs to the Applications/Multimedia group
- reintroduce patches from the old libgr package

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jul  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 9.5

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 9.4

* Sat Jun  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- switch back to the netpbm tree, which is maintained again

* Mon Feb 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- make sure all man pages are included (#9328)
- fix pstopnm bomb when xres == yres (#9329)
- add libjpeg and libz because libtiff now needs them

* Wed Feb 02 2000 Nalin Dahyabhai <nalin@redhat.com>
- added/updated TIFF compression patch from jik@kamens.brookline.ma.us (#8826)

* Mon Dec 06 1999 Michael K. Johnson <johnsonm@redhat.com>
- added TIFF resolution patch from jik@kamens.brookline.ma.us (#7589)

* Mon Sep 20 1999 Michael K. Johnson <johnsonm@redhat.com>
- added section 5 man pages

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- fix tiff-to-pnm.fpi (#4267)

* Thu Jul 29 1999 Bill Nottingham <notting@redhat.com>
- add a pile of foo-to-bar.fpi filters (#4251)

* Mon Mar 23 1999 Michael Johnson <johnsonm@redhat.com>
- removed old png.h header file that was causing png utils to die
- build png in build instead of install section...

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- patch for 24-bit .BMP files (from sam@campbellsci.co.uk)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 15)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- clean up the spec file
- build for glibc 2.1
- patch to fix pktopbm

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- glibc2 defines random in <stdlib.h> (pbm/pbmplus.h problem #693)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- cleaned up the spec file a little bit
- validated mike's changes :-)

* Wed May 6 1998 Michael Maher <mike@redhat.com>
- added pnm-to-ps.fpi that was missing from previous packages

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- altered %install so that the package installs now even if a previous
  version was not installed on the system 

* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- built against libpng 1.0

* Thu Nov 06 1997 Donnie Barnes <djb@redhat.com>
- changed copyright from "distributable" to "freeware"
- added some missing scripts that existed in netpbm
- added some binaries that weren't getting built
- added patch to build tiff manipulation progs (requires libtiff)

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- obsoletes netpbm now

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>
- mucked config.guess and Make.Rules to build on Alpha/Linux

* Tue Oct 07 1997 Donnie Barnes <djb@redhat.com>
- updated to 2.0.13
- dropped libjpeg and libtiff (those should come from home sources)
- removed glibc patch (new version appears to have it!)
- added i686 as a valid arch type to config.guess

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
