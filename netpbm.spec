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
Version:	10.86.47
Release:	1
License:	Freeware
Group:		Libraries
#  svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/stable netpbm-%{version} (where version from doc/HISTORY)
#  svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/userguide netpbm-%{version}/userguide
Source0:	https://downloads.sourceforge.net/netpbm/%{name}-%{version}.tgz
# Source0-md5:	1336b64047687f65f1257b668b48f6b4
# svn export https://netpbm.svn.sourceforge.net/svnroot/netpbm/userguide
# tar cJf netpbm-userguide-YYYYMMDD.tar.xz userguide
Source1:	%{name}-userguide-20250927.tar.xz
# Source1-md5:	ced05a4777ec29a28f8b0bb72f8a0dde
Patch0:		%{name}-make.patch
Patch1:		gcc15.patch
Patch2:		includes.patch
Patch3:		%{name}-as-needed.patch
URL:		https://netpbm.sourceforge.net/
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
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Obsoletes:	libgr < 3
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
Obsoletes:	libgr-devel < 3

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
Obsoletes:	libgr-static < 3

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
Obsoletes:	libgr-progs < 3

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
Obsoletes:	libgr-progs < 3
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
%setup -q -a1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

cp -p config.mk.in config.mk
cat >>config.mk <<EOF
# variables handled by interactive configure
DEFAULT_TARGET = nonmerge
NETPBMLIBTYPE=unixshared
NETPBMLIBSUFFIX=so
STATICLIB_TOO=Y
CFLAGS = %{rpmcflags} %{rpmcppflags} -fPIC -ffast-math -pedantic -fno-common -Wall -Wno-uninitialized -Wmissing-declarations -Wimplicit -Wwrite-strings -Wmissing-prototypes -Wundef -Wno-unknown-pragmas -Wno-strict-overflow
CFLAGS_MERGE = -Wno-missing-declarations -Wno-missing-prototypes
LDRELOC = ld --reloc
LINKER_CAN_DO_EXPLICIT_LIBRARY=Y
LINKERISCOMPILER = Y
CFLAGS_SHLIB += -fPIC
TIFFLIB = libtiff.so
JPEGLIB = libjpeg.so
PNGHDR_DIR = USE_PKG_CONFIG.a
PNGLIB = USE_PKG_CONFIG.a
ZLIB = libz.so
X11HDR_DIR = USE_PKGCONFIG.a
X11LIB = USE_PKGCONFIG.a
LINUXSVGALIB = %{?with_svga:libvga.so}%{!?with_svga:NONE}
# online is http://netpbm.sourceforge.net/doc/
NETPBM_DOCURL = %{_docdir}/%{name}-%{version}/userguide/
# additional for PLD
CC = %{__cc}
LDFLAGS = %{rpmldflags}
JASPERHDR_DIR =
JASPERLIB = -ljasper
JBIGHDR_DIR =
JBIGLIB = -ljbig
EOF

%build
# it appends defines to pm_config.h twice if -j > 1
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

rm -rf PKG
%{__make} -j1 package \
	pkgdir=$(pwd)/PKG

cp -dfp PKG/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -dfp PKG/lib/* $RPM_BUILD_ROOT%{_libdir}
cp -p PKG/staticlink/*.a $RPM_BUILD_ROOT%{_libdir}
cp -pr PKG/include/netpbm $RPM_BUILD_ROOT%{_includedir}

# Install the static-only librle.a
cp -p urt/{rle,rle_config}.h $RPM_BUILD_ROOT%{_includedir}
cp -p urt/librle.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{CONTRIBUTORS,COPYRIGHT.PATENT,HISTORY,USERDOC}
%attr(755,root,root) %{_libdir}/libnetpbm.so.*.*
%ghost %{_libdir}/libnetpbm.so.11

%files devel
%defattr(644,root,root,755)
%{_libdir}/libnetpbm.so
%{_includedir}/netpbm

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
%doc userguide
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
%attr(755,root,root) %{_bindir}/pamaltsat
%attr(755,root,root) %{_bindir}/pamarith
%attr(755,root,root) %{_bindir}/pambackground
%attr(755,root,root) %{_bindir}/pambayer
%attr(755,root,root) %{_bindir}/pambrighten
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
%attr(755,root,root) %{_bindir}/pamfind
%attr(755,root,root) %{_bindir}/pamfix
%attr(755,root,root) %{_bindir}/pamfixtrunc
%attr(755,root,root) %{_bindir}/pamflip
%attr(755,root,root) %{_bindir}/pamfunc
%attr(755,root,root) %{_bindir}/pamgauss
%attr(755,root,root) %{_bindir}/pamgetcolor
%attr(755,root,root) %{_bindir}/pamgradient
%attr(755,root,root) %{_bindir}/pamhue
%attr(755,root,root) %{_bindir}/pamlevels
%attr(755,root,root) %{_bindir}/pamlookup
%attr(755,root,root) %{_bindir}/pammasksharpen
%attr(755,root,root) %{_bindir}/pammixinterlace
%attr(755,root,root) %{_bindir}/pammixmulti
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
%attr(755,root,root) %{_bindir}/pamtable
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
%attr(755,root,root) %{_bindir}/pamtris
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
%attr(755,root,root) %{_bindir}/pcdindex
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

%files progs-pstopnm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pstopnm

%if %{with svga}
%files ppmsvgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppmsvgalib
%endif
