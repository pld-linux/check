#
# Conditional build:
%bcond_without	subunit	# support for subunit test protocol

Summary:	Check - unit testing framework for C
Summary(pl.UTF-8):	Check - szkielet testów jednostkowych dla C
Name:		check
Version:	0.15.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/libcheck/check/releases
Source0:	https://github.com/libcheck/check/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	50fcafcecde5a380415b12e9c574e0b2
URL:		https://libcheck.github.io/check/
# aclocal required for %{_aclocaldir}
BuildRequires:	automake >= 1:1.11.2
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
%{?with_subunit:BuildRequires:	subunit-devel}
BuildRequires:	texinfo >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Check is a unit test framework for C. It features a simple interface
for defining unit tests, putting little in the way of the developer.
Tests are run in a separate address space, so Check can catch both
assertion failures and code errors that cause segmentation faults or
other signals. The output from unit tests can be used within source
code editors and IDEs.

This package contains only shared library.

%description -l pl.UTF-8
Check to szkielet testów jednostkowych dla C. Ma prosty interfejs do
definiowania testów jednostkowych, nie przeszkadzający zbytnio
programiście. Testy są uruchamiane w wydzielonej przestrzeni
adresowej, dzięki czemu Check może wyłapać zarówno niepowodzenia
zapewnień (assert), jak i błędy w kodzie powodujące naruszenie ochrony
pamięci lub inne sygnały. Wyjście z testów jednostkowych może być
używane z poziomu edytorów kodu źródłowego i IDE.

Ten pakiet zawiera tylko bibliotekę współdzieloną.

%package devel
Summary:	Headers for developing programs with check library
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów przy użyciu biblioteki checka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_subunit:Requires:	subunit-devel}

%description devel
Headers for developing programs with check library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów przy użyciu biblioteki checka.

%package static
Summary:	Static check library
Summary(pl.UTF-8):	Biblioteka statyczna check
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static check library.

%description static -l pl.UTF-8
Biblioteka statyczna check.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -fPIC"
%configure \
	%{!?with_subunit:--disable-subunit}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	exampledir=%{_examplesdir}/%{name}-%{version} \
	examplesrcdir=%{_examplesdir}/%{name}-%{version}/src \
	exampletestsdir=%{_examplesdir}/%{name}-%{version}/tests \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcheck.la
%{__rm} -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libcheck.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheck.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/checkmk
%attr(755,root,root) %{_libdir}/libcheck.so
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_aclocaldir}/check.m4
%{_pkgconfigdir}/check.pc
%{_mandir}/man1/checkmk.1*
%{_infodir}/check.info*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libcheck.a
