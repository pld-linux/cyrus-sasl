Summary:	The SASL library API for the Cyrus mail system.
Name:		cyrus-sasl
Version:	1.5.21
Release:	3
Copyright:	distributable
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/%{name}-%{version}.tar.gz
Patch0:		cyrus-sasl-configdir.patch
BuildRequires:	gdbm-devel
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cyrus-sasl.

%package static
Summary:	Static cyrus-sasl libraries
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static cyrus-sasl libraries.

%package cram-md5
Summary:	Cram-MD5 Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description cram-md5
Cram-MD5 Cyrus SASL pluggin.

%package digest-md5
Summary:	Digest-MD5 Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description digest-md5
Digest-MD5 Cyrus SASL pluggin.

%package plain
Summary:	Plain Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description plain
Plain Cyrus SASL pluggin.

%package anonymous
Summary:	Anonymous Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description anonymous
Anonymous Cyrus SASL pluggin.

%package login
Summary:	Unsupported Login Cyrus SASL pluggin
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description login
Unsupported Login Cyrus SASL pluggin.

%prep
%setup  -q
%patch0 -p1

%build
aclocal -I cmulocal
autoheader
automake -a
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-static \
	--enable-login \
	--with-pam \
	--with-dblib=gdbm \
	--with-dbpath=/var/lib/sasl/sasl.db \
	--with-configdir=%{_sysconfdir}
	--with-dbpath=/var/lib/sasl/sasl.db
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/sasl

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* \
	$RPM_BUILD_ROOT%{_libdir}/sasl/lib*.so.*.*

touch $RPM_BUILD_ROOT/var/lib/sasl/sasl.db

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/*

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
