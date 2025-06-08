Name:           python-gnupg
Version:        0.5.4
Release:        1
Source0:        https://github.com/vsajip/python-gnupg/releases/download/%{version}/python-gnupg-%{ve>
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
%{py_sitedir}/__pycache__ 
%{py_sitedir}/gnupg.py
%{py_sitedir}/python_gnupg-*.dist-info
