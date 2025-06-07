Name:           python-gnupg
Version:        2.3.1
Release:        1
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{oname}-%{version}.tar.gz

Summary:        A Python wrapper for GnuPG
URL:            https://pypi.org/project/gnupg/
License:        BSD
Group:          Development/Python
BuildRequires:  python
BuildRequires:  gnupg
BuildRequires:  python%{pyver}dist(build)
BuildRequires:  python%{pyver}dist(installer)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(pytest)
BuildSystem:    python
BuildArch:      noarch
Requires:       gnupg
Requires:       python

%description
A Python wrapper for GnuPG

%files
%{py_sitedir}/gnupg
%{py_sitedir}/gnupg-*.egg-info
/usr/bin/versioneer.py

