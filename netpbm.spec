Summary:	A library for handling different graphics file formats
Summary(pl):	Biblioteki do obs³ugi ró¿nych formatów graficznych
Name:		netpbm
Version:	9.20
Release:	1
License:	freeware
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://download.sourceforge.net/pub/sourceforge/netpbm/%{name}-%{version}.tgz
Patch0:		%{name}-install.patch
Patch1:		%{name}-system-jbig.patch
Patch2:		%{name}-Makefile.common.patch
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	jbigkit-devel
BuildRequires:	perl
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgr

%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%description -l pl
Pakiet netpbm zawiera biblioteki funkcji obs³uguj±cych ró¿ne formaty
graficzne, w tym .pbm, .pgm, .pnm, .ppm.

%package devel
Summary:	Development tools for programs which will use the netpbm libraries
Summary(pl):	Biblioteka netpbm - czê¶æ dla programistów
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libgr-devel

%description devel
The netpbm-devel package contains the header files and programmer's
documentation for developing programs which can handle the various
graphics file formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries. You'll also
need to have the netpbm package installed.

%description devel -l pl
Pakiet netpbm-devel zawiera pliki nag³ówkowe i dokumentacjê dla
programistów do tworzenia programów obs³uguj±cych formaty
graficzne wspierane przez netpbm.

%package static
Summary:	Static netpbm libraries
Summary(pl):	Statyczne biblioteki netpbm
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	libgr-static

%description static
Static netpbm libraries.

%description static -l pl
Statyczne biblioteki netpbm.

%package progs
Summary:	Tools for manipulating graphics files in netpbm supported formats
Summary(pl):	Narzêdzia do konwersji plików graficznych
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

%description progs -l pl
Pakiet netpbm-progs zawiera programy konwertuj±ce pliki graficzne
do oraz z formatów obs³ugiwanych przez biblioteki netpbm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -fPIC" \
	JPEGINC_DIR=%{_includedir} \
	PNGINC_DIR=%{_includedir} \
	TIFFINC_DIR=%{_includedir} \
	JPEGLIB_DIR=%{_libdir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFLIB_DIR=%{_libdir} << EOF
gnu
/usr
regular
shared
yes
EOF

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
install pbm/pbm.h $RPM_BUILD_ROOT/%{_includedir}
install pbm/pm.h $RPM_BUILD_ROOT/%{_includedir}
install pm_config.h $RPM_BUILD_ROOT/%{_includedir}
install pgm/pgm.h $RPM_BUILD_ROOT/%{_includedir}
install pnm/pnm.h $RPM_BUILD_ROOT/%{_includedir}
install ppm/ppm.h $RPM_BUILD_ROOT/%{_includedir}
install shhopt/shhopt.h $RPM_BUILD_ROOT/%{_includedir}

# Install the static-only librle.a
install urt/{rle,rle_config}.h $RPM_BUILD_ROOT/%{_includedir}/
install urt/librle.a $RPM_BUILD_ROOT%{_libdir}/

# Fixup symlinks.
ln -sf gemtopnm $RPM_BUILD_ROOT%{_bindir}/gemtopbm
ln -sf pnmtoplainpnm $RPM_BUILD_ROOT%{_bindir}/pnmnoraw

# Fixup perl paths in the two scripts that require it.
perl -pi -e 's^/bin/perl^%{__perl}^' \
	$RPM_BUILD_ROOT%{_bindir}/{ppmfade,ppmshadow}

gzip -9nf COPYRIGHT.PATENT HISTORY README

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
