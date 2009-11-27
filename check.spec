Summary:	Check - unit testing framework for C
Summary(pl.UTF-8):	Check - szkielet testów jednostkowych dla C
Name:		check
Version:	0.9.5
Release:	1
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/check/%{name}-%{version}.tar.gz
# Source0-md5:	30143c7974b547a12a7da47809a90951
Patch0:		%{name}-info.patch
URL:		http://check.sourceforge.net/
# aclocal required for %{_aclocaldir}
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	texinfo >= 4.2
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check is a unit test framework for C. It features a simple interface
for defining unit tests, putting little in the way of the developer.
Tests are run in a separate address space, so Check can catch both
assertion failures and code errors that cause segmentation faults or
other signals. The output from unit tests can be used within source
code editors and IDEs.

%description -l pl.UTF-8
Check to szkielet testów jednostkowych dla C. Ma prosty interfejs do
definiowania testów jednostkowych, nie przeszkadzający zbytnio
programiście. Testy są uruchamiane w wydzielonej przestrzeni
adresowej, dzięki czemu Check może wyłapać zarówno niepowodzenia
zapewnień (assert), jak i błędy w kodzie powodujące naruszenie
ochrony pamięci lub inne sygnały. Wyjście z testów jednostkowych może
być używane z poziomu edytorów kodu źródłowego i IDE.

%package static
Summary:	Static check library
Summary(pl.UTF-8):	Biblioteka statyczna check
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static check library.

%description static -l pl.UTF-8
Biblioteka statyczna check.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -fPIC"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	exampledir=%{_examplesdir}/%{name}-%{version} \
	examplesrcdir=%{_examplesdir}/%{name}-%{version}/src \
	exampletestsdir=%{_examplesdir}/%{name}-%{version}/tests \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libdir}/libcheck.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README SVNChangeLog THANKS TODO
%attr(755,root,root) %{_libdir}/libcheck.so.*.*.*
%attr(755,root,root) %{_libdir}/libcheck.so
%{_includedir}/check.h
%{_aclocaldir}/check.m4
%{_pkgconfigdir}/check.pc
%{_infodir}/check.info*
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libcheck.a
