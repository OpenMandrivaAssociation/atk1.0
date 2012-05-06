%define url_ver %(echo %{version}|cut -d. -f1,2) 

%define enable_gtkdoc	0

%define api		1.0
%define major	0
%define pkgname	atk
%define libname %mklibname %{pkgname} %{api} %{major}
%define girname %mklibname %{pkgname}-gir %{api}
%define develname %mklibname -d %{name}

Summary:	Accessibility features for Gtk+
Name:		%{pkgname}%{api}
Version:	2.4.0
Release:	3
License:	LGPLv2+
Group:		Accessibility
Url:		http://developer.gnome.org/projects/gap/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/atk/%{url_ver}/%{pkgname}-%{version}.tar.xz

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
%setup -qn %{pkgname}-%{version}

%build
%configure2_5x \
	--disable-static \
%if %{enable_gtkdoc}
	--enable-gtk-doc
%endif

%make

%install
%makeinstall_std
find %{buildroot} -name "*.la" -delete
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

