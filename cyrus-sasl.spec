#
# Conditional builds:
# x509 - build x509 pluggin
# srp - build srp pluggin
#
Summary:	The SASL library API for the Cyrus mail system.
Name:		cyrus-sasl
Version:	1.5.24
Release:	7
LIcense:	Distributable
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/%{name}-%{version}.tar.gz
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-des.patch
BuildRequires:	db3-devel
BuildRequires:	pam-devel
BuildRequires:	openssl-devel
URL:		http://asg.web.cmu.edu/sasl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sasl

%description
The cyrus-sasl package contains the SASL library API implementation
for the Cyrus mail system.

%description -l pl
Pakiet cyrus-sasl zawiera implementację biblioteki API SASL dla
systemu poczty elektronicznej Cyrusa.

%package devel
Summary:	Header files and documentation for cyrus-sasl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cyrus-sasl.

%package static
Summary:	Static cyrus-sasl libraries
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static cyrus-sasl libraries.

%package cram-md5
Summary:	Cram-MD5 Cyrus SASL pluggin
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description cram-md5
Cram-MD5 Cyrus SASL pluggin.

%package digest-md5
Summary:	Digest-MD5 Cyrus SASL pluggin
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description digest-md5
Digest-MD5 Cyrus SASL pluggin.

%package plain
Summary:	Plain Cyrus SASL pluggin
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description plain
Plain Cyrus SASL pluggin.

%package anonymous
Summary:	Anonymous Cyrus SASL pluggin
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description anonymous
Anonymous Cyrus SASL pluggin.

%package login
Summary:	Unsupported Login Cyrus SASL pluggin
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description login
Unsupported Login Cyrus SASL pluggin.

%if %{?srp:1}%{?!srp:0}
%package srp
Summary:	SRP Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description srp
SRP Cyrus SASL pluggin.

%endif

%if %{?x509:1}%{?!x509:0}
%package x509
Summary:	x509 Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description x509
x509 Cyrus SASL pluggin.

%endif

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
aclocal -I cmulocal
autoheader
automake -a
autoconf
%configure \
	--enable-static \
	--enable-login \
	%{?srp:--enable-srp} \
	%{?x509:--enable-x509} \
	--with-pam \
	--with-dblib=berkeley \
	--with-dbpath=/var/lib/sasl/sasl.db \
	--with-configdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/sasl,%{_sysconfdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/var/lib/sasl/sasl.db

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%dir %{_libdir}/sasl
%dir /var/lib/sasl
%attr(755,root,root) %{_libdir}/lib*.so.*.*
#%attr(755,root,root) %{_libdir}/sasl/lib*.so*
%attr(755,root,root) %{_sbindir}/*

%config(noreplace) %verify(not mtime md5 size) /var/lib/sasl/sasl.db
%{_mandir}/man[18]/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/sasl/lib*.a

%files cram-md5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libcrammd5.so*

%files digest-md5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libdigestmd5.so*

%files plain
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libplain.so*

%files anonymous
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libanonymous.so*

%files login
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/liblogin.so*

%if %{?srp:1}%{?!srp:0}
%files srp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libsrp.so*
%endif

%if %{?x509:1}%{?!x509:0}
%files x509
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libx509.so*
%endif
