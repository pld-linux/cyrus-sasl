%define name cyrus-sasl
%define version 1.5.3
%define release 2
%define prefix /usr

Summary: The SASL library API for the Cyrus mail system.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: distributable
Group: System Environment/Libraries
Source: ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/cyrus-sasl-1.5.3.tar.gz
URL: http://asg.web.cmu.edu/cyrus/imapd/
Buildroot:/var/tmp/%{name}-root
Provides: libsasl

%description
The cyrus-sasl package contains the SASL library API implementation
for the Cyrus mail system.

%prep
%setup -n %{name}-%{version}

%build
(cd $RPM_BUILD_DIR/cyrus-sasl-1.5.3
./configure --prefix=%{prefix}
make)

%install
rm -rf $RPM_BUILD_ROOT
(cd $RPM_BUILD_DIR/cyrus-sasl-1.5.3
	make prefix=$RPM_BUILD_ROOT%{prefix} install )

strip -s $RPM_BUILD_ROOT%{prefix}/sbin/* || :
chmod 755 $RPM_BUILD_ROOT%{prefix}/lib/sasl/*
chmod 755 $RPM_BUILD_ROOT%{prefix}/lib/libsasl.la 
chmod 755 $RPM_BUILD_ROOT%{prefix}/lib/libsasl.so.5.1.0
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-,root,root)
%{prefix}/include/*.h
%{prefix}/lib/sasl/*
%{prefix}/lib/libsasl*
%dir %{prefix}/lib/sasl
%{prefix}/man/man1/sasl_client.1
%{prefix}/man/man1/sasl_server.1
%{prefix}/man/man8/saslpasswd.8
%{prefix}/sbin/saslpasswd

%changelog
* Mon Aug 30 1999 Tim Powers <timp@redhat.com>
- changed group

* Fri Aug 13 1999 Tim Powers <timp@redhat.com>
- first build for Powertools
