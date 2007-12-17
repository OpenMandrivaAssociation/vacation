%define name vacation 
%define version 1.2.6.1
%define release 5

Summary: Automatic mail answering program for Linux
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
License: GPL
Group: Networking/Mail
Source: http://download.sourceforge.net/vacation/%{name}-%{version}.tar.bz2
URL: http://sourceforge.net/projects/vacation/
Buildrequires: gdbm-devel
Requires: sendmail-command

%description 
Vacation is the automatic mail answering program found
on many Unix systems. This version works with the sendmail 
restricted shell.

%prep
%setup -q -n %{name}

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

install -s -m 755 vacation        $RPM_BUILD_ROOT%{_bindir}/vacation
install -m 755 vaclook         $RPM_BUILD_ROOT%{_bindir}/vaclook
install -m 444 vacation.man    $RPM_BUILD_ROOT%{_mandir}/man1/vacation.1
install -m 444 vaclook.man     $RPM_BUILD_ROOT%{_mandir}/man1/vaclook.1

%post
if [ -d /etc/smrsh/ ] ; then 
  ln -s /usr/bin/vacation /etc/smrsh
fi

%postun
if [ -L /etc/smrsh/vacation ] ; then 
  rm -f /etc/smrsh/vacation
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root) 
%{_bindir}/vacation
%{_bindir}/vaclook
%{_mandir}/*/*
%doc COPYING README README.smrsh ChangeLog

