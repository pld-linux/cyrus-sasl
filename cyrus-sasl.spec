#
# TODO:
# - add ldap plugin from openldap sources
#
# Conditional build:
# _with_srp		- build srp pluggin
# _without_myslq	- don't build mysql pluggin
# _without_ldap		- disable LDAP support for sasluthd
#
Summary:	The SASL library API for the Cyrus mail system
Summary(pl):	Biblioteka Cyrus SASL
Summary(pt_BR):	Implementa��o da API SASL
Summary(ru):	���������� Cyrus SASL
Summary(uk):	��̦����� Cyrus SASL
Name:		cyrus-sasl
Version:	2.1.13
Release:	0.2
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.andrew.cmu.edu/pub/cyrus/%{name}-%{version}.tar.gz
# Source0-md5: 1114d59d970791932e96de8557472672
Source1:	saslauthd.init
Source2:	saslauthd.sysconfig
Source3:	%{name}.pam
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-nolibs.patch
Patch2:		%{name}-lt14d.patch
Patch3:		%{name}-do_dlopen.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	ed
BuildRequires:	libtool	>= 1.4
%{!?_without_mysql:BuildRequires: mysql-devel}
%{!?_without_ldap:BuildRequires: openldap-devel}
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pam-devel
URL:		http://asg.web.cmu.edu/sasl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/sasl

%description
This is an implementation of the SASL API, useful for adding
authentication, authorization, and security to network protocols. The
SASL protocol itself is documented in rfc2222; the API standard is a
work in progress.

%description -l pl
Pakiet cyrus-sasl zawiera implementacj� biblioteki API SASL dla
systemu poczty elektronicznej Cyrusa. Biblioteka ta jest przydatna
tak�e do dodawania uwierzytelniania, autoryzacji oraz zwi�kszania
bezpiecze�stwa protoko��w sieciowych. Sam protok� SASL jest opisany w
RFC 2222; standaryzacja API jest w toku.

%description -l pt_BR
Esta � uma implementa��o da API SASL, �til para acrescentar
autentica��o, autoriza��o e seguan�a (criptografia) para protocolos de
rede. O protocolo SASL est� documentado na RFC 2222. A API "padr�o"
ainda est� em desenvolvimento.

%description -l ru
����� cyrus-sasl �������� ���������� Cyrus SASL. SASL - ��� Simple
Authentication and Security Layer, ����� ��� ���������� ���������
������������ � ����������, ���������� �� �����������.

%description -l uk
����� cyrus-sasl ͦ����� ���̦��æ� Cyrus SASL. SASL - �� Simple
Authentication and Security Layer, ����� ��� ������� Ц�������
���������æ� �� �������̦�, ��������� �� �'��������.

%package devel
Summary:	Header files and documentation for cyrus-sasl
Summary(pl):	Pliki nag��wkowe i dokumentacja dla cyrus-sasl
Summary(pt_BR):	Exemplos e arquivos para desenvolvimento com SASL
Summary(ru):	����� ��� ���������������� � ����������� Cyrus SASL
Summary(ru):	����� ��� ������������� � ¦�̦������ Cyrus SASL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This includes the header files and documentation needed to develop
applications which use SASL.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla cyrus-sasl.

%description devel -l pt_BR
Este pacote inclui os arquivos de cabe�alho e documenta��o necess�rios
para desenvolver aplicativos que usem SASL.

%description devel -l ru
������ � ����������, ����������� ��� ���������� ����������,
������������ Cyrus SASL.

%description devel -l uk
������ �� ¦�̦�����, ����Ȧ�Φ ��� �������� �������, ��
�������������� Cyrus SASL.

%package static
Summary:	Static cyrus-sasl libraries
Summary(pl):	Statyczne biblioteki cyrus-sasl
Summary(ru):	����������� ���������� Cyrus SASL
Summary(uk):	������Φ ¦�̦����� Cyrus SASL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static cyrus-sasl libraries.

%description static -l pl
Statyczne biblioteki cyrus-sasl.

%description static -l ru
����������� ����������, ����������� ��� ���������� ����������,
������������ Cyrus SASL.

%description static -l uk
������Φ ¦�̦�����, ����Ȧ�Φ ��� �������� �������, �� ��������������
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
Wtyczka dodaj�ca obs�ug� mechanizmu CRAM-MD5 do Cyrus SASL. CRAM-MD5
jest obowi�zkowym do zaimplementowania mechanizmem uwierzytelniania
dla wielu protoko��w; do uwierzytelnienia u�ytkownika u�ywa MD5 wraz z
systemem challenge/response.

%description cram-md5 -l pt_BR
Este plugin implementa o mecanismo SASL CRAM-MD5. CRAM-MD5 � o
mecanismo de autentica��o obrigat�rio de ser implementado para v�rios
protocolos: ele usa MD5 com um sistema de desafio/resposta para
autenticar o usu�rio.

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
Wtyczka dodaj�ca najnowsz� wersj� mechanizmu DIGEST-MD5 do Cyrus SASL.
Pomimo tego, �e nie jest jeszcze uko�czony, najprawdopodobniej stanie
si� obowi�zkowym do zaimplementowania systemem uwierzytelniania we
wszystkich nowych protoko�ach. Bazuje na systemie uwierzytelniania
Digest-MD5 zaprojektowanym dla HTTP.

%description digest-md5 -l pt_BR
Este plugin implementa a �ltima vers�o da especifica��o do mecanismo
SASL DIGEST-MD5. Embora ainda n�o esteja finalizado, DIGEST-MD5
provavelmente ser� o novo sistema de autentica��o obrigat�rio para
protocolos novos. Ele � baseado na autentica��o md5 digest
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
Wtyczka dodaj�ca obs�ug� mechanizmu PLAIN do Cyrus SASL. Pomimo tego,
�e nie jest bezpieczny, PLAIN jest przydatny przy przechodzeniu na
nowe mechanizmu bezpiecze�stwa, jako �e jest to jedyny mechanizm,
kt�ry udost�pnia serwerowi kopi� has�a u�ytkownika.

%description plain -l pt_BR
Este plugin implementa o mecanismo SASL PLAIN. Embora inseguro, este
mecanismo � �til durante transi��es para novos mecanismos de
seguran�a, pois � o �nico esquema que fornece uma c�pia da senha do
usu�rio para o servidor.

%package anonymous
Summary:	Anonymous Cyrus SASL plugin
Summary(pl):	Wtyczka anonymous do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL ANONYMOUS
Group:		Libraries
Requires:	%{name} = %{version}

%description anonymous
This plugin implements the SASL ANONYMOUS mechanism, used for
anonymous authentication.

%description anonymous -l pl
Wtyczka dodaj�ca obs�ug� mechanizmu ANONYMOUS do Cyrus SASL. S�u�y do
anonimowego uwierzytelniania.

%description anonymous -l pt_BR
Este plugin implementa o mecanismo SASL ANONYMOUS, usado para
autentica��o an�nima.

%package login
Summary:	Unsupported Login Cyrus SASL plugin
Summary(pl):	Nie wspierana wtyczka Login do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}

%description login
Unsupported LOGIN Cyrus SASL plugin.

%description login -l pl
Wtyczka dodaj�ca obs�ug� nie wspieranego mechanizmu LOGIN do Cyrus
SASL.

%package srp
Summary:	SRP Cyrus SASL plugin
Summary(pl):	Wtyczka SRP do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL SRP
Group:		Libraries
Requires:	%{name} = %{version}

%description srp
This plugin implements the SASL SRP mechanism, based on the Secure
Remote Password protocol. This mechanism performs mutual
authentication and can provide a security layer with replay detection,
integrity protection and/or condifentiality protection.

%description srp -l pl
Wtyczka dodaj�ca obs�ug� mechanizmu SRP do Cyrus SASL. Bazuje na
protokole Secure Remote Password. Ten mechanizm dokonuje wzajemnego
uwierzytelnienia i mo�e dodawa� warstw� bezpiecze�stwa z wykrywaniem
powtarzania, zabezpieczeniem integralno�ci i/lub poufno�ci.

%description srp -l pt_BR
Este plugin implementa o mecanismo SASL SRP, baseado no protocolo SRP
(Secure Remote Password). Este mecanismo oferece autentica��o m�tua
(do cliente e do servidor) e pode prover uma camada de seguran�a com
detec��o de ataques de replay, garantia de integridade e/ou
confidencialidade.

%package otp
Summary:	OTP Cyrus SASL plugin
Summary(pl):	Wtyczka OTP do Cyrus SASL
Summary(pt_BR):	Mecanismo SASL OTP
Group:		Libraries
Requires:	%{name} = %{version}

%description otp
This plugin implements the SASL OTP (One Time Password) mechanism.

%description otp -l pl
Wtyczka dodaj�ca obs�ug� mechanizmu OTP (has�a jednorazowe) do Cyrus
SASL.

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
Requires(post,postun):	/sbin/chkconfig
Requires:	%{name} = %{version}

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

%package sasldb
Summary:	Cyrus SASL sasldb plugin
Summary(pl):	Wtyczka sasldb do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}

%description sasldb
Cyrus SASL sasldb plugin.

%description sasldb -l pl
Wtyczka sasldb do Cyrus SASL.

%package mysql
Summary:	Cyrus SASL mysql plugin
Summary(pl):	Wtyczka mysql do Cyrus SASL
Group:		Libraries
Requires:	%{name} = %{version}

%description mysql
Cyrus SASL mysql plugin.

%description mysql -l pl
Wtyczka mysql do Cyrus SASL.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cd doc
echo "cyrus-sasl complies with the following RFCs:" > rfc-compliance
ls rfc*.txt >> rfc-compliance
rm -f rfc*.txt
cd ..

%build
# acinclude.m4 contains only old libtool.m4
rm -f acinclude.m4 config/missing
%{__libtoolize}
%{__aclocal} -I cmulocal -I config
%{__autoheader}
%{__automake}
%{__autoconf}

cd saslauthd
%{__aclocal} -I ../cmulocal -I ../config -I config
%{__autoheader}
automake -a
%{__autoconf}
cd ..

LDFLAGS="%{rpmldflags} -ldl"; export LDFLAGS
%configure \
	--enable-static \
	--enable-login \
	%{?_with_srp:--enable-srp} \
	%{?!_without_mysql: --with-mysql=%{_prefix}} \
	%{?!_without_ldap: --with-ldap=%{_prefix}} \
	%{?_with_pwcheck: --with-pwcheck=/var/lib/sasl2} \
	--with-saslauthd=/var/lib/sasl2 \
	--with-pam \
	--with-dblib=berkeley \
	--with-dbpath=/var/lib/sasl2/sasl.db \
	--with-configdir=%{_sysconfdir} \
	--disable-krb4 \
	--disable-gssapi
%{__make}

cd doc
RFCLIST=`grep 'rfc.\+\.txt' rfc-compliance`
for i in $RFCLIST; do
	RFCDIR=../RFC/text/`echo $i | sed -e 's:^rfc::' -e 's:..\.txt$::' `00
	echo -e ',s:'$i':'$RFCDIR/$i'\n,w\nq' | ed index.html
done
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/sasl2,%{_sysconfdir},/etc/{rc.d/init.d,sysconfig}} \
		$RPM_BUILD_ROOT%{_mandir}/man8
%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_mandir}/cat*
rm -f $RPM_BUILD_ROOT%{_libdir}/sasl2/*.{la,a}

install {utils,saslauthd}/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf libsasl2.so $RPM_BUILD_ROOT%{_libdir}/libsasl.so

touch $RPM_BUILD_ROOT/var/lib/sasl2/sasl.db

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/saslauthd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/saslauthd
install %{SOURCE3} ./cyrus.pam

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

%if %{!?_without_mysql:1}%{?_without_mysql:0}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libmysql*.so*
%endif

%if %{?_with_srp:1}%{?!_with_srp:0}
%files srp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libsrp.so*
%endif

%if %{?_with_x509:1}%{?!_with_x509:0}
%files x509
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/sasl2/libx509.so*
%endif

%if %{?_with_pwcheck:1}%{?!_with_pwcheck:0}
%files pwcheck
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/pwcheck
%endif

%files saslauthd
%defattr(644,root,root,755)
%doc cyrus.pam
%attr(755,root,root) %{_sbindir}/saslauthd
%attr(754,root,root) /etc/rc.d/init.d/saslauthd
%config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/saslauthd
%{_mandir}/man8/saslauthd.*
