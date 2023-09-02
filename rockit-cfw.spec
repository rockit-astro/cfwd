Name:      rockit-cfw
Version:   %{_version}
Release:   1
Summary:   FLI Colour Filter Wheel.
Url:       https://github.com/rockit-astro/cfwd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/cfwd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/filter %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/cfwd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/cfwd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/filter %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/warwick.json %{buildroot}%{_sysconfdir}/cfwd/

%package server
Summary:  CFW control server.
Group:    Unspecified
Requires: python3-rockit-cfw libfli
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/cfwd
%defattr(0644,root,root,-)
%{_unitdir}/cfwd@.service

%package client
Summary:  CFW control client.
Group:    Unspecified
Requires: python3-rockit-cfw
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/filter
/etc/bash_completion.d/filter

%package data-warwick
Summary: CFW data for Windmill Hill Observatory telescope
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/cfwd/warwick.json

%changelog
