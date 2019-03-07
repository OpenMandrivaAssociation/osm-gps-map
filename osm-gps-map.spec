%define lname	osmgpsmap

%define major   1
%define api     1.0
%define gir_major       1.0
%define libname %mklibname %{lname} %{api} %{major}
%define devname %mklibname %{lname} %{api} -d
%define gir_name %mklibname %{lname}-gir %{gir_major}

Name:           osm-gps-map
Version:        1.1.0
Release:        1
Summary:        Gtk+ widget for displaying OpenStreetMap tiles
Group:          System/Libraries
License:        GPLv2
URL:            http://nzjrs.github.com/osm-gps-map/
Source0:        https://github.com/nzjrs/osm-gps-map/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:		osm-gps-map-1.0.0-linkage.patch
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	python-gi
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  gtk-doc
BuildRequires:  gnome-common

%description
A Gtk+ widget that when given GPS co-ordinates, draws a GPS track, and
points of interest on a moving map display. Downloads map data from a
number of websites, including openstreetmap.org.

%package -n %{gir_name}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}

%description -n %{gir_name}
GObject Introspection interface description for %{name}.

%package -n %{libname}
Summary:	Gtk+ widget for displaying OpenStreetMap tiles
Group:		System/Libraries

%description -n %{libname}
A Gtk+ widget that when given GPS co-ordinates, draws a GPS track, and
points of interest on a moving map display. Downloads map data from a
number of websites, including openstreetmap.org.

%package -n %{devname}
Summary:        Development files for the %{name} Gtk+ widget
Group:          Development/Other
Requires:       %{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{lname}-devel = %{version}-%{release}
Provides:	lib%{lname}-devel = %{version}-%{release}

%description -n %{devname}
The development files for the %{name} Gtk+ widget.

%prep
%setup -q

%build
[[ -f configure ]] || NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x \
	--disable-static --enable-introspection
%make_build V=1

%install
%make_install

#handle docs inf files section
rm -rf %{buildroot}/usr/doc/osm-gps-map

%files -n %{libname}
%{_docdir}/%{name}
%{_libdir}/lib%{lname}-%{api}.so.%{major}{,.*}

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/lib%{lname}/
%{_includedir}/%{lname}-%{api}
%{_libdir}/lib%{lname}-%{api}.so
%{_libdir}/pkgconfig/%{lname}-%{api}.pc

%files -n %{gir_name}
%{_libdir}/girepository-1.0/*-%{gir_major}.typelib
%{_datadir}/gir-1.0/*-%{gir_major}.gir

