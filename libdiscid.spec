Summary:	Library for creating MusicBrainz DiscIDs
Name:		libdiscid
Version:	0.2.2
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://users.musicbrainz.org/~matt/%{name}-%{version}.tar.gz
# Source0-md5:	ee21ddbe696a3c60e14827a75f3bcf5b
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
URL:		http://musicbrainz.org/doc/libdiscid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdiscid is a C library for creating MusicBrainz DiscIDs from audio
CDs. It reads a CD's table of contents (TOC) and generates an
identifier which can be used to lookup the CD at MusicBrainz.
Additionally, it provides a submission URL for adding the DiscID to
the database.

%package devel
Summary:	Header files for discid library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for discid library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libdiscid.so.0
%attr(755,root,root) %{_libdir}/libdiscid.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdiscid.so
%{_libdir}/libdiscid.la
%{_includedir}/discid
%{_pkgconfigdir}/libdiscid.pc

