# TODO:
# - documentation for progs: try to get some real man pages (old netpbm? Debian?)
#
# Conditional build:
%bcond_with	svga	# build ppmsvgalib tool
#
Summary:	A library for handling different graphics file formats
Summary(pl.UTF-8):	Biblioteki do obsługi różnych formatów graficznych
Summary(pt_BR.UTF-8):	Ferramentas para manipular arquivos graficos nos formatos suportados netpbm
Summary(ru.UTF-8):	Набор библиотек для работы с различными графическими файлами
Summary(uk.UTF-8):	Набір бібліотек для роботи з різними графічними файлами
Name:		netpbm
Version:	10.35.83
Release:	2
License:	Freeware
Group:		Libraries
#  svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/stable netpbm-%{version} (where version from doc/HISTORY)
#  svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/userguide netpbm-%{version}/userguide
Source0:	http://downloads.sourceforge.net/netpbm/%{name}-%{version}.tgz
# Source0-md5:	00ead6b73a9755f75e135a9b9ebb5d1d
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	8fb174f8da02ea01bf72a9dc61be10f1
Source2:	%{name}-docs-20030520.tar.bz2
# Source2-md5:	2d6a3965d493def21edfbc3e1aa262e9
Patch0:		%{name}-make.patch
Patch1:		%{name}-build.patch
URL:		http://netpbm.sourceforge.net/
BuildRequires:	flex
BuildRequires:	jasper-devel
BuildRequires:	jbigkit-devel
BuildRequires:	libjpeg-devel >= 7
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl-base
BuildRequires:	perl-modules
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libX11-devel
Obsoletes:	libgr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%description -l pl.UTF-8
Pakiet netpbm zawiera biblioteki funkcji obsługujących różne formaty
graficzne, w tym .pbm, .pgm, .pnm, .ppm.

%description -l pt_BR.UTF-8
O pacote netpbm contém bibliotecas de funções que suportam programas
para manipular vários formatos gráficos, incluindo .pbm (ortable
bitmaps), .pgm (portable graymaps), .pnm (portable anymaps), .ppm
(portable pixmaps) e outros

%description -l ru.UTF-8
Набор библиотек для обработки графических файлов различных форматов
включая FBM, PBM, PGM, PNM, PPM и REL.

%description -l uk.UTF-8
Набір бібліотек для обробки графічних файлів різних форматів,
включаючи FBM, PBM, PGM, PNM, PPM та REL.

%package devel
Summary:	Development tools for programs which will use the netpbm libraries
Summary(pl.UTF-8):	Biblioteka netpbm - część dla programistów
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento usados para libnetpbm
Summary(ru.UTF-8):	Хедеры и библиотеки для разработки программ, использующих netpbm
Summary(uk.UTF-8):	Хедери та бібліотеки для розробки програм, що використовують netpbm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgr-devel

%description devel
The netpbm-devel package contains the header files and programmer's
documentation for developing programs which can handle the various
graphics file formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries. You'll also
need to have the netpbm package installed.

%description devel -l pl.UTF-8
Pakiet netpbm-devel zawiera pliki nagłówkowe i dokumentację dla
programistów do tworzenia programów obsługujących formaty graficzne
wspierane przez netpbm.

%description devel -l pt_BR.UTF-8
The netpbm-devel package contains the header files and programmer's
documentation for developing programs which can handle the various
graphics file formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries. You'll also
need to have the netpbm package installed.

%description devel -l ru.UTF-8
Этот пакет содержит все необходимое для разработки программ,
работающих с графическими файлами в форматах, поддерживаемых netpbm.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, що працюють з
графічними файлами в форматах, що їх підтримує netpbm.

%package static
Summary:	Static netpbm libraries
Summary(pl.UTF-8):	Statyczne biblioteki netpbm
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libnetpbm
Summary(ru.UTF-8):	Статическая библиотека для программирования с netpbm
Summary(uk.UTF-8):	Статична бібліотека для програмування з netpbm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libgr-static

%description static
Static netpbm libraries.

%description static -l pl.UTF-8
Statyczne biblioteki netpbm.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libnetpbm.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих netpbm.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для написання
програм, що використовують netpbm.

%package rle-static
Summary:	Limited rle library
Summary(pl.UTF-8):	Okrojona biblioteka rle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	urt-static

%description rle-static
Limited version of rle library from netpbm.

%description rle-static -l pl.UTF-8
Okrojona wersja biblioteki rle z netpbm.

%package progs
Summary:	Tools for manipulating graphics files in netpbm supported formats
Summary(pl.UTF-8):	Narzędzia do konwersji plików graficznych
Summary(ru.UTF-8):	Утилиты манипулирования файлами форматов, поддерживаемых netpbm
Summary(uk.UTF-8):	Утиліти маніпулювання файлами форматів, підтримуваних netpbm
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
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

%description progs -l pl.UTF-8
Pakiet netpbm-progs zawiera programy konwertujące pliki graficzne do
oraz z formatów obsługiwanych przez biblioteki netpbm.

%description progs -l ru.UTF-8
Этот пакет включает разнообразные утилиты для работы с графическими
файлами в форматах, поддерживаемых netpbm.

%description progs -l uk.UTF-8
Цей пакет містить різноманітні утиліти для роботи з графічним файлами
в форматах, підтримуваних netpbm.

%package progs-pstopnm
Summary:	pstopnm - tool to convert PostScript files to PNM images
Summary(pl.UTF-8):	pstopnm - narzędzie do konwersji plików postscriptowych na obrazy PNM
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	fonts-Type1-urw
Requires:	ghostscript
Obsoletes:	libgr-progs
Conflicts:	ghostscript-esp

%description progs-pstopnm
This package contains pstopnm tool to convert PostScript files to PNM
images.

%description progs-pstopnm -l pl.UTF-8
Ten pakiet zawiera program konwertujący pliki w formacie PostScript na
obrazy w formacie PNM.

%package ppmsvgalib
Summary:	ppmsvgalib - display PPM image on Linux console using svgalib
Summary(pl.UTF-8):	ppmsvgalib - wyświetlanie obrazków PPM na konsoli przy użyciu svgalib
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description ppmsvgalib
ppmsvgalib - display PPM image on Linux console using svgalib.

%description ppmsvgalib -l pl.UTF-8
ppmsvgalib - wyświetlanie obrazków PPM na konsoli linuksowej przy
użyciu svgalib.

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p1

%build
./configure << EOF



















EOF

# it appends defines to pm_config.h twice if -j > 1
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	JPEGINC_DIR=%{_includedir} \
	PNGINC_DIR=%{_includedir} \
	TIFFINC_DIR=%{_includedir} \
	JPEGLIB_DIR=%{_libdir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFLIB_DIR=%{_libdir} \
	LINUXSVGALIB="%{?with_svga:%{_libdir}/libvga.so}%{!?with_svga:NONE}" \
	X11LIB=%{_libdir}/libX11.so \
	XML2LIBS="$(%{_bindir}/xml2-config --libs)" \
	JASPERLIB="" \
	JASPERDEPLIBS="-ljasper" \
	JASPERHDR_DIR="%{_includedir}/jasper" \
	NETPBM_DOCURL="%{_docdir}/%{name}-%{version}/netpbm.sourceforge.net/doc/"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man{1,3,5}}

rm -rf PKG
%{__make} -j1 package \
	pkgdir=$(pwd)/PKG \
	LINUXSVGALIB="%{?with_svga:%{_libdir}/libvga.so}%{!?with_svga:NONE}"

%{__rm} PKG/bin/doc.url
cp -df PKG/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -df PKG/lib/* $RPM_BUILD_ROOT%{_libdir}
install PKG/link/*.a $RPM_BUILD_ROOT%{_libdir}
install PKG/include/*.h $RPM_BUILD_ROOT%{_includedir}
install PKG/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install PKG/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install PKG/man/man5/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

# Install the static-only librle.a
install urt/{rle,rle_config}.h $RPM_BUILD_ROOT%{_includedir}
install urt/librle.a $RPM_BUILD_ROOT%{_libdir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.netpbm-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{COPYRIGHT.PATENT,HISTORY,USERDOC} netpbm.sourceforge.net
%attr(755,root,root) %{_libdir}/libnetpbm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetpbm.so.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetpbm.so
%{_includedir}/bitio.h
%{_includedir}/colorname.h
%{_includedir}/mallocvar.h
%{_includedir}/nstring.h
%{_includedir}/pam*.h
%{_includedir}/pbm*.h
%{_includedir}/pgm.h
%{_includedir}/pm*.h
%{_includedir}/pnm.h
%{_includedir}/ppm*.h
%{_includedir}/rle*.h
%{_includedir}/shhopt.h
%{_mandir}/man3/libnetpbm.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetpbm.a

%files rle-static
%defattr(644,root,root,755)
%{_libdir}/librle.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*topam
%attr(755,root,root) %{_bindir}/*topbm
%attr(755,root,root) %{_bindir}/*topgm
%attr(755,root,root) %{_bindir}/*topnm
%attr(755,root,root) %{_bindir}/*toppm
%attr(755,root,root) %{_bindir}/manweb
%attr(755,root,root) %{_bindir}/pam*
%attr(755,root,root) %{_bindir}/pbm*
%attr(755,root,root) %{_bindir}/pgm*
%attr(755,root,root) %{_bindir}/pnm*
%attr(755,root,root) %{_bindir}/ppm*
%{_mandir}/man1/*topam.1*
%{_mandir}/man1/*topbm.1*
%{_mandir}/man1/*topgm.1*
%{_mandir}/man1/*topnm.1*
%{_mandir}/man1/*toppm.1*
%{_mandir}/man1/manweb.1*
%{_mandir}/man1/pam*.1*
%{_mandir}/man1/pbm*.1*
%{_mandir}/man1/pgm*.1*
%{_mandir}/man1/pnm*.1*
%{_mandir}/man1/ppm*.1*
%{_mandir}/man5/pam.5*
%{_mandir}/man5/pbm.5*
%{_mandir}/man5/pgm.5*
%{_mandir}/man5/pnm.5*
%{_mandir}/man5/ppm.5*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man[15]/*
%exclude %{_bindir}/pstopnm
%exclude %{_mandir}/man1/pstopnm.1*
%{?with_svga:%exclude %{_bindir}/ppmsvgalib}
%{?with_svga:%exclude %{_mandir}/man1/ppmsvgalib.1*}

%files progs-pstopnm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pstopnm
%{_mandir}/man1/pstopnm.1*

%if %{with svga}
%files ppmsvgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppmsvgalib
%{_mandir}/man1/ppmsvgalib.1*
%endif
