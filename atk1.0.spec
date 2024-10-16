# Wine uses atk
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api 1.0
%define	major 0
%define	pkgname atk
%define	libname %mklibname %{pkgname} %{api} %{major}
%define	girname %mklibname %{pkgname}-gir %{api}
%define	devname %mklibname -d %{name}
%bcond_with	bootstrap
%bcond_with	gtk_doc
%define lib32name lib%{pkgname}%{api}_%{major}
%define dev32name lib%{name}-devel

Summary:	Accessibility features for Gtk+
Name:		%{pkgname}%{api}
Version:	2.38.0
Release:	2
License:	LGPLv2+
Group:		Accessibility
Url:		https://developer.gnome.org/projects/gap/
Source0:	https://download.gnome.org/sources/atk/%{url_ver}/atk-%{version}.tar.xz

%if %{with gtkdoc}
BuildRequires:	gtk-doc >= 1.11-3
%endif
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0) >= 2.5.7
BuildRequires:	pkgconfig(gobject-introspection-1.0)
%if %{with compat32}
BuildRequires:	devel(libglib-2.0)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Accessibility features for Gtk+ (32-bit)
Group:		System/Libraries
Suggests:	%{name}-common >= %{version}-%{release}

%description -n %{lib32name}
Accessibility means providing system infrastructure that allows add-on
assistive software to transparently provide specalized input and ouput
capabilities. For example, screen readers allow blind users to navigate
through applications, determine the state of controls, and read text via
text to speech conversion. On-screen keyboards replace physical
keyboards, and head-mounted pointers replace mice.

%package -n %{dev32name}
Summary:	Stuff for developing with atk
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
ATK, the Accessibility Tookit, is used to obtain accessibily information
from GTK+ and GNOME widgets.
%endif

%prep
%autosetup -p1 -n %{pkgname}-%{version}
%if %{with compat32}
%meson32 -Dintrospection=false
%endif
%meson

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install
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
%if %{with gtkdoc}
%doc %{_datadir}/gtk-doc/html/*
%endif
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%if !%{with bootstrap}
%{_datadir}/gir-1.0/Atk-%{api}.gir
%endif

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libatk-%{api}.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*
%endif
