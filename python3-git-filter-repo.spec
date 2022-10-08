Summary:	Quickly rewrite git repository history
Summary(pl.UTF-8):	Szybkie przepisywanie historii repozytorium
Name:		python3-git-filter-repo
Version:	2.34.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/git-filter-repo/
Source0:	https://files.pythonhosted.org/packages/source/g/git-filter-repo/git-filter-repo-%{version}.tar.gz
# Source0-md5:	14825e3c78de704a0244092600bf1fdc
URL:		https://pypi.org/project/git-filter-repo/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	git-core >= 2.24.0
Requires:	python3-modules >= 1:3.5
Conflicts:	git-filter-repo < 2.34.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
git filter-repo is a versatile tool for rewriting history.

%description -l pl.UTF-8
git filter-repo to wszechstronne narzędzie do przepisywania historii.

%prep
%setup -q -n git-filter-repo-%{version}

# fix #!/usr/bin/env python -> #!/usr/bin/python:
%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' git_filter_repo.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} $RPM_BUILD_ROOT%{_bindir}/git-filter-repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/git_filter_repo.py
%{py3_sitescriptdir}/__pycache__/git_filter_repo.cpython-*.py[co]
%{py3_sitescriptdir}/git_filter_repo-%{version}-py*.egg-info
