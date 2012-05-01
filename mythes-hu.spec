Name: mythes-hu
Summary: Hungarian thesaurus
%define upstreamid 20090918
Version: 0.%{upstreamid}
Release: 1.1%{?dist}
Source: http://extensions.services.openoffice.org/files/1283/5/hu_dicts.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/hu_dicts
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

%description
Hungarian thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_hu_HU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_hu_HU_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090918-1.1
- Rebuilt for RHEL 6

* Fri Sep 18 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090918-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090203-1
- initial version
