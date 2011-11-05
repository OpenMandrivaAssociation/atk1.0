# enable_gtkdoc: Toggle if gtkdoc stuff should be rebuilt
#	0 = no
#	1 = yes
%define enable_gtkdoc	0

%define api_version	1.0
%define lib_major	0
%define pkgname     atk

# Version of glib needed
%define req_glib2_version 2.5.7

%define lib_name %mklibname %{name}_ %{lib_major}
%define develname %mklibname -d %{name}

Name: %{pkgname}%{api_version}
Version: 2.2.0
Release: 2
Summary: Accessibility features for Gtk+
License: LGPLv2+
Group: Accessibility
Url: http://developer.gnome.org/projects/gap/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.xz
BuildRequires: libglib2-devel >= %{req_glib2_version}
%if %enable_gtkdoc
BuildRequires:	gtk-doc >= 1.11-3
%endif
BuildRequires: gobject-introspection-devel

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
Summary: Data files used by atk
Group: System/Libraries
Conflicts:  %{_lib}atk1.0_0 < 1.13.1-2
# 64bit atk1.0-common conflicts with old 32bit lib as well -Anssi
Conflicts:  libatk1.0_0 < 1.13.1-2

%description common
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

This package contains data used by atk library.

%package -n %{lib_name}
Summary: Accessibility features for Gtk+
Group: System/Libraries
Requires: common-licenses
Obsoletes:	%{pkgname} lib%{pkgname}
Provides:	%{pkgname} = %{version}-%{release}
Provides:	lib%{pkgname} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Requires:	%{name}-common >= %{version}-%{release}
Conflicts:	gir-repository < 0.6.5-4

%description -n %{lib_name}
Accessibility means providing system infrastructure that allows add-on
assistive software to transparently provide specalized input and ouput
capabilities. For example, screen readers allow blind users to navigate
through applications, determine the state of controls, and read text via
text to speech conversion. On-screen keyboards replace physical
keyboards, and head-mounted pointers replace mice.

%package -n %{develname}
Summary: Stuff for developing with atk
Group: Development/C
Obsoletes:	%{pkgname}-devel lib%{pkgname}-devel
Provides:	%{pkgname}-devel = %{version}-%{release}
Provides:	lib%{pkgname}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	libglib2-devel >= %{req_glib2_version}
Conflicts:  libatk10-devel
Obsoletes: %mklibname -d %{name}_ 0
Conflicts:	gir-repository < 0.6.5-4

%description -n %develname
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x \
	--enable-static \
%if %enable_gtkdoc
	--enable-gtk-doc
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{pkgname}10

# clean .la files
rm -f %{buildroot}%{_libdir}/*.la


%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files common -f %{pkgname}10.lang
%doc README

%files -n %{lib_name}
%{_libdir}/libatk-%{api_version}.so.%{lib_major}*
%{_libdir}/girepository-1.0/Atk-%{api_version}.typelib

%files -n %develname
%doc AUTHORS ChangeLog NEWS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Atk-%{api_version}.gir
