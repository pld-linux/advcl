%include	/usr/lib/rpm/macros.perl
%define	rname	acl
Summary:	Advanced Color Logs
Summary(pl):	Advanced Color Logs - program koloruj±cy logi
Name:		advcl
Version:	0.7.0
Release:	4
License:	GPL
Group:		Applications/Console
Source0:	http://linuxrc.net/linuxrc.org/projects/acl/%{rname}-%{version}.tar.gz
# Source0-md5:	978e4da7eec020aea1efff9c2ab953f8
Patch0:		%{name}-config.patch
URL:		http://linuxrc.net/linuxrc.org/projects/acl/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
acl is a perl script that colorizes system logs. Inspired by
ColorLogs, acl (Advanced Color Logs) has advanced parsing
capabilities.

%description -l pl
acl to skrypt napisany w perlu, koloruj±cy logi systemowe.
Zainspirowany programem ColorLogs, acl (Advanced Color Logs) posiada
bardziej rozbudowane mo¿liwo¶ci parsowania.

%prep
%setup -q -n %{rname}-%{version}
%patch -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install acl.pl		$RPM_BUILD_ROOT%{_bindir}/acl
install acl.conf	$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO
%attr(755,root,root) %{_bindir}/acl
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/acl.conf
