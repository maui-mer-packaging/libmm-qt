# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       libmm-qt

# >> macros
# << macros

Summary:    Library wrapping ModemManager DBus API
Version:    5.1.0
Release:    1
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  libmm-qt.yaml
Source101:  libmm-qt-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  ModemManager-devel >= 1.0.0

%description
Qt 5 libraries and header files for developing applications that use ModemManager


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc README
%{_kf5_libdir}/libKF5ModemManagerQt.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/libKF5ModemManagerQt.so
%{_kf5_cmakedir}/KF5ModemManagerQt
%{_kf5_includedir}/ModemManagerQt
%{_kf5_includedir}/modemmanagerqt_version.h
%{_kf5_mkspecsdir}/*.pri
# >> files devel
# << files devel
