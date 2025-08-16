Name:      rockit-filterwheel-fli
Version:   %{_version}
Release:   1%{dist}
Summary:   FLI Colour Filter Wheel.
Url:       https://github.com/rockit-astro/filterwheeld-fli
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/filterwheeld/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/filter %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/fli_filterwheeld %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/fli_filterwheeld@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/filter %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/warwick.json %{buildroot}%{_sysconfdir}/filterwheeld/

%package server
Summary:  CFW control server.
Group:    Unspecified
Requires: python3-rockit-filterwheel-fli libfli
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/fli_filterwheeld
%defattr(0644,root,root,-)
%{_unitdir}/fli_filterwheeld@.service

%package client
Summary:  CFW control client.
Group:    Unspecified
Requires: python3-rockit-filterwheel-fli
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
%{_sysconfdir}/filterwheeld/warwick.json

%changelog
