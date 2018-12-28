#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Counter
Version  : 1.0.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/7d/b0/23d19892f8d91ec9c5b8a2035659bce23587fed419d68fa3d70b6abf8bcd/Counter-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/b0/23d19892f8d91ec9c5b8a2035659bce23587fed419d68fa3d70b6abf8bcd/Counter-1.0.0.tar.gz
Summary  : Counter package defines the "counter.Counter" class similar to bags or multisets in other languages.
Group    : Development/Tools
License  : MIT
Requires: Counter-python3
Requires: Counter-python
BuildRequires : buildreq-distutils3

%description
===========

%package python
Summary: python components for the Counter package.
Group: Default
Requires: Counter-python3
Provides: counter-python

%description python
python components for the Counter package.


%package python3
Summary: python3 components for the Counter package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Counter package.


%prep
%setup -q -n Counter-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536659864
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
