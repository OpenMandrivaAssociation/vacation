%define debug_package %{nil}

Summary:  Automatic mail answering program for Linux
Name:     vacation 
Version:  1.2.7.0
Release:  4
License:  GPL
Group:    Networking/Mail
Source:   http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:      https://sourceforge.net/projects/vacation/
Requires: sendmail-command
BuildRequires: gdbm-devel

%description 
Vacation is the automatic mail answering program found
on many Unix systems. This version works with the sendmail 
restricted shell.

%prep
%setup -q

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -s -m 755 vacation        %{buildroot}%{_bindir}/vacation
install -m 755 vaclook         %{buildroot}%{_bindir}/vaclook
install -m 444 vacation.man    %{buildroot}%{_mandir}/man1/vacation.1
install -m 444 vaclook.man     %{buildroot}%{_mandir}/man1/vaclook.1

%post
if [ -d /etc/smrsh/ ] ; then 
  ln -s /usr/bin/vacation /etc/smrsh
fi

%postun
if [ -L /etc/smrsh/vacation ] ; then 
  rm -f /etc/smrsh/vacation
fi

%files
%{_bindir}/vacation
%{_bindir}/vaclook
%{_mandir}/*/*
%doc COPYING README README.smrsh ChangeLog
