#
# TODO:
# - add ldap plugin from openldap sources
# - cleaner solution for mysql/pgsql support
#
# Conditional build:
%bcond_without	ldap	# disable LDAP support for saslauthd
%bcond_with	gssapi	# enable GSSAPI support for saslauthd and build gssapi plugin
%bcond_without	mysql	# don't build MySQL pluggin
%bcond_with	pgsql	# build PostgreSQL pluggin
%bcond_with	srp	# build srp pluggin
%bcond_with	pwcheck	# build pwcheck helper (deprecated)
%bcond_with	x509	# build x509 plugin (no sources in package???)
#
Summary:	The SASL library API for the Cyrus mail system
Summary(pl):	Biblioteka Cyrus SASL
Summary(pt_BR):	Implementação da API SASL
Summary(ru):	âÉÂÌÉÏÔÅËÁ Cyrus SASL
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ Cyrus SASL
Name:		cyrus-sasl
Version:	2.1.20
Release:	2
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus/%{name}-%{version}.tar.gz
# Source0-md5:	268ead27f4ac39bcfe17d9e38e0f2977
Source1:	saslauthd.init
Source2:	saslauthd.sysconfig
Source3:	%{name}.pam
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-lt.patch
URL:		http://asg.web.cmu.edu/sasl/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	ed
BuildRequires:	groff
%{?with_gssapi:BuildRequires:	heimdal-devel}
BuildRequires:	libtool	>= 1.4
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sasl

%description
This is an implementation of the SASL API, useful for adding
authentication, authorization, and security to network protocols. The
SASL protocol itself is documented in rfc2222; the API standard is a
work in progress.

Note: remember to install appropriate plugins, or you won't have any
authentication mechanisms available.

%description -l pl
Pakiet cyrus-sasl zawiera implementacjê biblioteki API SASL dla
systemu poczty elektronicznej Cyrusa. Biblioteka ta jest przydatna
tak¿e do dodawania uwierzytelniania, autoryzacji oraz zwiêkszania
bezpieczeñstwa protoko³ów sieciowych. Sam protokó³ SASL jest opisany w
RFC 2222; standaryzacja API jest w toku.

Uwaga: aby by³y dostêpne jakiekolwiek mechanizmy autoryzacji, nale¿y
doinstalowaæ odpowiednie wtyczki.

%description -l pt_BR
Esta é uma implementação da API SASL, útil para acrescentar
autenticação, autorização e seguança (criptografia) para protocolos de
rede. O protocolo SASL está documentado na RFC 2222. A API "padrão"
ainda está em desenvolvimento.

%description -l ru
ðÁËÅÔ cyrus-sasl ÓÏÄÅÒÖÉÔ ÒÅÁÌÉÚÁÃÉÀ Cyrus SASL. SASL - ÜÔÏ Simple
Authentication and Security Layer, ÍÅÔÏÄ ÄÌÑ ÄÏÂÁ×ÌÅÎÉÑ ÐÏÄÄÅÒÖËÉ
ÁÕÔÅÎÔÉËÁÃÉÉ Ë ÐÒÏÔÏËÏÌÁÍ, ÏÓÎÏ×ÁÎÎÙÍ ÎÁ ÓÏÅÄÉÎÅÎÉÑÈ.

%description -l uk
ðÁËÅÔ cyrus-sasl Í¦ÓÔÉÔØ ÒÅÁÌ¦ÚÁÃ¦À Cyrus SASL. SASL - ÃÅ Simple
Authentication and Security Layer, ÍÅÔÏÄ ÄÌÑ ÄÏÄÁÎÎÑ Ð¦ÄÔÒÉÍËÉ
ÁÕÔÅÎÔÉËÁÃ¦§ ÄÏ ÐÒÏÔÏËÏÌ¦×, ÂÁÚÏ×ÁÎÉÈ ÎÁ Ú'¤ÄÎÁÎÎÑÈ.

%package devel
Summary:	Header files and documentation for cyrus-sasl
Summary(pl):	Pliki nag³ówkowe i dokumentacja dla cyrus-sasl
Summary(pt_BR):	Exemplos e arquivos para desenvolvimento com SASL
Summary(ru):	æÁÊÌÙ ÄÌÑ ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ Ó ÂÉÂÌÉÏÔÅËÏÊ Cyrus SASL
Summary(ru):	æÁÊÌÉ ÄÌÑ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ Ú Â¦ÂÌ¦ÏÔÅËÏÀ Cyrus SASL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This includes the header files and documentation needed to develop
applications which use SASL.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla cyrus-sasl.

%description devel -l pt_BR
Este pacote inclui os arquivos de cabeçalho e documentação necessários
para desenvolver aplicativos que usem SASL.

%description devel -l ru
èÅÄÅÒÙ É ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ,
ÉÓÐÏÌØÚÕÀÝÉÈ Cyrus SASL.

%description devel -l uk
èÅÄÅÒÉ ÔÁ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ
×ÉËÏÒÉÓÔÏ×ÕÀÔØ Cyrus SASL.

%package static
Summary:	Static cyrus-sasl libraries
Summary(pl):	Statyczne biblioteki cyrus-sasl
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ Cyrus SASL
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ Cyrus SASL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cyrus-sasl libraries.

%description static -l pl
Statyczne biblioteki cyrus-sasl.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÉÌÏÖÅÎÉÊ,
ÉÓÐÏÌØÚÕÀÝÉÈ Cyrus SASL.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ, ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ×ÉËÏÒÉÓÔÏ×ÕÀÔØ
Cyrus SASL.

%package cram-md5
Summary:	Cram-MD5 Cyrus SASL plugin
Summary(pl):	Wtyczka Cram-MD5 do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL CRAM-MD5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cram-md5
This plugin implements the SASL CRAM-MD5 mechanism. CRAM-MD5 is the
mandatory-to-implement authentication mechanism for a number of
protocols; it uses MD5 with a challenge/response system to
authenticate the user.

%description cram-md5 -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu CRAM-MD5 do Cyrus SASL. CRAM-MD5
jest obowi±zkowym do zaimplementowania mechanizmem uwierzytelniania
dla wielu protoko³ów; do uwierzytelnienia u¿ytkownika u¿ywa MD5 wraz z
systemem challenge/response.

%description cram-md5 -l pt_BR
Este plugin implementa o mecanismo SASL CRAM-MD5. CRAM-MD5 é o
mecanismo de autenticação obrigatório de ser implementado para vários
protocolos: ele usa MD5 com um sistema de desafio/resposta para
autenticar o usuário.

%package digest-md5
Summary:	Digest-MD5 Cyrus SASL plugin
Summary(pl):	Wtyczka Digest-MD5 do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL DIGEST-MD5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description digest-md5
This plugin implements the latest draft of the SASL DIGEST-MD5
mechanism. Although not yet finalized, this is likely to become the
new mandatory-to-implement authentication system in all new protocols.
It's based on the digest md5 authentication system designed for HTTP.

%description digest-md5 -l pl
Wtyczka dodaj±ca najnowsz± wersjê mechanizmu DIGEST-MD5 do Cyrus SASL.
Pomimo tego, ¿e nie jest jeszcze ukoñczony, najprawdopodobniej stanie
siê obowi±zkowym do zaimplementowania systemem uwierzytelniania we
wszystkich nowych protoko³ach. Bazuje na systemie uwierzytelniania
Digest-MD5 zaprojektowanym dla HTTP.

%description digest-md5 -l pt_BR
Este plugin implementa a última versão da especificação do mecanismo
SASL DIGEST-MD5. Embora ainda não esteja finalizado, DIGEST-MD5
provavelmente será o novo sistema de autenticação obrigatório para
protocolos novos. Ele é baseado na autenticação md5 digest
desenvolvida para HTTP.

%package plain
Summary:	Plain Cyrus SASL plugin
Summary(pl):	Wtyczka plain do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL PLAIN
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plain
This plugin implements the SASL PLAIN mechanism. Although insecure,
PLAIN is useful for transitioning to new security mechanisms, as this
is the only mechanism which gives the server a copy of the user's
password.

%description plain -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu PLAIN do Cyrus SASL. Pomimo tego,
¿e nie jest bezpieczny, PLAIN jest przydatny przy przechodzeniu na
nowe mechanizmu bezpieczeñstwa, jako ¿e jest to jedyny mechanizm,
który udostêpnia serwerowi kopiê has³a u¿ytkownika.

%description plain -l pt_BR
Este plugin implementa o mecanismo SASL PLAIN. Embora inseguro, este
mecanismo é útil durante transições para novos mecanismos de
segurança, pois é o único esquema que fornece uma cópia da senha do
usuário para o servidor.

%package anonymous
Summary:	Anonymous Cyrus SASL plugin
Summary(pl):	Wtyczka anonymous do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL ANONYMOUS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description anonymous
This plugin implements the SASL ANONYMOUS mechanism, used for
anonymous authentication.

%description anonymous -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu ANONYMOUS do Cyrus SASL. S³u¿y do
anonimowego uwierzytelniania.

%description anonymous -l pt_BR
Este plugin implementa o mecanismo SASL ANONYMOUS, usado para
autenticação anônima.

%package gssapi
Summary:	GSSAPI Cyrus SASL plugin
Summary(pl):	Wtyczka GSSAPI do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL GSSAPI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gssapi
This plugin implements the SASL GSSAPI mechanism, used for
GSSAPI/Kerberos5 authentication.

%description gssapi -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu SASL GSSAPI, u¿ywanego do
uwierzytelniania z u¿yciem GSSAPI/Kerberos5.

%description gssapi -l pt_BR
Este plugin implementa o mecanismo SASL GSSAPI, usado para
autenticação Kerberos/GSSAPI.

%package login
Summary:	Unsupported Login Cyrus SASL plugin
Summary(pl):	Nie wspierana wtyczka Login do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description login
Unsupported LOGIN Cyrus SASL plugin.

%description login -l pl
Wtyczka dodaj±ca obs³ugê nie wspieranego mechanizmu LOGIN do Cyrus
SASL.

%package srp
Summary:	SRP Cyrus SASL plugin
Summary(pl):	Wtyczka SRP do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL SRP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description srp
This plugin implements the SASL SRP mechanism, based on the Secure
Remote Password protocol. This mechanism performs mutual
authentication and can provide a security layer with replay detection,
integrity protection and/or condifentiality protection.

%description srp -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu SRP do Cyrus SASL. Bazuje na
protokole Secure Remote Password. Ten mechanizm dokonuje wzajemnego
uwierzytelnienia i mo¿e dodawaæ warstwê bezpieczeñstwa z wykrywaniem
powtarzania, zabezpieczeniem integralno¶ci i/lub poufno¶ci.

%description srp -l pt_BR
Este plugin implementa o mecanismo SASL SRP, baseado no protocolo SRP
(Secure Remote Password). Este mecanismo oferece autenticação mútua
(do cliente e do servidor) e pode prover uma camada de segurança com
detecção de ataques de replay, garantia de integridade e/ou
confidencialidade.

%package otp
Summary:	OTP Cyrus SASL plugin
Summary(pl):	Wtyczka OTP do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL OTP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description otp
This plugin implements the SASL OTP (One Time Password) mechanism.

%description otp -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu OTP (has³a jednorazowe) do Cyrus
SASL.

%package x509
Summary:	x509 Cyrus SASL plugin
Summary(pl):	Wtyczka x509 do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description x509
x509 Cyrus SASL plugin.

%description x509 -l pl
Wtyczka x509 do Cyrus SASL.

%package saslauthd
Summary:	Cyrus SASL authd
Summary(pl):	Demon authd do Cyrus SASL
Group:		Daemons
Requires(post,postun):	/sbin/chkconfig
Requires:	%{name} = %{version}-%{release}

%description saslauthd
Cyrus SASL authd.

%description saslauthd -l pl
Demon authd do Cyrus SASL.

%package pwcheck
Summary:	Cyrus SASL pwcheck helper
Summary(pl):	Program pomocniczy pwcheck do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pwcheck
Cyrus SASL pwcheck helper.

%description pwcheck -l pl
Program pomocniczy pwcheck do Cyrus SASL.

%package sasldb
Summary:	Cyrus SASL sasldb plugin
Summary(pl):	Wtyczka sasldb do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sasldb
Cyrus SASL sasldb plugin.

%description sasldb -l pl
Wtyczka sasldb do Cyrus SASL.

%package mysql
Summary:	Cyrus SASL MySQL plugin
Summary(pl):	Wtyczka MySQL do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description mysql
Cyrus SASL MySQL plugin.

%description mysql -l pl
Wtyczka MySQL do Cyrus SASL.

%package pgsql
Summary:	Cyrus SASL PostgreSQL plugin
Summary(pl):	Wtyczka PostgreSQL do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description pgsql
Cyrus SASL PostgreSQL plugin.

%description pgsql -l pl
Wtyczka PostgreSQL do Cyrus SASL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

cd doc
echo "cyrus-sasl complies with the following RFCs:" > rfc-compliance
ls rfc*.txt >> rfc-compliance
rm -f rfc*.txt
cd ..

rm -rf autom4te.cache saslauthd/autom4te.cache
# acinclude.m4 contains only old libtool.m4
rm -f acinclude.m4 libtool config/libtool.m4 saslauthd/acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I cmulocal -I config
%{__autoheader}
%{__automake}
%{__autoconf}

cd saslauthd
%{__libtoolize}
%{__aclocal} -I ../cmulocal -I ../config -I config
%{__autoheader}
%{__automake}
%{__autoconf}
cd ..

%configure \
	--disable-krb4 \
	%{!?with_gssapi: --disable-gssapi} \
	%{?with_gssapi: --enable-gssapi --with-gss_impl=heimdal} \
	--enable-login \
	--enable-sql \
	%{?with_srp: --enable-srp} \
	--enable-static \
	--with-plugindir=%{_libdir}/sasl2 \
	--with-configdir=%{_sysconfdir} \
	--with-dblib=berkeley \
	--with-dbpath=/var/lib/sasl2/sasl.db \
	%{?with_ldap: --with-ldap=%{_prefix}} \
	%{?with_mysql: --with-mysql=%{_prefix}} \
	%{?with_pgsql: --with-pgsql=%{_prefix}} \
	--with-pam \
	%{?with_pwcheck: --with-pwcheck=/var/lib/sasl2} \
	--with-saslauthd=/var/lib/sasl2
%{__make}

%{__make} -C saslauthd testsaslauthd
%{__make} -C saslauthd saslcache

cd doc
RFCLIST=`grep 'rfc.\+\.txt' rfc-compliance`
for i in $RFCLIST; do
	RFCDIR=../RFC/text/`echo $i | sed -e 's:^rfc::' -e 's:..\.txt$::' `00
	echo -e ',s:'$i':'$RFCDIR/$i'\n,w\nq' | ed index.html
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/sasl2,%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
		$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	sasldir=%{_libdir}/sasl2 \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_mandir}/cat*
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/*.{la,a}

install utils/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install saslauthd/saslauthd.mdoc $RPM_BUILD_ROOT%{_mandir}/man8/saslauthd.8

ln -sf libsasl2.so $RPM_BUILD_ROOT%{_libdir}/libsasl.so

touch $RPM_BUILD_ROOT/var/lib/sasl2/sasl.db

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/saslauthd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/saslauthd
install %{SOURCE3} ./cyrus.pam

install saslauthd/{testsaslauthd,saslcache} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post saslauthd
/sbin/chkconfig --add saslauthd
if [ -f /var/lock/subsys/saslauthd ]; then
	/etc/rc.d/init.d/saslauthd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/saslauthd start\" to start saslauthd."
fi

%preun saslauthd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/saslauthd ]; then
		/etc/rc.d/init.d/saslauthd stop 1>&2
	fi
	/sbin/chkconfig --del saslauthd
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%doc doc/{ONEWS,TODO,*.txt,*.html,*.fig,rfc-compliance}
%dir %{_sysconfdir}
%dir %{_libdir}/sasl2
%dir /var/lib/sasl2
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_sbindir}/sasldblistusers2
%attr(755,root,root) %{_sbindir}/saslpasswd2

%attr(640,root,mail) %ghost %config(noreplace) %verify(not mtime md5 size) /var/lib/sasl2/sasl.db
%{_mandir}/man8/sasldblistusers2.*
%{_mandir}/man8/saslpasswd2.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sasl
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files anonymous
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libanonymous.so*

%if %{with gssapi}
%files gssapi
%defattr(644,root,root,755)
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

%files otp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libotp.so*

%files plain
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libplain.so*

%files sasldb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsasldb.so*

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsql*.so*
%endif

%if %{with pgsql}
%files pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsql*.so*
%endif

%if %{with srp}
%files srp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsrp.so*
%endif

%if %{with x509}
%files x509
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libx509.so*
%endif

%if %{with pwcheck}
%files pwcheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pwcheck
%endif

%files saslauthd
%defattr(644,root,root,755)
%doc cyrus.pam
%attr(755,root,root) %{_sbindir}/saslauthd
%attr(755,root,root) %{_sbindir}/testsaslauthd
%attr(755,root,root) %{_sbindir}/saslcache
%attr(754,root,root) /etc/rc.d/init.d/saslauthd
%config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/saslauthd
%{_mandir}/man8/saslauthd.*
