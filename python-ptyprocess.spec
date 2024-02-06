# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ptyprocess
Epoch: 100
Version: 0.7.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Run a subprocess in a pseudo terminal
License: ISC
URL: https://github.com/pexpect/ptyprocess/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ptyprocess
Summary: Run a subprocess in a pseudo terminal
Requires: python3
Provides: python3-ptyprocess = %{epoch}:%{version}-%{release}
Provides: python3dist(ptyprocess) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ptyprocess = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ptyprocess) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ptyprocess = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ptyprocess) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

%files -n python%{python3_version_nodots}-ptyprocess
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-ptyprocess
Summary: Run a subprocess in a pseudo terminal
Requires: python3
Provides: python3-ptyprocess = %{epoch}:%{version}-%{release}
Provides: python3dist(ptyprocess) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ptyprocess = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ptyprocess) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ptyprocess = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ptyprocess) = %{epoch}:%{version}-%{release}

%description -n python3-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both
the process and its pty.

%files -n python3-ptyprocess
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
