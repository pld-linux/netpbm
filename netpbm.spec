#
# Conditional build:
# _without_svga		- don't build ppmsvgalib tool
#
%ifnarch %{ix86} alpha
%define	_without_svga	1
%endif
Summary:	A library for handling different graphics file formats
Summary(pl):	Biblioteki do obsЁugi rС©nych formatСw graficznych
Summary(pt_BR):	Ferramentas para manipular arquivos graficos nos formatos suportados netpbm
Summary(ru):	Набор библиотек для работы с различными графическими файлами
Summary(uk):	Наб╕р б╕бл╕отек для роботи з р╕зними граф╕чними файлами
Name:		netpbm
Version:	9.25
Release:	3
License:	Freeware
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	cb8036f3649c93cf51ee377971ddbf1c
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	8fb174f8da02ea01bf72a9dc61be10f1
Patch0:		%{name}-Makefile.common.patch
Patch1:		%{name}-security-CAN-2003-0924-VU#378049-VU#630433.patch
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	jbigkit-devel
BuildRequires:	perl
%{!?_without_svga:BuildRequires:	svgalib-devel}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libgr

%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%description -l pl
Pakiet netpbm zawiera biblioteki funkcji obsЁuguj╠cych rС©ne formaty
graficzne, w tym .pbm, .pgm, .pnm, .ppm.

%description -l pt_BR
O pacote netpbm contИm bibliotecas de funГУes que suportam programas
para manipular vАrios formatos grАficos, incluindo .pbm (ortable
bitmaps), .pgm (portable graymaps), .pnm (portable anymaps), .ppm
(portable pixmaps) e outros

%description -l ru
Набор библиотек для обработки графических файлов различных форматов
включая FBM, PBM, PGM, PNM, PPM и REL.

%description -l uk
Наб╕р б╕бл╕отек для обробки граф╕чних файл╕в р╕зних формат╕в,
включаючи FBM, PBM, PGM, PNM, PPM та REL.

%package devel
Summary:	Development tools for programs which will use the netpbm libraries
Summary(pl):	Biblioteka netpbm - czЙ╤Ф dla programistСw
Summary(pt_BR):	Arquivos de desenvolvimento usados para libnetpbm
Summary(ru):	Хедеры и библиотеки для разработки программ, использующих netpbm
Summary(uk):	Хедери та б╕бл╕отеки для розробки програм, що використовують netpbm
Group:		Development/Libraries
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
Pakiet netpbm-devel zawiera pliki nagЁСwkowe i dokumentacjЙ dla
programistСw do tworzenia programСw obsЁuguj╠cych formaty graficzne
wspierane przez netpbm.

%description devel -l pt_BR
The netpbm-devel package contains the header files and programmer's
documentation for developing programs which can handle the various
graphics file formats supported by the netpbm libraries.

Install netpbm-devel if you want to develop programs for handling the
graphics file formats supported by the netpbm libraries. You'll also
need to have the netpbm package installed.

%description devel -l ru
Этот пакет содержит все необходимое для разработки программ,
работающих с графическими файлами в форматах, поддерживаемых netpbm.

%description devel -l uk
Цей пакет м╕стить все необх╕дне для розробки програм, що працюють з
граф╕чними файлами в форматах, що ╖х п╕дтриму╓ netpbm.

%package static
Summary:	Static netpbm libraries
Summary(pl):	Statyczne biblioteki netpbm
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libnetpbm
Summary(ru):	Статическая библиотека для программирования с netpbm
Summary(uk):	Статична б╕бл╕отека для програмування з netpbm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libgr-static

%description static
Static netpbm libraries.

%description static -l pl
Statyczne biblioteki netpbm.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libnetpbm.

%description static -l ru
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих netpbm.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для написання
програм, що використовують netpbm.

%package rle-static
Summary:	Limited rle library
Summary(pl):	Okrojona biblioteka rle
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	urt-static

%description rle-static
Limited version of rle library from netpbm.

%description rle-static -l pl
Okrojona wersja biblioteki rle z netpbm.

%package progs
Summary:	Tools for manipulating graphics files in netpbm supported formats
Summary(pl):	NarzЙdzia do konwersji plikСw graficznych
Summary(ru):	Утилиты манипулирования файлами форматов, поддерживаемых netpbm
Summary(uk):	Утил╕ти ман╕пулювання файлами формат╕в, п╕дтримуваних netpbm
Group:		Applications/Graphics
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
Pakiet netpbm-progs zawiera programy konwertuj╠ce pliki graficzne do
oraz z formatСw obsЁugiwanych przez biblioteki netpbm.

%description progs -l ru
Этот пакет включает разнообразные утилиты для работы с графическими
файлами в форматах, поддерживаемых netpbm.

%description progs -l uk
Цей пакет м╕стить р╕зноман╕тн╕ утил╕ти для роботи з граф╕чним файлами
в форматах, п╕дтримуваних netpbm.

%package ppmsvgalib
Summary:	ppmsvgalib - display PPM image on Linux console using svgalib
Summary(pl):	ppmsvgalib - wy╤wietlanie obrazkСw PPM na konsoli przy u©yciu svgalib
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description ppmsvgalib
ppmsvgalib - display PPM image on Linux console using svgalib.

%description ppmsvgalib -l pl
ppmsvgalib - wy╤wietlanie obrazkСw PPM na konsoli linuksowej przy
u©yciu svgalib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -fPIC" \
	JBIGHDR_DIR=%{_includedir} \
	JPEGHDR_DIR=%{_includedir} \
	PNGHDR_DIR=%{_includedir} \
	TIFFHDR_DIR=%{_includedir} \
	JBIGLIB_DIR=%{_libdir} \
	JPEGLIB_DIR=%{_libdir} \
	PNGLIB_DIR=%{_libdir} \
	TIFFLIB_DIR=%{_libdir} << EOF
gnu
regular
shared
yes
%{_prefix}
bin
lib
lib
include
man
%{?_without_svga:NONE}%{!?_without_svga:/usr/lib}
EOF

%install
rm -rf $RPM_BUILD_ROOT

#	JBIGINC_DIR=$RPM_BUILD_ROOT%{_includedir} \
#	JPEGINC_DIR=$RPM_BUILD_ROOT%{_includedir} \
#	PNGINC_DIR=$RPM_BUILD_ROOT%{_includedir} \
#	TIFFINC_DIR=$RPM_BUILD_ROOT%{_includedir}

PATH="`pwd`:${PATH}" \
%{__make} install \
	JBIGLIB_DIR=%{_libdir} \
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
install pbm/pbm.h $RPM_BUILD_ROOT%{_includedir}
install pbm/pm.h $RPM_BUILD_ROOT%{_includedir}
install pm_config.h $RPM_BUILD_ROOT%{_includedir}
install pgm/pgm.h $RPM_BUILD_ROOT%{_includedir}
install pnm/pnm.h $RPM_BUILD_ROOT%{_includedir}
install ppm/ppm.h $RPM_BUILD_ROOT%{_includedir}
install shhopt/shhopt.h $RPM_BUILD_ROOT%{_includedir}

# Install the static-only librle.a
install urt/{rle,rle_config}.h $RPM_BUILD_ROOT%{_includedir}
install urt/librle.a $RPM_BUILD_ROOT%{_libdir}

# Fixup symlinks.
ln -sf gemtopnm $RPM_BUILD_ROOT%{_bindir}/gemtopbm
ln -sf pnmtoplainpnm $RPM_BUILD_ROOT%{_bindir}/pnmnoraw

# Fixup perl paths in the two scripts that require it.
perl -pi -e 's^/bin/perl^%{__perl}^' \
	$RPM_BUILD_ROOT%{_bindir}/{ppmfade,ppmshadow}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc COPYRIGHT.PATENT HISTORY README
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libp*.a

%files rle-static
%defattr(644,root,root,755)
%{_libdir}/librle.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
%lang(fi) %{_mandir}/fi/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
%{!?_without_svga:%exclude %{_bindir}/ppmsvgalib}
%{!?_without_svga:%exclude %{_mandir}/man1/ppmsvgalib.1*}

%if 0%{!?_without_svga:1}
%files ppmsvgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ppmsvgalib
%{_mandir}/man1/ppmsvgalib.1*
%endif
