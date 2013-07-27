Summary:	Renderer for User Interfaces in Ncurses library
Summary(pl.UTF-8):	Biblioteka renderująca interfejsy użytkownika przy użyciu ncurses
Name:		libruin
Version:	0.2.0
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/libruin/%{name}-%{version}.tar.gz
# Source0-md5:	880ebec675f165a7fc0b80a2aae98b72
Patch0:		%{name}-make.patch
URL:		http://www.nongnu.org/libruin/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	guile-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires:	glib2 >= 1:2.28.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libRUIN is a Renderer for User Interfaces in Ncurses. It is a library
that can be embedded in arbitrary applications that allows developers
to design user interfaces in any of several XML dialects that are
suitable for interface mark-up and will display these interfaces and
manage input handling for them using the Ncurses terminal control
library. 

%description -l pl.UTF-8
libRUIN (Renderer for User Interface in Ncurses) to biblioteka
renderująca interfejsy użytkownika przy użyciu biblioteki ncurses.
Może być osadzona w dowolnej aplikacji, pozwalając programistom
projektować interfejsy użytkownika w jednym z kilku dialektów XML-a,
nadających się jako znaczniki dla interfejsu. Biblioteka wyświetla
interfejsy i zarządza obsługą wejścia przy użyciu biblioteki
sterującej terminalem ncurses.

%package devel
Summary:	Header files for libRUIN library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libRUIN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.28.0
Requires:	guile-devel >= 2.0
Requires:	ncurses-devel

%description devel
Header files for libRUIN library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libRUIN.

%package static
Summary:	Static libRUIN library
Summary(pl.UTF-8):	Statyczna biblioteka libRUIN
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libRUIN library.

%description static -l pl.UTF-8
Statyczna biblioteka libRUIN.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libruin/ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libruin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libruin.so.0
%{_libdir}/libruin

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libruin.so
%{_libdir}/libruin.la
%{_includedir}/libruin.h
%{_infodir}/libruin.info*
%{_mandir}/man3/ruin.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libruin.a
