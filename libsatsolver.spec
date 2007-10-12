Name:           libsatsolver
Version:        0.0.1
Release:        1
License:        BSD
Url:            http://svn.opensuse.org/svn/zypp/trunk/sat-solver
Source:         satsolver-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          System/Libraries
BuildRequires:  libexpat-devel db43-devel
Requires:       expat db43
Summary:        A new approach to package dependency solving


%description
-

%package devel
Summary:        A new approach to package dependency solving
Group:          Development/Libraries

%description devel
-

%prep
%setup -n satsolver-%{version}

%build
%configure --prefix=/usr --libdir=%{_libdir} --sysconfdir=/etc
make

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/libsatsolver.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)

%files devel
%defattr(-,root,root)
%{_libdir}/libsatsolver.a
%doc doc/README*
%doc doc/THEORY
%doc doc/PLANNING
%dir /usr/include/satsolver
/usr/include/satsolver/*

%changelog
