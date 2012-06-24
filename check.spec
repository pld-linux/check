Summary:	Check - unit testing framework for C
Summary(pl):	Check - szkielet test�w jednostkowych dla C
Name:		check
Version:	0.9.5
Release:	0.1
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/check/%{name}-%{version}.tar.gz
# Source0-md5:	30143c7974b547a12a7da47809a90951
URL:		http://check.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Check is a unit test framework for C. It features a simple interface
for defining unit tests, putting little in the way of the developer.
Tests are run in a separate address space, so Check can catch both
assertion failures and code errors that cause segmentation faults or
other signals. The output from unit tests can be used within source
code editors and IDEs.

%description -l pl
Check to szkielet test�w jednostkowych dla C. Ma prosty interfejs do
definiowania test�w jednostkowych, nie przeszkadzaj�cy zbytnio
programi�cie. Testy s� uruchamiane w wydzielonej przestrzeni
adresowej, dzi�ki czemu Check mo�e wy�apa� zar�wno niepowodzenia
zapewnie� (assert), jak i b��dy w kodzie powoduj�ce naruszenie
ochrony pami�ci lub inne sygna�y. Wyj�cie z test�w jednostkowych mo�e
by� u�ywane z poziomu edytor�w kodu �r�d�owego i IDE.

%prep
%setup -q

%build
%configure2_13
%{__make} \
    CFLAGS="%{rpmcflags} -Wall -Wstrict-prototypes -Wmissing-prototypes -Wwrite-strings -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README doc/*.html
%{_libdir}/libcheck.a
%{_includedir}/check.h
%{_aclocaldir}/check.m4
