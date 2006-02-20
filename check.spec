Summary:	Check - unit testing framework for C
Summary(pl):	Check - szkielet testów jednostkowych dla C
Name:		check
Version:	0.9.3
Release:	2
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/check/%{name}-%{version}.tar.gz
# Source0-md5:	6e5870f7c9c5414572158d8005e91d68
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
Check to szkielet testów jednostkowych dla C. Ma prosty interfejs do
definiowania testów jednostkowych, nie przeszkadzaj±cy zbytnio
programi¶cie. Testy s± uruchamiane w wydzielonej przestrzeni
adresowej, dziêki czemu Check mo¿e wy³apaæ zarówno niepowodzenia
zapewnieñ (assert), jak i b³êdy w kodzie powoduj±ce naruszenie
ochrony pamiêci lub inne sygna³y. Wyj¶cie z testów jednostkowych mo¿e
byæ u¿ywane z poziomu edytorów kodu ¼ród³owego i IDE.

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
