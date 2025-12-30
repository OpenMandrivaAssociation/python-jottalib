Name:		python-jottalib
Version:	0.5.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/j/jottalib/jottalib-%{version}.tar.gz
Summary:	A library and tools to access the JottaCloud API
URL:		https://pypi.org/project/jottalib/
License:	GPLv3
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

%description
A library and tools to access the JottaCloud API

%files
%{_bindir}/jotta-*
%{py_sitedir}/jottalib
%{py_sitedir}/jottalib-*.*-info
