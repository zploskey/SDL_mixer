Summary: Simple DirectMedia Layer - Sample Mixer Library
Name: SDL_mixer
Version: 1.2.5
Release: 10.1
Source: %{name}-%{version}.tar.gz
Patch1: SDL_mixer-1.0.6-redhat.patch
Patch2: SDL_mixer-1.2.4-64bit.patch
Patch3: SDL_mixer-ppc64.patch
Patch4: SDL_mixer-1.2.5-bad_code.patch
Patch5: SDL_mixer-1.2.5-autofoo.patch
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.libsdl.org/projects/SDL_mixer/
Prefix: %{_prefix}
BuildRequires: SDL-devel >= 1.2.4-1 
BuildRequires: libvorbis-devel
Requires: SDL >= 1.2.4-1

%description
A simple multi-channel audio mixer for SDL.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and Ogg Vorbis
libraries.

%package devel
Summary: Libraries, includes and more to develop SDL applications using the SDL mixer.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: SDL-devel >= 1.2.4-1

%description devel
Development files for SDL_mixer, a simple multi-channel audio mixer for SDL.
It supports 4 channels of 16 bit stereo audio, plus a single channel
of music, mixed by the popular MikMod MOD, Timidity MIDI and Ogg Vorbis
libraries.

You need SDL_mixer-devel if you want to compile an application using SDL_mixer.

%prep
%setup -q
%patch1 -p1 -b .redhat
%patch2 -p1 -b .64bit
%patch3 -p1 -b .ppc64
%patch4 -p1 -b .bad_code
%patch5 -p1 -b .autofoo

%build
# replaced by patch
#libtoolize --copy --force
#aclocal
#autoconf
#automake --foreign --include-deps --add-missing --force-missing --copy -a
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
/usr/bin/install -d $RPM_BUILD_ROOT/usr/bin
./libtool --mode=install /usr/bin/install -c playmus $RPM_BUILD_ROOT/usr/bin
./libtool --mode=install /usr/bin/install -c playwave $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%{_bindir}/playmus
%{_bindir}/playwave
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*a
%{_libdir}/lib*.so
%{_includedir}/SDL

%changelog
* Thu Jun 16 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.5-10.1
- Make -devel package require exact release of main package (this
  is particularly important for API changes such as in 1.2.5-9).

* Thu Jun  9 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.2.5-9
- Bring back Ogg support (BuildRequire libvorbis-devel).
- Add SDL-devel dependency to -devel.
- Improve description.

* Thu May 26 2005 Bill Nottingham <notting@redhat.com> 1.2.5-7
- rebuild

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 1.2.5-5
- rebuild

* Thu Sep 30 2004 Thomas Woerner <twoerner@redhat.com> 1.2.5-4
- moved to new autofoo utils

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr 22 2004 Thomas Woerner <twoerner@redhat.com> 1.2.5-2
- fixed bad code in effect_position.c
- cleaned up build

* Tue Mar  9 2004 Thomas Woerner <twoerner@redhat.com> 1.2.5-1
- new version 1.2.5
- cleaned up spec file
- installing playmus and playwave by hand (not installed automatically anymore)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 17 2003 Elliot Lee <sopwith@redhat.com> 1.2.4-8
- ppc64 fix

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 19 2002 Tim Powers <timp@redhat.com>
- bump and rebuild
- use pushd and popd instead of cd'ing into the buildroot

* Sat Oct 12 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add 64bit patch

* Wed Aug 28 2002 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jul 18 2002 Bill Nottingham <notting@redhat.com> 1.2.4-4
- build against current libvorbis

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraeenzer <bero@redhat.com> 1.2.4-1
- 1.2.4
- clean up spec file

* Fri Mar  1 2002 Than Ngo <than@redhat.com> 1.2.1-4
- rebuild in new env

* Thu Jan 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-3
- Rebuild to get rid of superfluous dependencies
  [dependencies removed from SDL-1.2.3-5]

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jan  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.2.1-1
- Require arts-devel rather than the obsolete kdelibs-sound-devel
- Update to 1.2.1
- Fix build with current auto* tools

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add more build dependencies (#49828)

* Tue Jul 10 2001 Elliot Lee <sopwith@redhat.com>
- Rebuild

* Fri Jun 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- do not delete acinclude.m4 in spec file

* Sun Apr 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.2.0

* Tue Jan 16 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Require arts, not kdelibs-sound

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.0
- Fix %%post, %%postun
- Fix summary line for -devel

* Wed Nov 29 2000 Than Ngo <than@redhat.com>
- added ftp site

* Mon Nov 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.0.6
- Requires: smpeg
- BuildRequires: SDL-devel
- Look for timidity.cfg in the right place

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt lkto fix bad dir perms

* Tue Nov 14 2000 Tim Powers <timp@redhat.com>
- updated to 1.0.6

* Wed Aug 02 2000 Than Ngo <than@redhat.de>
- move libSDL_mixer.so in SDL_mixer-devel

* Tue Aug 1 2000 Tim Powers <timp@redhat.com>
- added post and postun sections with /sbin/ldconfig

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt
- use RPM macros

* Mon Jun 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial build for Red Hat Powertools
- fix build with current libtool

* Wed Jan 19 2000 Sam Lantinga 
- converted to get package information from configure

* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file

