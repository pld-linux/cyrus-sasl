#
# Conditional build:
%bcond_without	cryptedpw	# if you keep crypted passwords in your *sql
%bcond_without	ldap		# disable LDAP support for saslauthd
%bcond_without	gssapi		# do not enable GSSAPI support for saslauthd and build gssapi plugin
%bcond_without	mysql		# don't build MySQL plugin
%bcond_without	nagios		# do not enable Nagios plugin
%bcond_without	ntlm		# do not build NTLM plugin
%bcond_without	pgsql		# do not build PostgreSQL plugin
%bcond_without	sqlite		# do not enable sqlite 2 plugin
%bcond_without	sqlite3		# do not enable sqlite 3 plugin
%bcond_with	authlib		# enable courier-authlib (i wasn't able to test it)
%bcond_with	opie		# OTP plugin using opie library instead of internal code
%bcond_with	srp		# build srp plugin
%bcond_with	pwcheck		# build pwcheck helper (deprecated)
#
%if %{without mysql} && %{without pgsql}
%undefine with_cryptedpw
%endif

Summary:	The SASL library API for the Cyrus mail system
Summary(pl.UTF-8):	Biblioteka Cyrus SASL
Summary(pt_BR.UTF-8):	Implementação da API SASL
Summary(ru.UTF-8):	Библиотека Cyrus SASL
Summary(uk.UTF-8):	Бібліотека Cyrus SASL
Name:		cyrus-sasl
Version:	2.1.28
Release:	2
License:	distributable
Group:		Libraries
#Source0Download: https://github.com/cyrusimap/cyrus-sasl/releases
Source0:	https://github.com/cyrusimap/cyrus-sasl/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6f228a692516f5318a64505b46966cfa
Source1:	saslauthd.init
Source2:	saslauthd.sysconfig
Source3:	%{name}.pam
Source4:	check_saslauthd.cfg
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-lt.patch
Patch2:		%{name}-split-sql.patch
Patch3:		%{name}-opie.patch
# Adapted from http://frost.ath.cx/software/cyrus-sasl-patches/dist/2.1.19/cyrus-sasl-2.1.19-checkpw.c+sql.c.patch
Patch5:		%{name}-cryptedpw.patch
Patch6:		%{name}-md5sum-passwords.patch
Patch7:		%{name}-db.patch
Patch9:		%{name}-sizes.patch
Patch10:	%{name}-nagios-plugin.patch
Patch12:	%{name}-gssapi-detect.patch
Patch14:	%{name}-ac-libs.patch
Patch20:	%{name}-auxprop.patch
Patch21:	0030-dont_use_la_files_for_opening_plugins.patch
URL:		https://www.cyrusimap.org/sasl/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
%{?with_authlib:BuildRequires:	courier-authlib-devel}
BuildRequires:	db-devel
BuildRequires:	ed
BuildRequires:	groff
%{?with_gssapi:BuildRequires:	heimdal-devel}
BuildRequires:	libtool >= 1.4
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_opie:BuildRequires:	opie-devel}
BuildRequires:	pam-devel
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sphinx-pdg-3
%{?with_sqlite:BuildRequires:	sqlite-devel}
%{?with_sqlite3:BuildRequires:	sqlite3-devel >= 3}
Requires:	pam >= 0.79.0
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	cyrus-sasl-x509 < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sasl

%define		specflags	-fno-strict-aliasing

%description
This is an implementation of the SASL API, useful for adding
authentication, authorization, and security to network protocols. The
SASL protocol itself is documented in rfc2222; the API standard is a
work in progress.

Note: remember to install appropriate plugins, or you won't have any
authentication mechanisms available.

%description -l pl.UTF-8
Pakiet cyrus-sasl zawiera implementację biblioteki API SASL dla
systemu poczty elektronicznej Cyrusa. Biblioteka ta jest przydatna
także do dodawania uwierzytelniania, autoryzacji oraz zwiększania
bezpieczeństwa protokołów sieciowych. Sam protokół SASL jest opisany w
RFC 2222; standaryzacja API jest w toku.

Uwaga: aby były dostępne jakiekolwiek mechanizmy autoryzacji, należy
doinstalować odpowiednie wtyczki.

%description -l pt_BR.UTF-8
Esta é uma implementação da API SASL, útil para acrescentar
autenticação, autorização e seguança (criptografia) para protocolos de
rede. O protocolo SASL está documentado na RFC 2222. A API "padrão"
ainda está em desenvolvimento.

%description -l ru.UTF-8
Пакет cyrus-sasl содержит реализацию Cyrus SASL. SASL - это Simple
Authentication and Security Layer, метод для добавления поддержки
аутентикации к протоколам, основанным на соединениях.

%description -l uk.UTF-8
Пакет cyrus-sasl містить реалізацію Cyrus SASL. SASL - це Simple
Authentication and Security Layer, метод для додання підтримки
аутентикації до протоколів, базованих на з'єднаннях.

%package libs
Summary:	cyrus-sasl library itself
Summary(pl.UTF-8):	Sama biblioteka cyrus-sasl
Group:		Libraries
Requires(post,postun):	/sbin/ldconfig
Conflicts:	cyrus-sasl < 2.1.23-8

%description libs
cyrus-sasl library itself.

%description libs -l pl.UTF-8
Sama biblioteka cyrus-sasl.

%package devel
Summary:	Header files and documentation for cyrus-sasl
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla cyrus-sasl
Summary(pt_BR.UTF-8):	Exemplos e arquivos para desenvolvimento com SASL
Summary(ru.UTF-8):	Файлы для программирования с библиотекой Cyrus SASL
Summary(uk.UTF-8):	Файли для програмування з бібліотекою Cyrus SASL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This includes the header files and documentation needed to develop
applications which use SASL.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla cyrus-sasl.

%description devel -l pt_BR.UTF-8
Este pacote inclui os arquivos de cabeçalho e documentação necessários
para desenvolver aplicativos que usem SASL.

%description devel -l ru.UTF-8
Хедеры и библиотеки, необходимые для разработки приложений,
использующих Cyrus SASL.

%description devel -l uk.UTF-8
Хедери та бібліотеки, необхідні для розробки програм, що
використовують Cyrus SASL.

%package static
Summary:	Static cyrus-sasl libraries
Summary(pl.UTF-8):	Statyczne biblioteki cyrus-sasl
Summary(ru.UTF-8):	Статические библиотеки Cyrus SASL
Summary(uk.UTF-8):	Статичні бібліотеки Cyrus SASL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cyrus-sasl libraries.

%description static -l pl.UTF-8
Statyczne biblioteki cyrus-sasl.

%description static -l ru.UTF-8
Статические библиотеки, необходимые для разработки приложений,
использующих Cyrus SASL.

%description static -l uk.UTF-8
Статичні бібліотеки, необхідні для розробки програм, що використовують
Cyrus SASL.

%package anonymous
Summary:	Anonymous Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka anonymous do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL ANONYMOUS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description anonymous
This plugin implements the SASL ANONYMOUS mechanism, used for
anonymous authentication.

%description anonymous -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu ANONYMOUS do Cyrus SASL. Służy do
anonimowego uwierzytelniania.

%description anonymous -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL ANONYMOUS, usado para
autenticação anônima.

%package cram-md5
Summary:	Cram-MD5 Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka Cram-MD5 do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL CRAM-MD5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cram-md5
This plugin implements the SASL CRAM-MD5 mechanism. CRAM-MD5 is the
mandatory-to-implement authentication mechanism for a number of
protocols; it uses MD5 with a challenge/response system to
authenticate the user.

%description cram-md5 -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu CRAM-MD5 do Cyrus SASL. CRAM-MD5
jest obowiązkowym do zaimplementowania mechanizmem uwierzytelniania
dla wielu protokołów; do uwierzytelnienia użytkownika używa MD5 wraz z
systemem challenge/response.

%description cram-md5 -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL CRAM-MD5. CRAM-MD5 é o
mecanismo de autenticação obrigatório de ser implementado para vários
protocolos: ele usa MD5 com um sistema de desafio/resposta para
autenticar o usuário.

%package digest-md5
Summary:	Digest-MD5 Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka Digest-MD5 do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL DIGEST-MD5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description digest-md5
This plugin implements the latest draft of the SASL DIGEST-MD5
mechanism. Although not yet finalized, this is likely to become the
new mandatory-to-implement authentication system in all new protocols.
It's based on the digest md5 authentication system designed for HTTP.

%description digest-md5 -l pl.UTF-8
Wtyczka dodająca najnowszą wersję mechanizmu DIGEST-MD5 do Cyrus SASL.
Pomimo tego, że nie jest jeszcze ukończony, najprawdopodobniej stanie
się obowiązkowym do zaimplementowania systemem uwierzytelniania we
wszystkich nowych protokołach. Bazuje na systemie uwierzytelniania
Digest-MD5 zaprojektowanym dla HTTP.

%description digest-md5 -l pt_BR.UTF-8
Este plugin implementa a última versão da especificação do mecanismo
SASL DIGEST-MD5. Embora ainda não esteja finalizado, DIGEST-MD5
provavelmente será o novo sistema de autenticação obrigatório para
protocolos novos. Ele é baseado na autenticação md5 digest
desenvolvida para HTTP.

%package gssapi
Summary:	GSSAPI Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka GSSAPI do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL GSSAPI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gssapi
This plugin implements the SASL GSSAPI mechanism, used for
GSSAPI/Kerberos5 authentication.

%description gssapi -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu SASL GSSAPI, używanego do
uwierzytelniania z użyciem GSSAPI/Kerberos5.

%description gssapi -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL GSSAPI, usado para
autenticação Kerberos/GSSAPI.

%package login
Summary:	Unsupported Login Cyrus SASL plugin
Summary(pl.UTF-8):	Nie wspierana wtyczka Login do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description login
Unsupported LOGIN Cyrus SASL plugin.

%description login -l pl.UTF-8
Wtyczka dodająca obsługę nie wspieranego mechanizmu LOGIN do Cyrus
SASL.

%package mysql
Summary:	Cyrus SASL MySQL plugin
Summary(pl.UTF-8):	Wtyczka MySQL do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
Cyrus SASL MySQL plugin.

%description mysql -l pl.UTF-8
Wtyczka MySQL do Cyrus SASL.

%package ntlm
Summary:	Cyrus SASL NTLM plugin
Summary(pl.UTF-8):	Wtyczka NTLM do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ntlm
Cyrus SASL NTLM plugin.

%description ntlm -l pl.UTF-8
Wtyczka NTLM do Cyrus SASL.

%package otp
Summary:	OTP Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka OTP do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL OTP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	cyrus-sasl-opie < %{version}

%description otp
This plugin implements the SASL OTP (One Time Password) mechanism.

%description otp -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu OTP (hasła jednorazowe) do Cyrus
SASL.

%package pgsql
Summary:	Cyrus SASL PostgreSQL plugin
Summary(pl.UTF-8):	Wtyczka PostgreSQL do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pgsql
Cyrus SASL PostgreSQL plugin.

%description pgsql -l pl.UTF-8
Wtyczka PostgreSQL do Cyrus SASL.

%package plain
Summary:	Plain Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka plain do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL PLAIN
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plain
This plugin implements the SASL PLAIN mechanism. Although insecure,
PLAIN is useful for transitioning to new security mechanisms, as this
is the only mechanism which gives the server a copy of the user's
password.

%description plain -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu PLAIN do Cyrus SASL. Pomimo tego,
że nie jest bezpieczny, PLAIN jest przydatny przy przechodzeniu na
nowe mechanizmu bezpieczeństwa, jako że jest to jedyny mechanizm,
który udostępnia serwerowi kopię hasła użytkownika.

%description plain -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL PLAIN. Embora inseguro, este
mecanismo é útil durante transições para novos mecanismos de
segurança, pois é o único esquema que fornece uma cópia da senha do
usuário para o servidor.

%package sasldb
Summary:	Cyrus SASL sasldb plugin
Summary(pl.UTF-8):	Wtyczka sasldb do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sasldb
Cyrus SASL sasldb plugin.

%description sasldb -l pl.UTF-8
Wtyczka sasldb do Cyrus SASL.

%package ldapdb
Summary:	Cyrus SASL LDAPDB plugin
Summary(pl.UTF-8):	Wtyczka LDAPDB do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ldapdb
Cyrus SASL ldapdb plugin.

%description ldapdb -l pl.UTF-8
Wtyczka ldapdb do Cyrus SASL.

%package passdss
Summary:	PASSDSS Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka PASSDSS do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL PASSDSS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description passdss
This plugin implements the PASSDSS 3DES mechanism.

%description passdss -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu PASSDSS 3DES do Cyrus SASL.

%description passdss -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL PASSDSS 3DES.

%package scram
Summary:	SCRAM Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka SCRAM do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL SCRAM
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description scram
This plugin implements the SASL SCRAM-MD5 mechanism.

%description scram -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu SCRAM do Cyrus SASL.

%description scram -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL SCRAM.

%package sqlite
Summary:	Cyrus SQLite 2 PostgreSQL plugin
Summary(pl.UTF-8):	Wtyczka SQLite 2 do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sqlite
Cyrus SASL SQLite 2 plugin.

%description sqlite -l pl.UTF-8
Wtyczka SQLite 2 do Cyrus SASL.

%package sqlite3
Summary:	Cyrus SQLite 3 PostgreSQL plugin
Summary(pl.UTF-8):	Wtyczka SQLite 3 do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sqlite3
Cyrus SASL SQLite 3 plugin.

%description sqlite3 -l pl.UTF-8
Wtyczka SQLite 3 do Cyrus SASL.

%package srp
Summary:	SRP Cyrus SASL plugin
Summary(pl.UTF-8):	Wtyczka SRP do Cyrus SASL
Summary(pt_BR.UTF-8):	Mecanismo SASL SRP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description srp
This plugin implements the SASL SRP mechanism, based on the Secure
Remote Password protocol. This mechanism performs mutual
authentication and can provide a security layer with replay detection,
integrity protection and/or condifentiality protection.

%description srp -l pl.UTF-8
Wtyczka dodająca obsługę mechanizmu SRP do Cyrus SASL. Bazuje na
protokole Secure Remote Password. Ten mechanizm dokonuje wzajemnego
uwierzytelnienia i może dodawać warstwę bezpieczeństwa z wykrywaniem
powtarzania, zabezpieczeniem integralności i/lub poufności.

%description srp -l pt_BR.UTF-8
Este plugin implementa o mecanismo SASL SRP, baseado no protocolo SRP
(Secure Remote Password). Este mecanismo oferece autenticação mútua
(do cliente e do servidor) e pode prover uma camada de segurança com
detecção de ataques de replay, garantia de integridade e/ou
confidencialidade.

%package pwcheck
Summary:	Cyrus SASL pwcheck helper
Summary(pl.UTF-8):	Program pomocniczy pwcheck do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pwcheck
Cyrus SASL pwcheck helper.

%description pwcheck -l pl.UTF-8
Program pomocniczy pwcheck do Cyrus SASL.

%package saslauthd
Summary:	Cyrus SASL authd
Summary(pl.UTF-8):	Demon authd do Cyrus SASL
Group:		Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}
Requires:	/sbin/chkconfig
Requires:	rc-scripts

%description saslauthd
Cyrus SASL authd.

%description saslauthd -l pl.UTF-8
Demon authd do Cyrus SASL.

%package -n nagios-plugin-check_saslauthd
Summary:	Nagios plugin to check health of saslauthd
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania działania saslauthd
Group:		Networking
Requires:	nagios-core

%description -n nagios-plugin-check_saslauthd
Nagios plugin to check health of saslauthd.

%description -n nagios-plugin-check_saslauthd -l pl.UTF-8
Wtyczka Nagiosa do sprawdzania działania saslauthd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if %{with cryptedpw}
%patch5 -p1
%patch6 -p1
%endif
%patch7 -p1
%patch9 -p1
%{?with_nagios:%patch10 -p1}
%patch12 -p1
%patch14 -p1
%patch20 -p1
%patch21 -p1

# update to our paths
sed -i -e '
	s,/usr/local/etc/saslauthd.conf,%{_sysconfdir}/saslauthd.conf,g
	s,/etc/saslauthd.conf,%{_sysconfdir}/saslauthd.conf,g
	s,/var/run/saslauthd/mux,/var/lib/sasl2/mux,g
	s,/var/state/saslauthd,/var/lib/sasl2,g
' saslauthd/saslauthd.mdoc saslauthd/LDAP_SASLAUTHD doc/legacy/sysadmin.html

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SPHINX_BUILD=/usr/bin/sphinx-build-3 \
	%{?with_cryptedpw: LDFLAGS=-lcrypt} \
	%{!?with_gssapi:--disable-gssapi} \
	%{?with_gssapi:--enable-gssapi --with-gss_impl=heimdal} \
	--enable-httpform \
	--disable-krb4 \
	%{?with_ldap:--enable-ldapdb} \
	--enable-login \
	--enable-passdss \
	--enable-sample \
	--enable-sql \
	%{?with_srp:--enable-srp} \
	--enable-static \
	%{?with_authlib:--with-authdaemond=/var/spool/authdaemon/socket} \
	--with-configdir=%{_sysconfdir} \
	--with-dblib=berkeley \
	--with-dbpath=/var/lib/sasl2/sasl.db \
	%{?with_ldap:--with-ldap} \
	%{?with_mysql:--with-mysql=%{_prefix}} \
	%{?with_ntlm:--enable-ntlm} \
	%{?with_opie:--with-opie=%{_prefix}} \
	--with-pam \
	%{?with_pgsql:--with-pgsql=%{_prefix}} \
	--with-plugindir=%{_libdir}/sasl2 \
	%{?with_pwcheck:--with-pwcheck=/var/lib/sasl2} \
	--with-saslauthd=/var/lib/sasl2 \
	%{?with_sqlite:--with-sqlite=%{_prefix}} \
	%{?with_sqlite3:--with-sqlite3=%{_prefix}}

%{__make}

%{__make} -C saslauthd testsaslauthd
%{__make} -C saslauthd saslcache
%{__make} -C sample sample-client sample-server

%{__rm} -rf doc/html/{_sources,objects.inv,.buildinfo}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/var/lib/sasl2,%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
		$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	sasldir=%{_libdir}/sasl2 \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/sasl2/*.{la,a}

cp -a utils/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -a saslauthd/saslauthd.mdoc $RPM_BUILD_ROOT%{_mandir}/man8/saslauthd.8

ln -sf libsasl2.so $RPM_BUILD_ROOT%{_libdir}/libsasl.so

touch $RPM_BUILD_ROOT/var/lib/sasl2/sasl.db

# create empty config
touch $RPM_BUILD_ROOT%{_sysconfdir}/saslauthd.conf
install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/saslauthd
cp -a %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/saslauthd
cp -a %{SOURCE3} cyrus.pam

install -p saslauthd/{testsaslauthd,saslcache} $RPM_BUILD_ROOT%{_sbindir}

# sample programs for testing sasl
libtool --mode=install cp sample/sample-client $RPM_BUILD_ROOT%{_bindir}/sasl-sample-client
libtool --mode=install cp sample/sample-server $RPM_BUILD_ROOT%{_bindir}/sasl-sample-server

# package for ghost
touch $RPM_BUILD_ROOT/var/lib/sasl2/{cache.flock,cache.mmap,mux,mux.accept,saslauthd.pid}

%if %{with nagios}
install -d $RPM_BUILD_ROOT/etc/nagios/plugins
%{__sed} -e 's,@plugindir@,%{_libdir}/nagios/plugins,' %{SOURCE4} > $RPM_BUILD_ROOT/etc/nagios/plugins/check_saslauthd.cfg
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post saslauthd
/sbin/chkconfig --add saslauthd
%service saslauthd restart

%preun saslauthd
if [ "$1" = "0" ]; then
	%service saslauthd stop
	/sbin/chkconfig --del saslauthd
fi

%triggerin saslauthd -- pam
# restart saslauthd if pam is upgraded
# (saslauth is linked with old libpam but tries to open modules linked with new libpam)
if [ "$2" != 1 ]; then
	%service -q saslauthd restart
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README doc/legacy/{TODO,*.html,*.fig} doc/html
%dir %{_sysconfdir}
%dir %{_libdir}/sasl2
# sample programs to subpackage instead?
%attr(755,root,root) %{_bindir}/sasl-sample-client
%attr(755,root,root) %{_bindir}/sasl-sample-server
%attr(755,root,root) %{_sbindir}/pluginviewer
%attr(755,root,root) %{_sbindir}/sasldblistusers2
%attr(755,root,root) %{_sbindir}/saslpasswd2
%dir /var/lib/sasl2
%attr(640,root,mail) %ghost %config(noreplace) %verify(not md5 mtime size) /var/lib/sasl2/sasl.db
%{_mandir}/man8/pluginviewer.8*
%{_mandir}/man8/sasldblistusers2.8*
%{_mandir}/man8/saslpasswd2.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsasl2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsasl2.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsasl2.so
%attr(755,root,root) %{_libdir}/libsasl.so
%{_libdir}/libsasl2.la
%{_includedir}/sasl
%{_pkgconfigdir}/libsasl2.pc
%{_mandir}/man3/sasl*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsasl2.a

%files anonymous
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libanonymous.so*

%if %{with gssapi}
%files gssapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libgs2.so*
%attr(755,root,root) %{_libdir}/sasl2/libgssapiv2.so*
%endif

%files cram-md5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libcrammd5.so*

%files digest-md5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libdigestmd5.so*

%files login
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/liblogin.so*

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libmysql.so*
%endif

%if %{with ntlm}
%files ntlm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libntlm.so*
%endif

%files otp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libotp.so*

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libpgsql.so*
%endif

%files plain
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libplain.so*

%files sasldb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsasldb.so*

%if %{with ldap}
%files ldapdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libldapdb.so*
%endif

%files passdss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libpassdss.so*

%files scram
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libscram.so*

%if %{with sqlite}
%files sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsqlite.so*
%endif

%if %{with sqlite3}
%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsqlite3.so*
%endif

%if %{with srp}
%files srp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsrp.so*
%endif

%if %{with pwcheck}
%files pwcheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pwcheck
%endif

%files saslauthd
%defattr(644,root,root,755)
%doc cyrus.pam saslauthd/{COPYING,LDAP_SASLAUTHD}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/saslauthd.conf
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/saslauthd
%attr(755,root,root) %{_sbindir}/saslauthd
%attr(755,root,root) %{_sbindir}/testsaslauthd
%attr(755,root,root) %{_sbindir}/saslcache
%attr(754,root,root) /etc/rc.d/init.d/saslauthd
%ghost /var/lib/sasl2/cache.flock
%ghost /var/lib/sasl2/cache.mmap
%ghost /var/lib/sasl2/mux
%ghost /var/lib/sasl2/mux.accept
%ghost /var/lib/sasl2/saslauthd.pid
%{_mandir}/man8/saslauthd.8*
%{_mandir}/man8/testsaslauthd.8*

%if %{with nagios}
%files -n nagios-plugin-check_saslauthd
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/nagios/plugins/check_saslauthd.cfg
%attr(755,root,root) %{_libdir}/nagios/plugins/check_saslauthd
%endif
