#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module	fedmsg_meta_pld
Summary:	Metadata providers for PLD Linux fedmsg deployment
Name:		python-fedmsg-meta-pld
Version:	0.0.1
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://github.com/glensc/fedmsg_meta_pld/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	cff6b4aaf192d718632ebd6a2b24bcfc
URL:		https://github.com/glensc/fedmsg_meta_pld
BuildRequires:	fedmsg >= 0.10.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	fedmsg >= 0.7.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metadata providers for PLD Linux fedmsg deployment.

%prep
%setup -qc
mv fedmsg_meta_pld-*/* .

%build
%py_build

%if %{with tests}
PYTHONPATH=. FEDMSG_META_NO_NETWORK=True nosetests
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md
%{py_sitescriptdir}/fedmsg_meta_pld
%{py_sitescriptdir}/fedmsg_meta_pld-%{version}-py*.egg-info
