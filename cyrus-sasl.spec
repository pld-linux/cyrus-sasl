# TODO:
# - possible SECURITY: http://securitytracker.com/alerts/2004/Oct/1011568.html
#
# Conditional builds:
# x509 - build x509 pluggin
# srp - build srp pluggin
# _with_mysql - with mysql support
# _with_ldap - with ldap support
# _with_pwcheck - build pwcheck pluggin
#		
Summary:	The SASL library API for the Cyrus mail system
Summary(pl):	Biblioteka Cyrus SASL
Summary(pt_BR):	Implementação da API SASL
Summary(ru):	âÉÂÌÉÏÔÅËÁ Cyrus SASL
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ Cyrus SASL
Name:		cyrus-sasl
Version:	1.5.27
Release:	16
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/OLD-VERSIONS/sasl/%{name}-%{version}.tar.gz
# Source0-md5:	76ea426e2e2da3b8d2e3a43af5488f3b
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
Patch6:		saslauthd-man.diff
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db3-devel >= 3.1.17-8
BuildRequires:	pam-devel
BuildRequires:	openssl-devel >= 0.9.6m
BuildRequires:	libtool	>= 1.4
%{?_with_mysql:BuildRequires: mysql-devel}
%{?_with_ldap:BuildRequires: openldap-devel}
URL:		http://asg.web.cmu.edu/sasl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sasl

%description
This is an implemention of the SASL API, useful for adding
authentication, authorization, and security to network protocols. The
SASL protocol itself is documented in rfc2222; the API standard is a
work in progress.

%description -l pl
Pakiet cyrus-sasl zawiera implementacjê biblioteki API SASL dla
systemu poczty elektronicznej Cyrusa. Biblioteka ta jest przydatna
tak¿e do dodawania uwierzytelniania, autoryzacji oraz zwiêkszania
bezpieczeñstwa protoko³ów sieciowych. Sam protokó³ SASL jest opisany
w RFC 2222; standaryzacja API jest w toku.

%description -l pt_BR
Esta é uma implementação da API SASL, útil para acrescentar autenticação,
autorização e seguança (criptografia) para protocolos de rede. O
protocolo SASL está documentado na RFC 2222. A API "padrão" ainda está
em desenvolvimento.

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
Requires:	%{name} = %{version}
Requires:	db3-devel
Requires:	pam-devel

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
Requires:	%{name}-devel = %{version}

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
Requires:	%{name} = %{version}

%description cram-md5
This plugin implements the SASL CRAM-MD5 mechanism. CRAM-MD5 is the
mandatory-to-implement authentication mechanism for a number of
protocols; it uses MD5 with a challenge/response system to
authenticate the user.

%description cram-md5 -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu CRAM-MD5 do Cyrus SASL. CRAM-MD5
jest obowi±zkowym do zaimplementowania mechanizmem uwierzytelniania
dla wielu protoko³ów; do uwierzytelnienia u¿ytkownika u¿ywa MD5 wraz
z systemem challenge/response.

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
Requires:	%{name} = %{version}

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
Este plugin implementa a última versão da especificação do
mecanismo SASL DIGEST-MD5. Embora ainda não esteja finalizado,
DIGEST-MD5 provavelmente será o novo sistema de autenticação obrigatório
para protocolos novos. Ele é baseado na autenticação md5 digest
desenvolvida para HTTP.

%package plain
Summary:	Plain Cyrus SASL plugin
Summary(pl):	Wtyczka plain do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL PLAIN
Group:		Libraries
Requires:	%{name} = %{version}

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
Este plugin implementa o mecanismo SASL PLAIN. Embora inseguro,
este mecanismo é útil durante transições para novos mecanismos de
segurança, pois é o único esquema que fornece uma cópia da senha
do usuário para o servidor.

%package anonymous
Summary:	Anonymous Cyrus SASL plugin
Summary(pl):	Wtyczka anonymous do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL ANONYMOUS
Group:		Libraries
Requires:	%{name} = %{version}

%description anonymous
This plugin implements the SASL ANONYMOUS mechanism,
used for anonymous authentication.

%description anonymous -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu ANONYMOUS do Cyrus SASL. S³u¿y do
anonimowego uwierzytelniania.

%description anonymous -l pt_BR
Este plugin implementa o mecanismo SASL ANONYMOUS, usado
para autenticação anônima.

%package login
Summary:	Unsupported Login Cyrus SASL plugin
Summary(pl):	Nie wspierana wtyczka Login do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}

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
Requires:	%{name} = %{version}

%description srp
This plugin implements the SASL SRP mechanism, based on the
Secure Remote Password protocol. This mechanism performs mutual
authentication and can provide a security layer with replay
detection, integrity protection and/or condifentiality
protection.

%description srp -l pl
Wtyczka dodaj±ca obs³ugê mechanizmu SRP do Cyrus SASL. Bazuje na
protokole Secure Remote Password. Ten mechanizm dokonuje wzajemnego
uwierzytelnienia i mo¿e dodawaæ warstwê bezpieczeñstwa z wykrywaniem
powtarzania, zabezpieczeniem integralno¶ci i/lub poufno¶ci.

%description srp -l pt_BR
Este plugin implementa o mecanismo SASL SRP, baseado no protocolo SRP (Secure
Remote Password). Este mecanismo oferece autenticação mútua (do cliente e do
servidor) e pode prover uma camada de segurança com detecção de ataques de
replay, garantia de integridade e/ou confidencialidade.

%package x509
Summary:	x509 Cyrus SASL plugin
Summary(pl):	Wtyczka x509 do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}

%description x509
x509 Cyrus SASL plugin.

%description x509 -l pl
Wtyczka x509 do Cyrus SASL.

%package saslauthd
Summary:	Cyrus SASL authd
Summary(pl):	Demon authd do Cyrus SASL
Group:		Libraries
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
Requires:	%{name} = %{version}

%description pwcheck
Cyrus SASL pwcheck helper.

%description pwcheck -l pl
Program pomocniczy pwcheck do Cyrus SASL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

%build
rm -f config/missing
%{__libtoolize}
%{__aclocal} -I cmulocal
%{__autoheader}
automake -a
%{__autoconf}
LDFLAGS="%{rpmldflags} -ldl"; export LDFLAGS
%configure \
	--disable-krb4 \
	--disable-gssapi \
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%doc COPYING testing.txt NEWS TODO README doc/*.txt doc/*.html
%dir %{_sysconfdir}
%dir %{_libdir}/sasl
%dir /var/lib/sasl
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_sbindir}/sasldblistusers
%attr(755,root,root) %{_sbindir}/saslpasswd

%attr(640,root,mail) %ghost %config(noreplace) %verify(not mtime md5 size) /var/lib/sasl/sasl.db
%{_mandir}/man[18]/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_mandir}/man3/*

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
%attr(754,root,root) /etc/rc.d/init.d/saslauthd
%config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/saslauthd
%config(noreplace) %verify(not mtime md5 size) /etc/pam.d/cyrus
