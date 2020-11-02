#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB67157F3A70D4537 (ccaulfie@redhat.com)
#
Name     : libqb
Version  : 1.0.5
Release  : 3
URL      : https://github.com/ClusterLabs/libqb/releases/download/v1.0.5/libqb-1.0.5.tar.xz
Source0  : https://github.com/ClusterLabs/libqb/releases/download/v1.0.5/libqb-1.0.5.tar.xz
Source1  : https://github.com/ClusterLabs/libqb/releases/download/v1.0.5/libqb-1.0.5.tar.xz.asc
Summary  : libqb
Group    : Development/Tools
License  : LGPL-2.1
Requires: libqb-bin = %{version}-%{release}
Requires: libqb-lib = %{version}-%{release}
Requires: libqb-license = %{version}-%{release}
Requires: libqb-man = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : elfutils
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)

%description
# libqb
## What is libqb?
libqb is a library with the primary purpose of providing high-performance,
reusable features for client-server architecture, such as logging,
tracing, inter-process communication (IPC), and polling.

%package bin
Summary: bin components for the libqb package.
Group: Binaries
Requires: libqb-license = %{version}-%{release}

%description bin
bin components for the libqb package.


%package dev
Summary: dev components for the libqb package.
Group: Development
Requires: libqb-lib = %{version}-%{release}
Requires: libqb-bin = %{version}-%{release}
Provides: libqb-devel = %{version}-%{release}
Requires: libqb = %{version}-%{release}

%description dev
dev components for the libqb package.


%package doc
Summary: doc components for the libqb package.
Group: Documentation
Requires: libqb-man = %{version}-%{release}

%description doc
doc components for the libqb package.


%package lib
Summary: lib components for the libqb package.
Group: Libraries
Requires: libqb-license = %{version}-%{release}

%description lib
lib components for the libqb package.


%package license
Summary: license components for the libqb package.
Group: Default

%description license
license components for the libqb package.


%package man
Summary: man components for the libqb package.
Group: Default

%description man
man components for the libqb package.


%prep
%setup -q -n libqb-1.0.5
cd %{_builddir}/libqb-1.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604359829
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604359829
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libqb
cp %{_builddir}/libqb-1.0.5/COPYING %{buildroot}/usr/share/package-licenses/libqb/9a647436aa2324c4cb849c6f3d31c392ed50d9bd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/qb-blackbox

%files dev
%defattr(-,root,root,-)
/usr/include/qb/qbarray.h
/usr/include/qb/qbatomic.h
/usr/include/qb/qbconfig.h
/usr/include/qb/qbdefs.h
/usr/include/qb/qbhdb.h
/usr/include/qb/qbipc_common.h
/usr/include/qb/qbipcc.h
/usr/include/qb/qbipcs.h
/usr/include/qb/qblist.h
/usr/include/qb/qblog.h
/usr/include/qb/qbloop.h
/usr/include/qb/qbmap.h
/usr/include/qb/qbrb.h
/usr/include/qb/qbutil.h
/usr/lib64/libqb.so
/usr/lib64/pkgconfig/libqb.pc
/usr/share/man/man3/qbarray.h.3
/usr/share/man/man3/qbatomic.h.3
/usr/share/man/man3/qbdefs.h.3
/usr/share/man/man3/qbhdb.h.3
/usr/share/man/man3/qbipc_common.h.3
/usr/share/man/man3/qbipcc.h.3
/usr/share/man/man3/qbipcs.h.3
/usr/share/man/man3/qblist.h.3
/usr/share/man/man3/qblog.h.3
/usr/share/man/man3/qbloop.h.3
/usr/share/man/man3/qbmap.h.3
/usr/share/man/man3/qbrb.h.3
/usr/share/man/man3/qbutil.h.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libqb/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libqb.so.0
/usr/lib64/libqb.so.0.19.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libqb/9a647436aa2324c4cb849c6f3d31c392ed50d9bd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/qb-blackbox.8
