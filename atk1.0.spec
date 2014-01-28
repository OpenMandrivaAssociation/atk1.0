%define url_ver %(echo %{version}|cut -d. -f1,2)
%define enable_gtkdoc	0

%define api	1.0
%define major	0
%define pkgname	atk
%define libname %mklibname %{pkgname} %{api} %{major}
%define girname %mklibname %{pkgname}-gir %{api}
%define devname %mklibname -d %{name}
%bcond_with	bootstrap

Summary:	Accessibility features for Gtk+
Name:		%{pkgname}%{api}
Version:	2.11.4
Release:	1
License:	LGPLv2+
Group:		Accessibility
Url:		http://developer.gnome.org/projects/gap/
Source0:	https://download.gnome.org/sources/atk/2.11/atk-%{version}.tar.xz

%if %{enable_gtkdoc}
BuildRequires:	gtk-doc >= 1.11-3
%endif
BuildRequires:	pkgconfig(glib-2.0) >= 2.5.7
BuildRequires:	pkgconfig(gobject-introspection-1.0)

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

%description -n %{libname}
Accessibility means providing system infrastructure that allows add-on
assistive software to transparently provide specalized input and ouput
capabilities. For example, screen readers allow blind users to navigate
through applications, determine the state of controls, and read text via
text to speech conversion. On-screen keyboards replace physical
keyboards, and head-mounted pointers replace mice.

%if !%{with bootstrap}
%package -n %{girname}
Summary:	GObject introspection interface library for %{pkgname}
Group:		System/Libraries
Obsoletes:	%{_lib}atk1.0_0 < 2.4.0-1

%description -n %{girname}
GObject introspection interface library for %{pkgname}.
%endif

%package -n %{devname}
Summary:	Stuff for developing with atk
Group:		Development/C
Provides:	%{pkgname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girname} = %{version}-%{release}
%endif
Obsoletes:	%{_lib}atk1.0_0-devel

%description -n %{devname}
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.

%prep
%setup -q -n %{pkgname}-%{version}
for f in config.guess config.sub ; do
        test -f /usr/share/libtool/config/$f || continue
        find . -type f -name $f -exec cp /usr/share/libtool/config/$f \{\} \;
done

%build
%configure2_5x \
	--disable-static \
%if %{with bootstrap}
	--enable-introspection=no \
%endif
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

%if !%{with bootstrap}
%files -n %{girname}
%{_libdir}/girepository-1.0/Atk-%{api}.typelib
%endif

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%if !%{with bootstrap}
%{_datadir}/gir-1.0/Atk-%{api}.gir
%endif

