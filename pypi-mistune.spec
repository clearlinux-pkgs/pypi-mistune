#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mistune
Version  : 2.0.2
Release  : 47
URL      : https://files.pythonhosted.org/packages/33/36/506af4690234e7a84b8b3e0f4aee4dfe5a28b8688a0eec2047af9a078020/mistune-2.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/33/36/506af4690234e7a84b8b3e0f4aee4dfe5a28b8688a0eec2047af9a078020/mistune-2.0.2.tar.gz
Summary  : A sane Markdown parser with useful plugins and renderers
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-mistune-license = %{version}-%{release}
Requires: pypi-mistune-python = %{version}-%{release}
Requires: pypi-mistune-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
Mistune
=======
A fast yet powerful Python Markdown parser with renderers and plugins.

%package license
Summary: license components for the pypi-mistune package.
Group: Default

%description license
license components for the pypi-mistune package.


%package python
Summary: python components for the pypi-mistune package.
Group: Default
Requires: pypi-mistune-python3 = %{version}-%{release}

%description python
python components for the pypi-mistune package.


%package python3
Summary: python3 components for the pypi-mistune package.
Group: Default
Requires: python3-core
Provides: pypi(mistune)

%description python3
python3 components for the pypi-mistune package.


%prep
%setup -q -n mistune-2.0.2
cd %{_builddir}/mistune-2.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642179941
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mistune
cp %{_builddir}/mistune-2.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mistune/f763a35f662facb7d39a4fd7c3872b311855bc43
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mistune/f763a35f662facb7d39a4fd7c3872b311855bc43

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
