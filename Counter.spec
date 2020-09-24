#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Counter
Version  : 1.0.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/7d/b0/23d19892f8d91ec9c5b8a2035659bce23587fed419d68fa3d70b6abf8bcd/Counter-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/b0/23d19892f8d91ec9c5b8a2035659bce23587fed419d68fa3d70b6abf8bcd/Counter-1.0.0.tar.gz
Summary  : Counter package defines the "counter.Counter" class similar to bags or multisets in other languages.
Group    : Development/Tools
License  : MIT
Requires: Counter-license = %{version}-%{release}
Requires: Counter-python = %{version}-%{release}
Requires: Counter-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===========

%package license
Summary: license components for the Counter package.
Group: Default

%description license
license components for the Counter package.


%package python
Summary: python components for the Counter package.
Group: Default
Requires: Counter-python3 = %{version}-%{release}
Provides: counter-python

%description python
python components for the Counter package.


%package python3
Summary: python3 components for the Counter package.
Group: Default
Requires: python3-core
Provides: pypi(counter)

%description python3
python3 components for the Counter package.


%prep
%setup -q -n Counter-1.0.0
cd %{_builddir}/Counter-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583517538
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Counter
cp %{_builddir}/Counter-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/Counter/f8b32ec93da4a824d37adbf4897af051673e8abd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Counter/f8b32ec93da4a824d37adbf4897af051673e8abd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
