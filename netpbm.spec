Summary:	A library for handling different graphics file formats
Name:		netpbm
Version:	9.9
Release:	3
License:	freeware
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/netpbm/%{name}-%{version}.tgz
Patch0:		%{name}-pktopbm.patch
Patch1:		%{name}-pnmtotiff.patch
Patch2:		%{name}-pstopnm.patch
Patch3:		%{name}-install.patch
Patch4:		%{name}-asciitopgm.patch
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgr

%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%package devel
Summary:	Development tools for programs which will use the netpbm libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libgr-devel

%package static
Summary:	Static netpbm libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	libgr-static

%description static
Static netpbm libraries.

%description devel
The netpbm-devel package contains the header files and static
libraries, etc., for developing programs which can handle the various
graphics file formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries. You'll also
need to have the netpbm package installed.

%package progs
Summary:	Tools for manipulating graphics files in netpbm supported formats
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}
Obsoletes:	libgr-progs

%description progs
The netpbm-progs package contains a group of scripts for manipulating
the graphics files in formats which are supported by the netpbm
libraries. For example, netpbm-progs includes the rasttopnm script,
which will convert a Sun rasterfile into a portable anymap.
Netpbm-progs contains many other scripts for converting from one
graphics file format to another.

If you need to use these conversion scripts, you should install
netpbm-progs. You'll also need to install the netpbm package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="$RPM_OPT_FLAGS -fPIC" \
	JPEGINC_DIR=%{_includedir} \
	PNGINC_DIR=%{_includedir} \
	TIFFINC_DIR=%{_includedir} \
	JPEGLIB_DIR=%{_libdir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFLIB_DIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
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

# Install header files.
install -d $RPM_BUILD_ROOT%{_includedir}
install pbm/pbm.h $RPM_BUILD_ROOT/%{_includedir}/
install pbmplus.h $RPM_BUILD_ROOT/%{_includedir}/
install pgm/pgm.h $RPM_BUILD_ROOT/%{_includedir}/
install pnm/pnm.h $RPM_BUILD_ROOT/%{_includedir}/
install ppm/ppm.h $RPM_BUILD_ROOT/%{_includedir}/

# Install the static-only librle.a
install urt/{rle,rle_config}.h $RPM_BUILD_ROOT/%{_includedir}/
install urt/librle.a $RPM_BUILD_ROOT%{_libdir}/

# Fixup symlinks.
ln -sf gemtopnm $RPM_BUILD_ROOT%{_bindir}/gemtopbm
ln -sf pnmtoplainpnm $RPM_BUILD_ROOT%{_bindir}/pnmnoraw

# Fixup perl paths in the two scripts that require it.
perl -pi -e 's^/bin/perl^%{__perl}^' \
$RPM_BUILD_ROOT%{_bindir}/{ppmfade,ppmshadow}

gzip -9nf COPYRIGHT.PATENT HISTORY README README.CONFOCAL

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
