Summary:	The SASL library API for the Cyrus mail system.
Name:		cyrus-sasl
Version:	1.5.15
Release:	3
Copyright:	distributable
Group:		Libraries
Source:		ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/%{name}-%{version}.tar.gz
BuildRequires:	gdbm-devel
BuildRequires:	pam-devel
URL:		http://asg.web.cmu.edu/cyrus/imapd/
Buildroot:	/tmp/%{name}-%{version}-root

%description
The cyrus-sasl package contains the SASL library API implementation
for the Cyrus mail system.

%package devel
Summary:	Header files and documentation for cyrus-sasl
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cyrus-sasl.

%package static
Summary:	Static cyrus-sasl libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static cyrus-sasl libraries.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/sasl/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/sasl
%attr(755,root,toot) %{_libdir}/lib*.so.*.*
%attr(755,root,toot) %{_libdir}/sasl/lib*.so*
%attr(755,root,toot) %{_sbindir}/saslpasswd
%{_mandir}/man[18]/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,toot) %{_libdir}/lib*.so
%attr(755,root,toot) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/sasl/lib*.a
