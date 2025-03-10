Summary:	Quickly rewrite git repository history
Summary(pl.UTF-8):	Szybkie przepisywanie historii repozytorium
Name:		python3-git-filter-repo
Version:	2.47.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/git-filter-repo/
Source0:	https://pypi.debian.net/git-filter-repo/git_filter_repo-%{version}.tar.gz
# Source0-md5:	9aa3e5b4a036bdbacaf59770b8ca40a4
URL:		https://pypi.org/project/git-filter-repo/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
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
%setup -q -n git_filter_repo-%{version}

# use direct shebang
%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' git_filter_repo.py

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} $RPM_BUILD_ROOT%{_bindir}/git-filter-repo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/git_filter_repo.py
%{py3_sitescriptdir}/__pycache__/git_filter_repo.cpython-*.py[co]
%{py3_sitescriptdir}/git_filter_repo-%{version}.dist-info
