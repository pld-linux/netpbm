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
Version:	10.73.34
Release:	1
License:	Freeware
Group:		Libraries
#  svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/stable netpbm-%{version} (where version from doc/HISTORY)
#  svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/userguide netpbm-%{version}/userguide
Source0:	http://downloads.sourceforge.net/netpbm/%{name}-%{version}.tgz
# Source0-md5:	c5da60ea36f991e91fa231549cf4c6b9
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	8fb174f8da02ea01bf72a9dc61be10f1
Source2:	%{name}-docs-20030520.tar.bz2
# Source2-md5:	2d6a3965d493def21edfbc3e1aa262e9
Patch0:		%{name}-make.patch
Patch1:		%{name}-format.patch
URL:		http://netpbm.sourceforge.net/
BuildRequires:	flex
BuildRequires:	jasper-devel
BuildRequires:	jbigkit-devel
BuildRequires:	libjpeg-devel >= 7
BuildRequires:	libpng-devel >= 1.0
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 1:2.5.9
BuildRequires:	perl-base
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
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
Requires:	libxml2 >= 1:2.5.9
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
	JASPERHDR_DIR="%{_includedir}/jasper" \
	JASPERLIB="-ljasper" \
	JBIGHDR_DIR=%{_includedir} \
	JBIGLIB="-ljbig" \
	JPEGINC_DIR=%{_includedir} \
	JPEGLIB_DIR=%{_libdir} \
	LINUXSVGALIB="%{?with_svga:%{_libdir}/libvga.so}%{!?with_svga:NONE}" \
	NETPBM_DOCURL="%{_docdir}/%{name}-%{version}/netpbm.sourceforge.net/doc/" \
	PNGINC_DIR=%{_includedir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFINC_DIR=%{_includedir} \
	TIFFLIB_DIR=%{_libdir} \
	X11LIB=%{_libdir}/libX11.so \
	XML2LIBS="$(%{_bindir}/xml2-config --libs)"
#	JASPERLIB="" \
#	JASPERDEPLIBS="-ljasper" \

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
cp -p PKG/link/*.a $RPM_BUILD_ROOT%{_libdir}
cp -pr PKG/include/netpbm $RPM_BUILD_ROOT%{_includedir}
cp -p PKG/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p PKG/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
cp -p PKG/man/man5/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

# Install the static-only librle.a
cp -p urt/{rle,rle_config}.h $RPM_BUILD_ROOT%{_includedir}
cp -p urt/librle.a $RPM_BUILD_ROOT%{_libdir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.netpbm-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{CONTRIBUTORS,COPYRIGHT.PATENT,HISTORY,USERDOC}
%attr(755,root,root) %{_libdir}/libnetpbm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetpbm.so.11

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetpbm.so
%{_includedir}/netpbm
%{_mandir}/man3/libnetpbm.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetpbm.a

%files rle-static
%defattr(644,root,root,755)
%{_libdir}/librle.a
%{_includedir}/rle.h
%{_includedir}/rle_config.h

%files progs
%defattr(644,root,root,755)
%doc netpbm.sourceforge.net
%attr(755,root,root) %{_bindir}/411toppm
%attr(755,root,root) %{_bindir}/anytopnm
%attr(755,root,root) %{_bindir}/asciitopgm
%attr(755,root,root) %{_bindir}/atktopbm
%attr(755,root,root) %{_bindir}/avstopam
%attr(755,root,root) %{_bindir}/bioradtopgm
%attr(755,root,root) %{_bindir}/bmptopnm
%attr(755,root,root) %{_bindir}/bmptoppm
%attr(755,root,root) %{_bindir}/brushtopbm
%attr(755,root,root) %{_bindir}/cameratopam
%attr(755,root,root) %{_bindir}/cistopbm
%attr(755,root,root) %{_bindir}/cmuwmtopbm
%attr(755,root,root) %{_bindir}/ddbugtopbm
%attr(755,root,root) %{_bindir}/escp2topbm
%attr(755,root,root) %{_bindir}/eyuvtoppm
%attr(755,root,root) %{_bindir}/fiascotopnm
%attr(755,root,root) %{_bindir}/fitstopnm
%attr(755,root,root) %{_bindir}/fstopgm
%attr(755,root,root) %{_bindir}/g3topbm
%attr(755,root,root) %{_bindir}/gemtopbm
%attr(755,root,root) %{_bindir}/gemtopnm
%attr(755,root,root) %{_bindir}/giftopnm
%attr(755,root,root) %{_bindir}/gouldtoppm
%attr(755,root,root) %{_bindir}/hdifftopam
%attr(755,root,root) %{_bindir}/hipstopgm
%attr(755,root,root) %{_bindir}/hpcdtoppm
%attr(755,root,root) %{_bindir}/icontopbm
%attr(755,root,root) %{_bindir}/ilbmtoppm
%attr(755,root,root) %{_bindir}/imgtoppm
%attr(755,root,root) %{_bindir}/infotopam
%attr(755,root,root) %{_bindir}/jbigtopnm
%attr(755,root,root) %{_bindir}/jpeg2ktopam
%attr(755,root,root) %{_bindir}/jpegtopnm
%attr(755,root,root) %{_bindir}/leaftoppm
%attr(755,root,root) %{_bindir}/lispmtopgm
%attr(755,root,root) %{_bindir}/macptopbm
%attr(755,root,root) %{_bindir}/manweb
%attr(755,root,root) %{_bindir}/mdatopbm
%attr(755,root,root) %{_bindir}/mgrtopbm
%attr(755,root,root) %{_bindir}/mrftopbm
%attr(755,root,root) %{_bindir}/mtvtoppm
%attr(755,root,root) %{_bindir}/neotoppm
%attr(755,root,root) %{_bindir}/palmtopnm
%attr(755,root,root) %{_bindir}/pamaddnoise
%attr(755,root,root) %{_bindir}/pamarith
%attr(755,root,root) %{_bindir}/pambackground
%attr(755,root,root) %{_bindir}/pambayer
%attr(755,root,root) %{_bindir}/pamchannel
%attr(755,root,root) %{_bindir}/pamcomp
%attr(755,root,root) %{_bindir}/pamcrater
%attr(755,root,root) %{_bindir}/pamcut
%attr(755,root,root) %{_bindir}/pamdeinterlace
%attr(755,root,root) %{_bindir}/pamdepth
%attr(755,root,root) %{_bindir}/pamdice
%attr(755,root,root) %{_bindir}/pamditherbw
%attr(755,root,root) %{_bindir}/pamedge
%attr(755,root,root) %{_bindir}/pamendian
%attr(755,root,root) %{_bindir}/pamenlarge
%attr(755,root,root) %{_bindir}/pamexec
%attr(755,root,root) %{_bindir}/pamfile
%attr(755,root,root) %{_bindir}/pamfix
%attr(755,root,root) %{_bindir}/pamfixtrunc
%attr(755,root,root) %{_bindir}/pamflip
%attr(755,root,root) %{_bindir}/pamfunc
%attr(755,root,root) %{_bindir}/pamgauss
%attr(755,root,root) %{_bindir}/pamgradient
%attr(755,root,root) %{_bindir}/pamlookup
%attr(755,root,root) %{_bindir}/pammasksharpen
%attr(755,root,root) %{_bindir}/pammixinterlace
%attr(755,root,root) %{_bindir}/pammosaicknit
%attr(755,root,root) %{_bindir}/pamoil
%attr(755,root,root) %{_bindir}/pampaintspill
%attr(755,root,root) %{_bindir}/pamperspective
%attr(755,root,root) %{_bindir}/pampick
%attr(755,root,root) %{_bindir}/pampop9
%attr(755,root,root) %{_bindir}/pamrecolor
%attr(755,root,root) %{_bindir}/pamrgbatopng
%attr(755,root,root) %{_bindir}/pamrubber
%attr(755,root,root) %{_bindir}/pamscale
%attr(755,root,root) %{_bindir}/pamseq
%attr(755,root,root) %{_bindir}/pamshadedrelief
%attr(755,root,root) %{_bindir}/pamsharpmap
%attr(755,root,root) %{_bindir}/pamsharpness
%attr(755,root,root) %{_bindir}/pamsistoaglyph
%attr(755,root,root) %{_bindir}/pamslice
%attr(755,root,root) %{_bindir}/pamsplit
%attr(755,root,root) %{_bindir}/pamstack
%attr(755,root,root) %{_bindir}/pamstereogram
%attr(755,root,root) %{_bindir}/pamstretch
%attr(755,root,root) %{_bindir}/pamstretch-gen
%attr(755,root,root) %{_bindir}/pamsumm
%attr(755,root,root) %{_bindir}/pamsummcol
%attr(755,root,root) %{_bindir}/pamthreshold
%attr(755,root,root) %{_bindir}/pamtilt
%attr(755,root,root) %{_bindir}/pamtoavs
%attr(755,root,root) %{_bindir}/pamtodjvurle
%attr(755,root,root) %{_bindir}/pamtofits
%attr(755,root,root) %{_bindir}/pamtogif
%attr(755,root,root) %{_bindir}/pamtohdiff
%attr(755,root,root) %{_bindir}/pamtohtmltbl
%attr(755,root,root) %{_bindir}/pamtojpeg2k
%attr(755,root,root) %{_bindir}/pamtompfont
%attr(755,root,root) %{_bindir}/pamtooctaveimg
%attr(755,root,root) %{_bindir}/pamtopam
%attr(755,root,root) %{_bindir}/pamtopdbimg
%attr(755,root,root) %{_bindir}/pamtopfm
%attr(755,root,root) %{_bindir}/pamtopng
%attr(755,root,root) %{_bindir}/pamtopnm
%attr(755,root,root) %{_bindir}/pamtosrf
%attr(755,root,root) %{_bindir}/pamtosvg
%attr(755,root,root) %{_bindir}/pamtotga
%attr(755,root,root) %{_bindir}/pamtotiff
%attr(755,root,root) %{_bindir}/pamtouil
%attr(755,root,root) %{_bindir}/pamtowinicon
%attr(755,root,root) %{_bindir}/pamtoxvmini
%attr(755,root,root) %{_bindir}/pamundice
%attr(755,root,root) %{_bindir}/pamunlookup
%attr(755,root,root) %{_bindir}/pamvalidate
%attr(755,root,root) %{_bindir}/pamwipeout
%attr(755,root,root) %{_bindir}/pamx
%attr(755,root,root) %{_bindir}/pbmclean
%attr(755,root,root) %{_bindir}/pbmlife
%attr(755,root,root) %{_bindir}/pbmmake
%attr(755,root,root) %{_bindir}/pbmmask
%attr(755,root,root) %{_bindir}/pbmminkowski
%attr(755,root,root) %{_bindir}/pbmpage
%attr(755,root,root) %{_bindir}/pbmpscale
%attr(755,root,root) %{_bindir}/pbmreduce
%attr(755,root,root) %{_bindir}/pbmtext
%attr(755,root,root) %{_bindir}/pbmtextps
%attr(755,root,root) %{_bindir}/pbmto10x
%attr(755,root,root) %{_bindir}/pbmto4425
%attr(755,root,root) %{_bindir}/pbmtoascii
%attr(755,root,root) %{_bindir}/pbmtoatk
%attr(755,root,root) %{_bindir}/pbmtobbnbg
%attr(755,root,root) %{_bindir}/pbmtocis
%attr(755,root,root) %{_bindir}/pbmtocmuwm
%attr(755,root,root) %{_bindir}/pbmtodjvurle
%attr(755,root,root) %{_bindir}/pbmtoepsi
%attr(755,root,root) %{_bindir}/pbmtoepson
%attr(755,root,root) %{_bindir}/pbmtoescp2
%attr(755,root,root) %{_bindir}/pbmtog3
%attr(755,root,root) %{_bindir}/pbmtogem
%attr(755,root,root) %{_bindir}/pbmtogo
%attr(755,root,root) %{_bindir}/pbmtoibm23xx
%attr(755,root,root) %{_bindir}/pbmtoicon
%attr(755,root,root) %{_bindir}/pbmtolj
%attr(755,root,root) %{_bindir}/pbmtoln03
%attr(755,root,root) %{_bindir}/pbmtolps
%attr(755,root,root) %{_bindir}/pbmtomacp
%attr(755,root,root) %{_bindir}/pbmtomatrixorbital
%attr(755,root,root) %{_bindir}/pbmtomda
%attr(755,root,root) %{_bindir}/pbmtomgr
%attr(755,root,root) %{_bindir}/pbmtomrf
%attr(755,root,root) %{_bindir}/pbmtonokia
%attr(755,root,root) %{_bindir}/pbmtopgm
%attr(755,root,root) %{_bindir}/pbmtopi3
%attr(755,root,root) %{_bindir}/pbmtopk
%attr(755,root,root) %{_bindir}/pbmtoplot
%attr(755,root,root) %{_bindir}/pbmtoppa
%attr(755,root,root) %{_bindir}/pbmtopsg3
%attr(755,root,root) %{_bindir}/pbmtoptx
%attr(755,root,root) %{_bindir}/pbmtosunicon
%attr(755,root,root) %{_bindir}/pbmtowbmp
%attr(755,root,root) %{_bindir}/pbmtox10bm
%attr(755,root,root) %{_bindir}/pbmtoxbm
%attr(755,root,root) %{_bindir}/pbmtoybm
%attr(755,root,root) %{_bindir}/pbmtozinc
%attr(755,root,root) %{_bindir}/pbmupc
%attr(755,root,root) %{_bindir}/pc1toppm
%attr(755,root,root) %{_bindir}/pcdovtoppm
%attr(755,root,root) %{_bindir}/pcxtoppm
%attr(755,root,root) %{_bindir}/pdbimgtopam
%attr(755,root,root) %{_bindir}/pfmtopam
%attr(755,root,root) %{_bindir}/pgmabel
%attr(755,root,root) %{_bindir}/pgmbentley
%attr(755,root,root) %{_bindir}/pgmcrater
%attr(755,root,root) %{_bindir}/pgmdeshadow
%attr(755,root,root) %{_bindir}/pgmedge
%attr(755,root,root) %{_bindir}/pgmenhance
%attr(755,root,root) %{_bindir}/pgmhist
%attr(755,root,root) %{_bindir}/pgmkernel
%attr(755,root,root) %{_bindir}/pgmmake
%attr(755,root,root) %{_bindir}/pgmmedian
%attr(755,root,root) %{_bindir}/pgmminkowski
%attr(755,root,root) %{_bindir}/pgmmorphconv
%attr(755,root,root) %{_bindir}/pgmnoise
%attr(755,root,root) %{_bindir}/pgmnorm
%attr(755,root,root) %{_bindir}/pgmoil
%attr(755,root,root) %{_bindir}/pgmramp
%attr(755,root,root) %{_bindir}/pgmslice
%attr(755,root,root) %{_bindir}/pgmtexture
%attr(755,root,root) %{_bindir}/pgmtofs
%attr(755,root,root) %{_bindir}/pgmtolispm
%attr(755,root,root) %{_bindir}/pgmtopbm
%attr(755,root,root) %{_bindir}/pgmtopgm
%attr(755,root,root) %{_bindir}/pgmtoppm
%attr(755,root,root) %{_bindir}/pgmtosbig
%attr(755,root,root) %{_bindir}/pgmtost4
%attr(755,root,root) %{_bindir}/pi1toppm
%attr(755,root,root) %{_bindir}/pi3topbm
%attr(755,root,root) %{_bindir}/picttoppm
%attr(755,root,root) %{_bindir}/pjtoppm
%attr(755,root,root) %{_bindir}/pktopbm
%attr(755,root,root) %{_bindir}/pngtopam
%attr(755,root,root) %{_bindir}/pngtopnm
%attr(755,root,root) %{_bindir}/pnmalias
%attr(755,root,root) %{_bindir}/pnmarith
%attr(755,root,root) %{_bindir}/pnmcat
%attr(755,root,root) %{_bindir}/pnmcolormap
%attr(755,root,root) %{_bindir}/pnmcomp
%attr(755,root,root) %{_bindir}/pnmconvol
%attr(755,root,root) %{_bindir}/pnmcrop
%attr(755,root,root) %{_bindir}/pnmcut
%attr(755,root,root) %{_bindir}/pnmdepth
%attr(755,root,root) %{_bindir}/pnmenlarge
%attr(755,root,root) %{_bindir}/pnmfile
%attr(755,root,root) %{_bindir}/pnmflip
%attr(755,root,root) %{_bindir}/pnmgamma
%attr(755,root,root) %{_bindir}/pnmhisteq
%attr(755,root,root) %{_bindir}/pnmhistmap
%attr(755,root,root) %{_bindir}/pnmindex
%attr(755,root,root) %{_bindir}/pnminterp
%attr(755,root,root) %{_bindir}/pnminvert
%attr(755,root,root) %{_bindir}/pnmmargin
%attr(755,root,root) %{_bindir}/pnmmercator
%attr(755,root,root) %{_bindir}/pnmmontage
%attr(755,root,root) %{_bindir}/pnmnlfilt
%attr(755,root,root) %{_bindir}/pnmnoraw
%attr(755,root,root) %{_bindir}/pnmnorm
%attr(755,root,root) %{_bindir}/pnmpad
%attr(755,root,root) %{_bindir}/pnmpaste
%attr(755,root,root) %{_bindir}/pnmpsnr
%attr(755,root,root) %{_bindir}/pnmquant
%attr(755,root,root) %{_bindir}/pnmquantall
%attr(755,root,root) %{_bindir}/pnmremap
%attr(755,root,root) %{_bindir}/pnmrotate
%attr(755,root,root) %{_bindir}/pnmscale
%attr(755,root,root) %{_bindir}/pnmscalefixed
%attr(755,root,root) %{_bindir}/pnmshear
%attr(755,root,root) %{_bindir}/pnmsmooth
%attr(755,root,root) %{_bindir}/pnmsplit
%attr(755,root,root) %{_bindir}/pnmstitch
%attr(755,root,root) %{_bindir}/pnmtile
%attr(755,root,root) %{_bindir}/pnmtoddif
%attr(755,root,root) %{_bindir}/pnmtofiasco
%attr(755,root,root) %{_bindir}/pnmtofits
%attr(755,root,root) %{_bindir}/pnmtojbig
%attr(755,root,root) %{_bindir}/pnmtojpeg
%attr(755,root,root) %{_bindir}/pnmtopalm
%attr(755,root,root) %{_bindir}/pnmtopclxl
%attr(755,root,root) %{_bindir}/pnmtoplainpnm
%attr(755,root,root) %{_bindir}/pnmtopng
%attr(755,root,root) %{_bindir}/pnmtopnm
%attr(755,root,root) %{_bindir}/pnmtops
%attr(755,root,root) %{_bindir}/pnmtorast
%attr(755,root,root) %{_bindir}/pnmtorle
%attr(755,root,root) %{_bindir}/pnmtosgi
%attr(755,root,root) %{_bindir}/pnmtosir
%attr(755,root,root) %{_bindir}/pnmtotiff
%attr(755,root,root) %{_bindir}/pnmtotiffcmyk
%attr(755,root,root) %{_bindir}/pnmtoxwd
%attr(755,root,root) %{_bindir}/ppm3d
%attr(755,root,root) %{_bindir}/ppmbrighten
%attr(755,root,root) %{_bindir}/ppmchange
%attr(755,root,root) %{_bindir}/ppmcie
%attr(755,root,root) %{_bindir}/ppmcolormask
%attr(755,root,root) %{_bindir}/ppmcolors
%attr(755,root,root) %{_bindir}/ppmdcfont
%attr(755,root,root) %{_bindir}/ppmddumpfont
%attr(755,root,root) %{_bindir}/ppmdim
%attr(755,root,root) %{_bindir}/ppmdist
%attr(755,root,root) %{_bindir}/ppmdither
%attr(755,root,root) %{_bindir}/ppmdmkfont
%attr(755,root,root) %{_bindir}/ppmdraw
%attr(755,root,root) %{_bindir}/ppmfade
%attr(755,root,root) %{_bindir}/ppmflash
%attr(755,root,root) %{_bindir}/ppmforge
%attr(755,root,root) %{_bindir}/ppmglobe
%attr(755,root,root) %{_bindir}/ppmhist
%attr(755,root,root) %{_bindir}/ppmlabel
%attr(755,root,root) %{_bindir}/ppmmake
%attr(755,root,root) %{_bindir}/ppmmix
%attr(755,root,root) %{_bindir}/ppmnorm
%attr(755,root,root) %{_bindir}/ppmntsc
%attr(755,root,root) %{_bindir}/ppmpat
%attr(755,root,root) %{_bindir}/ppmquant
%attr(755,root,root) %{_bindir}/ppmquantall
%attr(755,root,root) %{_bindir}/ppmrainbow
%attr(755,root,root) %{_bindir}/ppmrelief
%attr(755,root,root) %{_bindir}/ppmrough
%attr(755,root,root) %{_bindir}/ppmshadow
%attr(755,root,root) %{_bindir}/ppmshift
%attr(755,root,root) %{_bindir}/ppmspread
%attr(755,root,root) %{_bindir}/ppmtoacad
%attr(755,root,root) %{_bindir}/ppmtoapplevol
%attr(755,root,root) %{_bindir}/ppmtoarbtxt
%attr(755,root,root) %{_bindir}/ppmtoascii
%attr(755,root,root) %{_bindir}/ppmtobmp
%attr(755,root,root) %{_bindir}/ppmtoeyuv
%attr(755,root,root) %{_bindir}/ppmtogif
%attr(755,root,root) %{_bindir}/ppmtoicr
%attr(755,root,root) %{_bindir}/ppmtoilbm
%attr(755,root,root) %{_bindir}/ppmtojpeg
%attr(755,root,root) %{_bindir}/ppmtoleaf
%attr(755,root,root) %{_bindir}/ppmtolj
%attr(755,root,root) %{_bindir}/ppmtomap
%attr(755,root,root) %{_bindir}/ppmtomitsu
%attr(755,root,root) %{_bindir}/ppmtompeg
%attr(755,root,root) %{_bindir}/ppmtoneo
%attr(755,root,root) %{_bindir}/ppmtopcx
%attr(755,root,root) %{_bindir}/ppmtopgm
%attr(755,root,root) %{_bindir}/ppmtopi1
%attr(755,root,root) %{_bindir}/ppmtopict
%attr(755,root,root) %{_bindir}/ppmtopj
%attr(755,root,root) %{_bindir}/ppmtopjxl
%attr(755,root,root) %{_bindir}/ppmtoppm
%attr(755,root,root) %{_bindir}/ppmtopuzz
%attr(755,root,root) %{_bindir}/ppmtorgb3
%attr(755,root,root) %{_bindir}/ppmtosixel
%attr(755,root,root) %{_bindir}/ppmtospu
%attr(755,root,root) %{_bindir}/ppmtoterm
%attr(755,root,root) %{_bindir}/ppmtotga
%attr(755,root,root) %{_bindir}/ppmtouil
%attr(755,root,root) %{_bindir}/ppmtowinicon
%attr(755,root,root) %{_bindir}/ppmtoxpm
%attr(755,root,root) %{_bindir}/ppmtoyuv
%attr(755,root,root) %{_bindir}/ppmtoyuvsplit
%attr(755,root,root) %{_bindir}/ppmtv
%attr(755,root,root) %{_bindir}/ppmwheel
%attr(755,root,root) %{_bindir}/psidtopgm
%attr(755,root,root) %{_bindir}/qrttoppm
%attr(755,root,root) %{_bindir}/rasttopnm
%attr(755,root,root) %{_bindir}/rawtopgm
%attr(755,root,root) %{_bindir}/rawtoppm
%attr(755,root,root) %{_bindir}/rgb3toppm
%attr(755,root,root) %{_bindir}/rlatopam
%attr(755,root,root) %{_bindir}/rletopnm
%attr(755,root,root) %{_bindir}/sbigtopgm
%attr(755,root,root) %{_bindir}/sgitopnm
%attr(755,root,root) %{_bindir}/sirtopnm
%attr(755,root,root) %{_bindir}/sldtoppm
%attr(755,root,root) %{_bindir}/spctoppm
%attr(755,root,root) %{_bindir}/spottopgm
%attr(755,root,root) %{_bindir}/sputoppm
%attr(755,root,root) %{_bindir}/srftopam
%attr(755,root,root) %{_bindir}/st4topgm
%attr(755,root,root) %{_bindir}/sunicontopnm
%attr(755,root,root) %{_bindir}/svgtopam
%attr(755,root,root) %{_bindir}/tgatoppm
%attr(755,root,root) %{_bindir}/thinkjettopbm
%attr(755,root,root) %{_bindir}/tifftopnm
%attr(755,root,root) %{_bindir}/wbmptopbm
%attr(755,root,root) %{_bindir}/winicontopam
%attr(755,root,root) %{_bindir}/winicontoppm
%attr(755,root,root) %{_bindir}/xbmtopbm
%attr(755,root,root) %{_bindir}/ximtoppm
%attr(755,root,root) %{_bindir}/xpmtoppm
%attr(755,root,root) %{_bindir}/xvminitoppm
%attr(755,root,root) %{_bindir}/xwdtopnm
%attr(755,root,root) %{_bindir}/ybmtopbm
%attr(755,root,root) %{_bindir}/yuvsplittoppm
%attr(755,root,root) %{_bindir}/yuvtoppm
%attr(755,root,root) %{_bindir}/yuy2topam
%attr(755,root,root) %{_bindir}/zeisstopnm
%{_mandir}/man1/411toppm.1*
%{_mandir}/man1/anytopnm.1*
%{_mandir}/man1/asciitopgm.1*
%{_mandir}/man1/atktopbm.1*
%{_mandir}/man1/avstopam.1*
%{_mandir}/man1/bioradtopgm.1*
%{_mandir}/man1/bmptopnm.1*
%{_mandir}/man1/brushtopbm.1*
%{_mandir}/man1/cameratopam.1*
%{_mandir}/man1/cistopbm.1*
%{_mandir}/man1/cmuwmtopbm.1*
%{_mandir}/man1/ddbugtopbm.1*
%{_mandir}/man1/escp2topbm.1*
%{_mandir}/man1/eyuvtoppm.1*
%{_mandir}/man1/fiascotopnm.1*
%{_mandir}/man1/fitstopnm.1*
%{_mandir}/man1/fstopgm.1*
%{_mandir}/man1/g3topbm.1*
%{_mandir}/man1/gemtopnm.1*
%{_mandir}/man1/giftopnm.1*
%{_mandir}/man1/gouldtoppm.1*
%{_mandir}/man1/hdifftopam.1*
%{_mandir}/man1/hipstopgm.1*
%{_mandir}/man1/hpcdtoppm.1*
%{_mandir}/man1/ilbmtoppm.1*
%{_mandir}/man1/imgtoppm.1*
%{_mandir}/man1/infotopam.1*
%{_mandir}/man1/jbigtopnm.1*
%{_mandir}/man1/jpeg2ktopam.1*
%{_mandir}/man1/jpegtopnm.1*
%{_mandir}/man1/leaftoppm.1*
%{_mandir}/man1/lispmtopgm.1*
%{_mandir}/man1/macptopbm.1*
%{_mandir}/man1/manweb.1*
%{_mandir}/man1/mdatopbm.1*
%{_mandir}/man1/mgrtopbm.1*
%{_mandir}/man1/mrftopbm.1*
%{_mandir}/man1/mtvtoppm.1*
%{_mandir}/man1/neotoppm.1*
%{_mandir}/man1/palmtopnm.1*
%{_mandir}/man1/pamaddnoise.1*
%{_mandir}/man1/pamarith.1*
%{_mandir}/man1/pambackground.1*
%{_mandir}/man1/pambayer.1*
%{_mandir}/man1/pamchannel.1*
%{_mandir}/man1/pamcomp.1*
%{_mandir}/man1/pamcrater.1*
%{_mandir}/man1/pamcut.1*
%{_mandir}/man1/pamdeinterlace.1*
%{_mandir}/man1/pamdepth.1*
%{_mandir}/man1/pamdice.1*
%{_mandir}/man1/pamditherbw.1*
%{_mandir}/man1/pamedge.1*
%{_mandir}/man1/pamendian.1*
%{_mandir}/man1/pamenlarge.1*
%{_mandir}/man1/pamexec.1*
%{_mandir}/man1/pamfile.1*
%{_mandir}/man1/pamfix.1*
%{_mandir}/man1/pamfixtrunc.1*
%{_mandir}/man1/pamflip.1*
%{_mandir}/man1/pamfunc.1*
%{_mandir}/man1/pamgauss.1*
%{_mandir}/man1/pamgradient.1*
%{_mandir}/man1/pamlookup.1*
%{_mandir}/man1/pammasksharpen.1*
%{_mandir}/man1/pammixinterlace.1*
%{_mandir}/man1/pammosaicknit.1*
%{_mandir}/man1/pamoil.1*
%{_mandir}/man1/pampaintspill.1*
%{_mandir}/man1/pamperspective.1*
%{_mandir}/man1/pampick.1*
%{_mandir}/man1/pampop9.1*
%{_mandir}/man1/pamrecolor.1*
%{_mandir}/man1/pamrubber.1*
%{_mandir}/man1/pamscale.1*
%{_mandir}/man1/pamseq.1*
%{_mandir}/man1/pamshadedrelief.1*
%{_mandir}/man1/pamsharpmap.1*
%{_mandir}/man1/pamsharpness.1*
%{_mandir}/man1/pamsistoaglyph.1*
%{_mandir}/man1/pamslice.1*
%{_mandir}/man1/pamsplit.1*
%{_mandir}/man1/pamstack.1*
%{_mandir}/man1/pamstereogram.1*
%{_mandir}/man1/pamstretch-gen.1*
%{_mandir}/man1/pamstretch.1*
%{_mandir}/man1/pamsumm.1*
%{_mandir}/man1/pamsummcol.1*
%{_mandir}/man1/pamthreshold.1*
%{_mandir}/man1/pamtilt.1*
%{_mandir}/man1/pamtoavs.1*
%{_mandir}/man1/pamtodjvurle.1*
%{_mandir}/man1/pamtofits.1*
%{_mandir}/man1/pamtogif.1*
%{_mandir}/man1/pamtohdiff.1*
%{_mandir}/man1/pamtohtmltbl.1*
%{_mandir}/man1/pamtojpeg2k.1*
%{_mandir}/man1/pamtompfont.1*
%{_mandir}/man1/pamtooctaveimg.1*
%{_mandir}/man1/pamtopam.1*
%{_mandir}/man1/pamtopdbimg.1*
%{_mandir}/man1/pamtopfm.1*
%{_mandir}/man1/pamtopng.1*
%{_mandir}/man1/pamtopnm.1*
%{_mandir}/man1/pamtosrf.1*
%{_mandir}/man1/pamtosvg.1*
%{_mandir}/man1/pamtotga.1*
%{_mandir}/man1/pamtotiff.1*
%{_mandir}/man1/pamtouil.1*
%{_mandir}/man1/pamtowinicon.1*
%{_mandir}/man1/pamtoxvmini.1*
%{_mandir}/man1/pamundice.1*
%{_mandir}/man1/pamunlookup.1*
%{_mandir}/man1/pamvalidate.1*
%{_mandir}/man1/pamwipeout.1*
%{_mandir}/man1/pamx.1*
%{_mandir}/man1/pbmclean.1*
%{_mandir}/man1/pbmlife.1*
%{_mandir}/man1/pbmmake.1*
%{_mandir}/man1/pbmmask.1*
%{_mandir}/man1/pbmminkowski.1*
%{_mandir}/man1/pbmpage.1*
%{_mandir}/man1/pbmpscale.1*
%{_mandir}/man1/pbmreduce.1*
%{_mandir}/man1/pbmtext.1*
%{_mandir}/man1/pbmtextps.1*
%{_mandir}/man1/pbmto10x.1*
%{_mandir}/man1/pbmto4425.1*
%{_mandir}/man1/pbmtoascii.1*
%{_mandir}/man1/pbmtoatk.1*
%{_mandir}/man1/pbmtobbnbg.1*
%{_mandir}/man1/pbmtocis.1*
%{_mandir}/man1/pbmtocmuwm.1*
%{_mandir}/man1/pbmtodjvurle.1*
%{_mandir}/man1/pbmtoepsi.1*
%{_mandir}/man1/pbmtoepson.1*
%{_mandir}/man1/pbmtoescp2.1*
%{_mandir}/man1/pbmtog3.1*
%{_mandir}/man1/pbmtogem.1*
%{_mandir}/man1/pbmtogo.1*
%{_mandir}/man1/pbmtoibm23xx.1*
%{_mandir}/man1/pbmtolj.1*
%{_mandir}/man1/pbmtoln03.1*
%{_mandir}/man1/pbmtolps.1*
%{_mandir}/man1/pbmtomacp.1*
%{_mandir}/man1/pbmtomatrixorbital.1*
%{_mandir}/man1/pbmtomda.1*
%{_mandir}/man1/pbmtomgr.1*
%{_mandir}/man1/pbmtomrf.1*
%{_mandir}/man1/pbmtonokia.1*
%{_mandir}/man1/pbmtopgm.1*
%{_mandir}/man1/pbmtopi3.1*
%{_mandir}/man1/pbmtopk.1*
%{_mandir}/man1/pbmtoplot.1*
%{_mandir}/man1/pbmtoppa.1*
%{_mandir}/man1/pbmtopsg3.1*
%{_mandir}/man1/pbmtoptx.1*
%{_mandir}/man1/pbmtosunicon.1*
%{_mandir}/man1/pbmtowbmp.1*
%{_mandir}/man1/pbmtox10bm.1*
%{_mandir}/man1/pbmtoxbm.1*
%{_mandir}/man1/pbmtoybm.1*
%{_mandir}/man1/pbmtozinc.1*
%{_mandir}/man1/pbmupc.1*
%{_mandir}/man1/pc1toppm.1*
%{_mandir}/man1/pcdovtoppm.1*
%{_mandir}/man1/pcxtoppm.1*
%{_mandir}/man1/pdbimgtopam.1*
%{_mandir}/man1/pfmtopam.1*
%{_mandir}/man1/pgmabel.1*
%{_mandir}/man1/pgmbentley.1*
%{_mandir}/man1/pgmcrater.1*
%{_mandir}/man1/pgmdeshadow.1*
%{_mandir}/man1/pgmenhance.1*
%{_mandir}/man1/pgmhist.1*
%{_mandir}/man1/pgmkernel.1*
%{_mandir}/man1/pgmmake.1*
%{_mandir}/man1/pgmmedian.1*
%{_mandir}/man1/pgmminkowski.1*
%{_mandir}/man1/pgmmorphconv.1*
%{_mandir}/man1/pgmnoise.1*
%{_mandir}/man1/pgmramp.1*
%{_mandir}/man1/pgmtexture.1*
%{_mandir}/man1/pgmtofs.1*
%{_mandir}/man1/pgmtolispm.1*
%{_mandir}/man1/pgmtopbm.1*
%{_mandir}/man1/pgmtopgm.1*
%{_mandir}/man1/pgmtoppm.1*
%{_mandir}/man1/pgmtosbig.1*
%{_mandir}/man1/pgmtost4.1*
%{_mandir}/man1/pi1toppm.1*
%{_mandir}/man1/pi3topbm.1*
%{_mandir}/man1/picttoppm.1*
%{_mandir}/man1/pjtoppm.1*
%{_mandir}/man1/pktopbm.1*
%{_mandir}/man1/pngtopam.1*
%{_mandir}/man1/pnmalias.1*
%{_mandir}/man1/pnmcat.1*
%{_mandir}/man1/pnmcolormap.1*
%{_mandir}/man1/pnmconvol.1*
%{_mandir}/man1/pnmcrop.1*
%{_mandir}/man1/pnmflip.1*
%{_mandir}/man1/pnmgamma.1*
%{_mandir}/man1/pnmhisteq.1*
%{_mandir}/man1/pnmhistmap.1*
%{_mandir}/man1/pnmindex.1*
%{_mandir}/man1/pnminvert.1*
%{_mandir}/man1/pnmmargin.1*
%{_mandir}/man1/pnmmercator.1*
%{_mandir}/man1/pnmmontage.1*
%{_mandir}/man1/pnmnlfilt.1*
%{_mandir}/man1/pnmnorm.1*
%{_mandir}/man1/pnmpad.1*
%{_mandir}/man1/pnmpaste.1*
%{_mandir}/man1/pnmpsnr.1*
%{_mandir}/man1/pnmquant.1*
%{_mandir}/man1/pnmquantall.1*
%{_mandir}/man1/pnmremap.1*
%{_mandir}/man1/pnmrotate.1*
%{_mandir}/man1/pnmscalefixed.1*
%{_mandir}/man1/pnmshear.1*
%{_mandir}/man1/pnmsmooth.1*
%{_mandir}/man1/pnmstitch.1*
%{_mandir}/man1/pnmtile.1*
%{_mandir}/man1/pnmtoddif.1*
%{_mandir}/man1/pnmtofiasco.1*
%{_mandir}/man1/pnmtojbig.1*
%{_mandir}/man1/pnmtojpeg.1*
%{_mandir}/man1/pnmtopalm.1*
%{_mandir}/man1/pnmtopclxl.1*
%{_mandir}/man1/pnmtoplainpnm.1*
%{_mandir}/man1/pnmtopng.1*
%{_mandir}/man1/pnmtops.1*
%{_mandir}/man1/pnmtorast.1*
%{_mandir}/man1/pnmtorle.1*
%{_mandir}/man1/pnmtosgi.1*
%{_mandir}/man1/pnmtosir.1*
%{_mandir}/man1/pnmtotiffcmyk.1*
%{_mandir}/man1/pnmtoxwd.1*
%{_mandir}/man1/ppm3d.1*
%{_mandir}/man1/ppmbrighten.1*
%{_mandir}/man1/ppmchange.1*
%{_mandir}/man1/ppmcie.1*
%{_mandir}/man1/ppmcolormask.1*
%{_mandir}/man1/ppmcolors.1*
%{_mandir}/man1/ppmdcfont.1*
%{_mandir}/man1/ppmddumpfont.1*
%{_mandir}/man1/ppmdim.1*
%{_mandir}/man1/ppmdist.1*
%{_mandir}/man1/ppmdither.1*
%{_mandir}/man1/ppmdmkfont.1*
%{_mandir}/man1/ppmdraw.1*
%{_mandir}/man1/ppmfade.1*
%{_mandir}/man1/ppmflash.1*
%{_mandir}/man1/ppmforge.1*
%{_mandir}/man1/ppmglobe.1*
%{_mandir}/man1/ppmhist.1*
%{_mandir}/man1/ppmlabel.1*
%{_mandir}/man1/ppmmake.1*
%{_mandir}/man1/ppmmix.1*
%{_mandir}/man1/ppmntsc.1*
%{_mandir}/man1/ppmpat.1*
%{_mandir}/man1/ppmquant.1*
%{_mandir}/man1/ppmrainbow.1*
%{_mandir}/man1/ppmrelief.1*
%{_mandir}/man1/ppmrough.1*
%{_mandir}/man1/ppmshadow.1*
%{_mandir}/man1/ppmshift.1*
%{_mandir}/man1/ppmspread.1*
%{_mandir}/man1/ppmtoacad.1*
%{_mandir}/man1/ppmtoapplevol.1*
%{_mandir}/man1/ppmtoarbtxt.1*
%{_mandir}/man1/ppmtoascii.1*
%{_mandir}/man1/ppmtobmp.1*
%{_mandir}/man1/ppmtoeyuv.1*
%{_mandir}/man1/ppmtogif.1*
%{_mandir}/man1/ppmtoicr.1*
%{_mandir}/man1/ppmtoilbm.1*
%{_mandir}/man1/ppmtoleaf.1*
%{_mandir}/man1/ppmtolj.1*
%{_mandir}/man1/ppmtomap.1*
%{_mandir}/man1/ppmtomitsu.1*
%{_mandir}/man1/ppmtompeg.1*
%{_mandir}/man1/ppmtoneo.1*
%{_mandir}/man1/ppmtopcx.1*
%{_mandir}/man1/ppmtopgm.1*
%{_mandir}/man1/ppmtopi1.1*
%{_mandir}/man1/ppmtopict.1*
%{_mandir}/man1/ppmtopj.1*
%{_mandir}/man1/ppmtopjxl.1*
%{_mandir}/man1/ppmtoppm.1*
%{_mandir}/man1/ppmtopuzz.1*
%{_mandir}/man1/ppmtorgb3.1*
%{_mandir}/man1/ppmtosixel.1*
%{_mandir}/man1/ppmtospu.1*
%{_mandir}/man1/ppmtoterm.1*
%{_mandir}/man1/ppmtowinicon.1*
%{_mandir}/man1/ppmtoxpm.1*
%{_mandir}/man1/ppmtoyuv.1*
%{_mandir}/man1/ppmtoyuvsplit.1*
%{_mandir}/man1/ppmtv.1*
%{_mandir}/man1/ppmwheel.1*
%{_mandir}/man1/psidtopgm.1*
%{_mandir}/man1/qrttoppm.1*
%{_mandir}/man1/rasttopnm.1*
%{_mandir}/man1/rawtopgm.1*
%{_mandir}/man1/rawtoppm.1*
%{_mandir}/man1/rgb3toppm.1*
%{_mandir}/man1/rlatopam.1*
%{_mandir}/man1/rletopnm.1*
%{_mandir}/man1/sbigtopgm.1*
%{_mandir}/man1/sgitopnm.1*
%{_mandir}/man1/sirtopnm.1*
%{_mandir}/man1/sldtoppm.1*
%{_mandir}/man1/spctoppm.1*
%{_mandir}/man1/spottopgm.1*
%{_mandir}/man1/sputoppm.1*
%{_mandir}/man1/srftopam.1*
%{_mandir}/man1/st4topgm.1*
%{_mandir}/man1/sunicontopnm.1*
%{_mandir}/man1/svgtopam.1*
%{_mandir}/man1/tgatoppm.1*
%{_mandir}/man1/thinkjettopbm.1*
%{_mandir}/man1/tifftopnm.1*
%{_mandir}/man1/wbmptopbm.1*
%{_mandir}/man1/winicontopam.1*
%{_mandir}/man1/winicontoppm.1*
%{_mandir}/man1/xbmtopbm.1*
%{_mandir}/man1/ximtoppm.1*
%{_mandir}/man1/xpmtoppm.1*
%{_mandir}/man1/xvminitoppm.1*
%{_mandir}/man1/xwdtopnm.1*
%{_mandir}/man1/ybmtopbm.1*
%{_mandir}/man1/yuvsplittoppm.1*
%{_mandir}/man1/yuvtoppm.1*
%{_mandir}/man1/yuy2topam.1*
%{_mandir}/man1/zeisstopnm.1*
%{_mandir}/man5/pam.5*
%{_mandir}/man5/pbm.5*
%{_mandir}/man5/pgm.5*
%{_mandir}/man5/pnm.5*
%{_mandir}/man5/ppm.5*
%lang(fi) %{_mandir}/fi/man1/*.1*
%lang(pl) %{_mandir}/pl/man1/*.1*
%lang(pl) %{_mandir}/pl/man5/p?m.5*

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
