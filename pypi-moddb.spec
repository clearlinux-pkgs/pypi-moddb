#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v10
# autospec commit: 5905be9
#
Name     : pypi-moddb
Version  : 0.11.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/9b/36/2b403da6865eb9fd82df6b52df2d5d9ba15cdc181b233ecd3dc261fb40fa/moddb-0.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9b/36/2b403da6865eb9fd82df6b52df2d5d9ba15cdc181b233ecd3dc261fb40fa/moddb-0.11.0.tar.gz
Summary  : A scrapper for ModDB Mod and Game pages
Group    : Development/Tools
License  : MIT
Requires: pypi-moddb-license = %{version}-%{release}
Requires: pypi-moddb-python = %{version}-%{release}
Requires: pypi-moddb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(beautifulsoup4)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ModDB Reader
**Library is now stable**
The goal of the library is to be able to navigate ModDB purely programmatically through scraping and parsing of the various models present on the website. This is based off a command of my bot which can parse either a game or a mod, this command gave birth to the original library which was extremely limited in its abilities and only able to parse a few pages with inconsistencies. This library is a much more mature and professional attempt at the whole idea, adding on a much deeper understanding of OOP.

%package license
Summary: license components for the pypi-moddb package.
Group: Default

%description license
license components for the pypi-moddb package.


%package python
Summary: python components for the pypi-moddb package.
Group: Default
Requires: pypi-moddb-python3 = %{version}-%{release}

%description python
python components for the pypi-moddb package.


%package python3
Summary: python3 components for the pypi-moddb package.
Group: Default
Requires: python3-core
Provides: pypi(moddb)
Requires: pypi(beautifulsoup4)
Requires: pypi(requests)

%description python3
python3 components for the pypi-moddb package.


%prep
%setup -q -n moddb-0.11.0
cd %{_builddir}/moddb-0.11.0
pushd ..
cp -a moddb-0.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713131624
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . toolz
pypi-dep-fix.py . pyrate-limiter
pypi-dep-fix.py . beautifulsoup4
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . toolz
pypi-dep-fix.py . pyrate-limiter
pypi-dep-fix.py . beautifulsoup4
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-moddb
cp %{_builddir}/moddb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-moddb/d7cb6636a1bcf8b92975627e64baab53f41d09c5 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} toolz
pypi-dep-fix.py %{buildroot} pyrate-limiter
pypi-dep-fix.py %{buildroot} beautifulsoup4
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-moddb/d7cb6636a1bcf8b92975627e64baab53f41d09c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
