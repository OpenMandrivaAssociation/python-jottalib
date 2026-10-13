Name:		python-jottalib
Version:	0.5.1
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/j/jottalib/jottalib-%{version}.tar.gz
Summary:	A library and tools to access the JottaCloud API
URL:		https://pypi.org/project/jottalib/
License:	GPLv3
Group:		Development/Python
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
A library and tools to access the JottaCloud API

%files
%{_bindir}/jotta-*
%{py_sitedir}/jottalib
%{py_sitedir}/jottalib-*.*-info
