#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-moddb
Version  : 0.8.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/ae/7d/8d5cf4e2aac9563dc2d6ba6a313aaef89c9f647b7df2e71907971d49e931/moddb-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ae/7d/8d5cf4e2aac9563dc2d6ba6a313aaef89c9f647b7df2e71907971d49e931/moddb-0.8.1.tar.gz
Summary  : A scrapper for ModDB Mod and Game pages
Group    : Development/Tools
License  : MIT
Requires: pypi-moddb-license = %{version}-%{release}
Requires: pypi-moddb-python = %{version}-%{release}
Requires: pypi-moddb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
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
Requires: pypi(pyrate_limiter)
Requires: pypi(requests)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-moddb package.


%prep
%setup -q -n moddb-0.8.1
cd %{_builddir}/moddb-0.8.1
pushd ..
cp -a moddb-0.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686615335
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . toolz
pypi-dep-fix.py . pyrate-limiter
pypi-dep-fix.py . beautifulsoup4
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . toolz
pypi-dep-fix.py . pyrate-limiter
pypi-dep-fix.py . beautifulsoup4
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-moddb
cp %{_builddir}/moddb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-moddb/b9b7e96a5a0c79d28265e29773a0a6887e1671d0 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} toolz
pypi-dep-fix.py %{buildroot} pyrate-limiter
pypi-dep-fix.py %{buildroot} beautifulsoup4
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-moddb/b9b7e96a5a0c79d28265e29773a0a6887e1671d0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
