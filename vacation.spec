%define name vacation 
%define version 1.2.7.0
%define release 2

Summary: Automatic mail answering program for Linux
Name: %{name}
Version: %{version}
Release: %mkrel %{release}
License: GPL
Group: Networking/Mail
Source: http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
URL: http://sourceforge.net/projects/vacation/
Buildrequires: gdbm-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: sendmail-command

%description 
Vacation is the automatic mail answering program found
on many Unix systems. This version works with the sendmail 
restricted shell.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}

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

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root) 
%{_bindir}/vacation
%{_bindir}/vaclook
%{_mandir}/*/*
%doc COPYING README README.smrsh ChangeLog



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7.0-2mdv2011.0
+ Revision: 615384
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.7.0-1mdv2010.1
+ Revision: 469120
- new version 1.2.7.0
- remove CFLAGS="$RPM_OPT_FLAGS" (already included in the Makefile)
- $RPM_BUILD_ROOT -> %%{buildroot}

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.2.6.1-6mdv2010.0
+ Revision: 434624
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.6.1-5mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import vacation


* Sun Jul 09 2006 Emmanuel Andry <eandry@mandriva.org> 1.2.6.1-5mdv2007.0
- rebuild

* Fri Jul  1 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.2.6.1-4mdk
- requires sendmail-command
- use mkrel

* Sat Apr 16 2005 Giuseppe Ghib� <ghibo@mandrakesoft.com> 1.2.6.1-3mdk
- Fixed deps for X86-64.

* Tue May 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.6.1-2mdk
- buildrequires

* Mon Mar 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2.6.1-1mdk
- 1.2.6.1

* Sun Nov 11 2001 Daouda LO <daouda@mandrakesoft.com> 1.2.6-1mdk
- intial mdk package (spec from tarball)

* Sat Nov 10 2001 Devon <devon@tuxfan.homeip.net>
- upgrade to version 1.2.6
* Wed Sep 19 2001 Devon <devon@tuxfan.homeip.net>
- added %%post link /etc/smrsh to /usr/bin/vacation
- added %%postun deletion of /etc/smrsh/vacation
- defined a umask of 022 fix permissions on created files.
  $HOME/.forward was created group writable, smrsh refused
  to run in that case. See vacation-1.2.2-permissions.patch

* Mon Aug 07 2000 Than Ngo <than@redhat.de>
- fix specfile and patch file to rebuilt

* Mon Aug 07 2000 Michael Stefaniuc <mstefani@redhat.com>
- upgraded to 1.2.2
- fixed security fix

* Wed Aug 02 2000 Than Ngo <than@redhat.de>
- fix manpath (Bug #15070)

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Sun Jul 16 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add security fix

* Mon Jul 10 2000 Than Ngo <than@redhat.de>
- fix problem (it won't include the .vacation.msg) (bug #13572)
- use RPM macros

* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun May 28 2000 Ngo Than <than@redhat.de>
- rebuild for 7.0
- put man pages in correct place
- cleanup specfile
- fix Summary

* Fri Dec 10 1999 Ngo Than <than@redhat.de>
- initial RPM for powertools-6.2
