%define lname	osmgpsmap

%define major	2
%define libname	%mklibname %{lname} %{major}
%define devname	%mklibname %{lname} -d

Name:           osm-gps-map
Version:        0.7.3
Release:        2
Summary:        Gtk+ widget for displaying OpenStreetMap tiles
Group:          System/Libraries
License:        GPLv2
URL:            http://nzjrs.github.com/osm-gps-map/
Source0:        http://www.johnstowers.co.nz/files/%{name}/%{name}-%{version}.tar.gz
Patch0:		osm-gps-map-0.7.3-linkage.patch
BuildRequires:	gtk+2-devel
BuildRequires:	libsoup-devel

%description
A Gtk+ widget that when given GPS co-ordinates, draws a GPS track, and
points of interest on a moving map display. Downloads map data from a
number of websites, including openstreetmap.org.

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
%patch0 -p0 -b .linkage

%build
%configure2_5x \
	--disable-static \
	--disable-introspection
%make V=1

%install
%makeinstall_std

#handle docs inf files section
rm -rf %{buildroot}/usr/doc/osm-gps-map

%files -n %{libname}
%doc AUTHORS README NEWS
%{_libdir}/lib%{lname}.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/lib%{lname}
%{_includedir}/%{lname}
%{_libdir}/lib%{lname}.so
%{_libdir}/pkgconfig/%{lname}.pc



%changelog
* Mon Oct 31 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7.3-1
+ Revision: 708033
- imported package osm-gps-map

