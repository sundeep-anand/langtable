Name:           langtable
Version:        0.0.2
Release:        1%{?dist}
Summary:        For guessing reasonable defaults for locale, keyboard, territory, …
Group:          Development/Tools
# the translations in languages.xml and territories.xml are (mostly)
# imported from CLDR and are thus under the Unicode license, the
# short name for this license is "MIT", see:
# https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#Modern_Style_without_sublicense_.28Unicode.29
License:        GPLv3+
URL:            https://github.com/mike-fabian/langtable
Source0:        http://mfabian.fedorapeople.org/langtable/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-lxml
BuildRequires:  python2-devel

%description
langtable is used to guess reasonable defaults for locale, keyboard,
territory, …, if part of that information is already known. For
example, guess the territory and the keyboard layout if the language
is known or guess the language and keyboard layout if the territory is
already known.

%package python
Summary:        Python module to query the langtable-data
Group:          Development/Tools
License:        GPLv3+
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-data = %{version}-%{release}
Requires:       python-lxml

%description python
This package contains a Python module to query the data
from langtable-data.

%package data
Summary:        Data files for langtable
Group:          Development/Tools
License:        GPLv3+ and MIT
Requires:       %{name} = %{version}-%{release}

%description data
This package contains the data files for langtable.

%prep
%setup -q

%build
perl -pi -e "s,_datadir = '(.*)',_datadir = '%{_datadir}/langtable'," langtable.py
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --prefix=%{_prefix} --install-data=%{_datadir}/langtable --root $RPM_BUILD_ROOT

%check
(cd $RPM_BUILD_DIR/%{name}-%{version}/data; PYTHONPATH=.. %{__python} -m doctest ../test_cases.txt)

%files
%doc README COPYING ChangeLog unicode-license.txt test_cases.txt

%files python
%{python_sitelib}/*

%files data
%{_datadir}/langtable/*

%changelog
* Fri May 10 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.2-1
- update to 0.0.2
- Prefer values for language, script, and territory found in languageId over those found in the other parameters

* Tue May 07 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.1-1
- initial package



