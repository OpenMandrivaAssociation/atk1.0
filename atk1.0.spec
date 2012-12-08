%define enable_gtkdoc	0

%define api		1.0
%define major	0
%define pkgname	atk
%define libname %mklibname %{pkgname} %{api} %{major}
%define girname %mklibname %{pkgname}-gir %{api}
%define develname %mklibname -d %{name}

Summary:	Accessibility features for Gtk+
Name:		%{pkgname}%{api}
Version:	2.6.0
Release:	1
License:	LGPLv2+
Group:		Accessibility
Url:		http://developer.gnome.org/projects/gap/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/2.6/%{pkgname}-%{version}.tar.xz

%if %{enable_gtkdoc}
BuildRequires:	gtk-doc >= 1.11-3
%endif
BuildRequires: pkgconfig(glib-2.0) >= 2.5.7
BuildRequires: pkgconfig(gobject-introspection-1.0)

%description
Accessibility means providing system infrastructure that allows add-on
assistive software to transparently provide specalized input and ouput
capabilities. For example, screen readers allow blind users to navigate
through applications, determine the state of controls, and read text via
text to speech conversion. On-screen keyboards replace physical
keyboards, and head-mounted pointers replace mice.

ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

%package common
Summary:	Data files used by atk
Group:		System/Libraries

%description common
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

This package contains data used by atk library.

%package -n %{libname}
Summary:	Accessibility features for Gtk+
Group:		System/Libraries
Suggests:	%{name}-common >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Conflicts:	gir-repository < 0.6.5-4

%description -n %{libname}
Accessibility means providing system infrastructure that allows add-on
assistive software to transparently provide specalized input and ouput
capabilities. For example, screen readers allow blind users to navigate
through applications, determine the state of controls, and read text via
text to speech conversion. On-screen keyboards replace physical
keyboards, and head-mounted pointers replace mice.

%package -n %{girname}
Summary:	GObject introspection interface library for %{pkgname}
Group:		System/Libraries
Obsoletes:	%{_lib}atk1.0_0 < 2.4.0-1

%description -n %{girname}
GObject introspection interface library for %{pkgname}.

%package -n %{develname}
Summary:	Stuff for developing with atk
Group:		Development/C
Provides:	%{pkgname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Obsoletes:	%{_lib}atk1.0_0-devel
Conflicts:	gir-repository < 0.6.5-4

%description -n %{develname}
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x \
	--disable-static \
%if %{enable_gtkdoc}
	--enable-gtk-doc
%endif

%make

%install
%makeinstall_std
%find_lang %{pkgname}10

%files common -f %{pkgname}10.lang
%doc README

%files -n %{libname}
%{_libdir}/libatk-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Atk-%{api}.typelib

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Atk-%{api}.gir


%changelog
* Fri Sep 28 2012 Arkady L. Shane <ashejn@rosalab.ru> 2.6.0-1
- update to 2.6.0

* Sat Jul 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.4.0-4
- Keep some old Provides for library package

* Fri Apr 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.4.0-3
+ Revision: 793702
- rebuild: make gir pkg reqd by devel pkg

* Mon Apr 23 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.4.0-2
+ Revision: 793021
- rebuild for new rpm typelib auto prov/req

* Wed Apr 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.4.0-1
+ Revision: 789112
- new version 2.4.0
- cleaned up spec
- split out gir pkg

* Sat Dec 03 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.2.0-4
+ Revision: 737360
- really disable static build now
- rebuild to remove reqs in devel pkg
- removed .la files
- disabled static build
- removed old ldconfig scriptlets
- removed dup devel provides
- converted BRs to pkgconfig provides

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2.0-3
+ Revision: 722053
- Revert removal of .la files.

* Sat Nov 05 2011 ZÃ© <ze@mandriva.org> 2.2.0-2
+ Revision: 720056
- clean defattr and section clean
- clean .la files
- rebuild

* Mon Oct 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.2.0-1
+ Revision: 708113
- new version 2.2.0

* Mon Jun 13 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.1-1
+ Revision: 684928
- new version
- xz tarball

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 2.0.0-1
+ Revision: 650440
- new version 2.0.0

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 1.32.0-2
+ Revision: 640095
- fix requires on newer glib

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.32.0-1mdv2011.0
+ Revision: 581215
- update to new version 1.32.0

* Sun Sep 12 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.30.0-3mdv2011.0
+ Revision: 577623
- rebuild for new g-i

* Thu Jul 29 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 563161
- rebuild for new gobject-introspection

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 528955
- update to new version 1.30.0

* Mon Mar 08 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.29.92-1mdv2010.1
+ Revision: 515777
- update to new version 1.29.92

* Mon Dec 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.29.4-1mdv2010.1
+ Revision: 480556
- new version
- disable gtk-doc (b.g.o #605113)
- enable introspection

* Wed Dec 09 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.29.3-1mdv2010.1
+ Revision: 475370
- update to new version 1.29.3

* Tue Sep 22 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.28.0-1mdv2010.0
+ Revision: 447188
- update to new version 1.28.0

* Mon Aug 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.27.90-1mdv2010.0
+ Revision: 414195
- update to new version 1.27.90

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.26.0-2mdv2010.0
+ Revision: 413120
- rebuild

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - reenable gtk-doc

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.26.0-1mdv2009.1
+ Revision: 355933
- new version
- disable gtk-doc

* Mon Dec 01 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.25.2-1mdv2009.1
+ Revision: 308752
- update to new version 1.25.2

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.24.0-1mdv2009.0
+ Revision: 286524
- new version
- update license

* Mon Jul 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.23.5-1mdv2009.0
+ Revision: 239327
- new version

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.22.0-2mdv2009.0
+ Revision: 220465
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.22.0-1mdv2008.1
+ Revision: 183403
- new version

* Mon Feb 25 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.21.92-1mdv2008.1
+ Revision: 174634
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1.21.5-1mdv2008.1
+ Revision: 151191
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Sep 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.20.0-1mdv2008.0
+ Revision: 88985
- new version
- new devel name

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.19.6-1mdv2008.0
+ Revision: 56491
- new version

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1.19.3-3mdv2008.0
+ Revision: 36140
- rebuild with correct optflags

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.18.0-1mdv2007.1
+ Revision: 141738
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.17.0-1mdv2007.1
+ Revision: 118936
- new version

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.13.2-1mdv2007.1
+ Revision: 111821
- new version

* Sat Jan 13 2007 Anssi Hannula <anssi@mandriva.org> 1.13.1-3mdv2007.1
+ Revision: 108174
- make atk1.0-common conflict old 32-bit libpkg on 64-bit as well

* Tue Jan 09 2007 Frederic Crozat <fcrozat@mandriva.com> 1.13.1-2mdv2007.1
+ Revision: 106620
- Fix libification

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.13.1-1mdv2007.1
+ Revision: 106043
- new version

* Mon Jan 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.13.0-1mdv2007.1
+ Revision: 105992
- new version

* Mon Dec 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.4-1mdv2007.1
+ Revision: 98484
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.3-3mdv2006.0
+ Revision: 63815
- rebuild
- rebuild
- Import atk1.0

* Wed Oct 04 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.3-1mdv2007.0
- New version 1.12.3

* Wed Aug 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.2-1mdv2007.0
- New release 1.12.2

* Wed Jul 26 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.1-1
- New release 1.12.1

* Tue Jul 11 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.12.1-1mdk
- New release 1.12.1

* Tue Apr 11 2006 Frederic Crozat <fcrozat@mandriva.com> 1.11.4-1mdk
- Release 1.11.4

* Thu Feb 23 2006 Frederic Crozat <fcrozat@mandriva.com> 1.10.3-3mdk
- use mkrel

* Fri Jan 20 2006 Frederic Crozat <fcrozat@mandriva.com> 1.10.3-2mdk
- Rebuild for debug package

* Wed Oct 05 2005 Frederic Crozat <fcrozat@mandriva.com> 1.10.3-1mdk
- Release 1.10.3

* Sat Apr 30 2005 Götz Waschk <waschk@mandriva.org> 1.10.1-1mdk
- make it rpmbuildupdatable
- new version

* Tue Mar 08 2005 Götz Waschk <waschk@linux-mandrake.com> 1.9.1-1mdk
- new version

* Mon Mar 07 2005 Götz Waschk <waschk@linux-mandrake.com> 1.9.0-1mdk
- bump glib dep
- drop patch 0
- new version

* Thu Oct 21 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.8.0-1mdk
- New release 1.8.0
- Patch0 (Fedora): fix Tamil translation

* Fri Sep 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.6.1-2mdk
- Enable libtoolize

* Tue Apr 20 2004 Goetz Waschk <goetz@mandrakesoft.com> 1.6.1-1mdk
- New release 1.6.1

* Sat Apr 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> -1mdk
- Release 1.6.0 (with Götz Waschk help)

