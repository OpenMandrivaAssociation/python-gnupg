%define oname python_gnupg
%bcond tests 1

Name:           python-gnupg
Version:        0.5.7
Release:        1
Summary:        A Python wrapper for GnuPG
License:        BSD-3-Clause
Group:          Development/Python
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://github.com/vsajip/python-gnupg/archive/%{version}/%{name}-%{version}.tar.gz
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

%prep -a
# 0.5.7 caps setuptools below 75. Cooker setuptools is 84, and this
# package is a single module that does not need the cap.
sed -i 's/setuptools >= 68,<75/setuptools >= 68/' pyproject.toml
# The key is missing its equals sign, which setuptools rejects.
sed -i 's/^requires_python >= 2.7/requires_python = >=2.7/' setup.cfg

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
export NO_EXTERNAL_TESTS=true
# skip flaky test
pytest -v test_gnupg.py -k "not test_auto_key_locating"
%endif

%files
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/__pycache__/gnupg.*.pyc
%{python_sitelib}/gnupg.py
%{python_sitelib}/%{oname}-%{version}.dist-info
