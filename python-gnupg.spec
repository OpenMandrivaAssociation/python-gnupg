%bcond tests 1

Name:           python-gnupg
Version:        0.5.5
Release:        1
Summary:        A Python wrapper for GnuPG
License:        BSD-3-Clause
Group:          Development/Python
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://github.com/vsajip/python-gnupg/releases/download/%{version}/python-gnupg-%{version}.tar.gz
BuildSystem:    python
BuildArch:      noarch
BuildRequires:  gnupg
BuildRequires:  python
BuildRequires:  python%{pyver}dist(build)
BuildRequires:  python%{pyver}dist(installer)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:  python%{pyver}dist(pytest)
%endif
Requires:       gnupg

%description
A Python wrapper for GnuPG

%if %{with tests}
%check
export CI=true
export NO_EXTERNAL_TESTS=true
# skip flaky test
pytest -v test_gnupg.py -k "not test_auto_key_locating"
%endif

%files
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/__pycache__/gnupg.*.pyc
%{python_sitelib}/gnupg.py
%{python_sitelib}/python_gnupg-%{version}.dist-info
