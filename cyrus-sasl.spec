#
# Conditional builds:	
# x509 - build x509 pluggin
# srp - build srp pluggin
#
Summary:	The SASL library API for the Cyrus mail system
Summary(pl):	Biblioteka Cyrus SASL
Name:		cyrus-sasl
Version:	1.5.27
Release:	8
License:	distributable
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/%{name}-%{version}.tar.gz
Source1:	saslauthd.init
Source2:	saslauthd.sysconfig
Source3:	%{name}.pam
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-des.patch
Patch2:		%{name}-mysql-ldap.patch
Patch3:		%{name}-saslauthd.patch
#Patch4:	http://www.imasy.or.jp/~ume/ipv6/cyrus-sasl-1.5.24-ipv6-20010321.diff.gz
Patch4:		%{name}-ipv6.patch
Patch5:		%{name}-ac25x.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db3-devel >= 3.1.17-8
BuildRequires:	pam-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	libtool	>= 1.4
%{?_with_mysql:BuildRequires: mysql-devel}
%{?_with_ldap:BuildRequires: openldap-devel}
URL:		http://asg.web.cmu.edu/sasl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sasl

%description
The cyrus-sasl package contains the SASL library API implementation
for the Cyrus mail system.

%description -l pl
Pakiet cyrus-sasl zawiera implementacjЙ biblioteki API SASL dla
systemu poczty elektronicznej Cyrusa.

%package devel
Summary:	Header files and documentation for cyrus-sasl
Summary(pl):	Pliki nagЁСwkowe i dokumentacja dla cyrus-sasl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Header files and documentation for cyrus-sasl.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja dla cyrus-sasl.

%package static
Summary:	Static cyrus-sasl libraries
Summary(pl):	Statyczne biblioteki cyrus-sasl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Static cyrus-sasl libraries.

%description static -l pl
Statyczne biblioteki cyrus-sasl.

%package cram-md5
Summary:	Cram-MD5 Cyrus SASL plugin
Summary(pl):	Wtyczka Cram-MD5 do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description cram-md5
Cram-MD5 Cyrus SASL plugin.

%description cram-md5 -l pl
Wtyczka Cram-MD5 do Cyrus SASL.

%package digest-md5
Summary:	Digest-MD5 Cyrus SASL plugin
Summary(pl):	Wtyczka Digest-MD5 do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description digest-md5
Digest-MD5 Cyrus SASL plugin.

%description digest-md5 -l pl
Wtyczka Digest-MD5 do Cyrus SASL.

%package plain
Summary:	Plain Cyrus SASL plugin
Summary(pl):	Wtyczka plain do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description plain
Plain Cyrus SASL plugin.

%description plain -l pl
Wtyczka plain do Cyrus SASL.

%package anonymous
Summary:	Anonymous Cyrus SASL plugin
Summary(pl):	Wtyczka anonymous do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description anonymous
Anonymous Cyrus SASL plugin.

%description anonymous -l pl
Wtyczka anonymous do Cyrus SASL.

%package login
Summary:	Unsupported Login Cyrus SASL plugin
Summary(pl):	Wtyczka Unsupported Login do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description login
Unsupported Login Cyrus SASL plugin.

%description login -l pl
Wtyczka Unsupported Login do Cyrus SASL.

%package srp
Summary:	SRP Cyrus SASL plugin
Summary(pl):	Wtyczka SRP do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description srp
SRP Cyrus SASL plugin.

%description srp -l pl
Wtyczka SRP do Cyrus SASL.

%package x509
Summary:	x509 Cyrus SASL plugin
Summary(pl):	Wtyczka x509 do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description x509
x509 Cyrus SASL plugin.

%description x509 -l pl
Wtyczka x509 do Cyrus SASL.

%package saslauthd
Summary:	Cyrus SASL authd
Summary(pl):	Demon authd do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}
Prereq:		/sbin/chkconfig

%description saslauthd
Cyrus SASL authd.

%description saslauthd -l pl
Demon authd do Cyrus SASL.

%package pwcheck
Summary:	Cyrus SASL pwcheck helper
Summary(pl):	Program pomocniczy pwcheck do Cyrus SASL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Requires:	%{name} = %{version}

%description pwcheck
Cyrus SASL pwcheck helper.

%description pwcheck -l pl
Program pomocniczy pwcheck do Cyrus SASL.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f config/missing
libtoolize --copy --force
aclocal -I cmulocal
autoheader
automake -a
autoconf
LDFLAGS="%{rpmldflags} -ldl"; export LDFLAGS
%configure \
	--enable-static \
	--enable-login \
	%{?_with_srp:--enable-srp} \
	%{?_with_x509:--enable-x509} \
	%{?_with_mysql: --with-mysql=%{_prefix}} \
	%{?_with_ldap: --with-ldap=%{_prefix}} \
	%{?_with_pwcheck: --with-pwcheck=/var/lib/sasl} \
	--with-saslauthd=/var/lib/sasl \
	--with-pam \
	--with-dblib=berkeley \
	--with-dbpath=/var/lib/sasl/sasl.db \
	--with-configdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/sasl,%{_sysconfdir},/etc/{rc.d/init.d,sysconfig,pam.d}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/var/lib/sasl/sasl.db

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/saslauthd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/saslauthd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/cyrus

gzip -9nf COPYING testing.txt NEWS TODO README doc/*.txt doc/*.html 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post saslauthd
/sbin/chkconfig --add saslauthd
if [ -f /var/lock/subsys/saslauthd ]; then
	/etc/rc.d/init.d/saslauthd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/saslauthd start\" to start saslauthd."
fi

%postun saslauthd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/saslauthd ]; then
		/etc/rc.d/init.d/saslauthd stop 1>&2
	fi
	/sbin/chkconfig --del saslauthd
fi

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%dir %{_libdir}/sasl
%dir /var/lib/sasl
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_sbindir}/sasldblistusers
%attr(755,root,root) %{_sbindir}/saslpasswd

%attr(640,root,mail) %ghost %config(noreplace) %verify(not mtime md5 size) /var/lib/sasl/sasl.db
%{_mandir}/man[18]/*
%doc *.gz doc/*.gz

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

%if %{?_with_srp:1}%{?!_with_srp:0}
%files srp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libsrp.so*
%endif

%if %{?_with_x509:1}%{?!_with_x509:0}
%files x509
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl/libx509.so*
%endif

%if %{?_with_pwcheck:1}%{?!_with_pwcheck:0}
%files pwcheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pwcheck
%endif

%files saslauthd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/saslauthd
%attr(755,root,root) /etc/rc.d/init.d/saslauthd
%config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/saslauthd
%config(noreplace) %verify(not mtime md5 size) /etc/pam.d/cyrus
