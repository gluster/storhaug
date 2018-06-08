Name:      storhaug
Summary:   High-Availability Add-on for NFS-Ganesha
Version:   1.0
Release:   1%{?prereltag:.%{prereltag}}%{?dist}
License:   GPLv2
URL:       https://github.com/gluster/storhaug
Vendor:    Fedora Project
BuildArch: noarch
Obsoletes: storhaug-smb < 1.0
Source0:   https://github.com/gluster/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:  glusterfs-server
Requires:  ctdb

%description
High-Availability add-on for storage servers

### NFS (NFS-Ganesha)
%package nfs
Summary:   storhaug NFS-Ganesha module
Requires:  %{name} = %{version}-%{release}
Requires:  nfs-ganesha-gluster

%description nfs
High-Availability NFS add-on for NFS-Ganesha

%build

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 0755 %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/ctdb/nfs-checks-ganesha.d
install -m 0744 storhaug %{buildroot}%{_sbindir}/storhaug
install -m 0744 20.nfs-ganesha.check %{buildroot}%{_sysconfdir}/ctdb/nfs-checks-ganesha.d/
install -m 0744 nfs-ganesha-callout %{buildroot}%{_sysconfdir}/ctdb

%clean

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_sbindir}/storhaug

%files nfs
%dir %{_sysconfdir}/ctdb/nfs-checks-ganesha.d
     %{_sysconfdir}/ctdb/nfs-checks-ganesha.d/20.nfs-ganesha.check
     %{_sysconfdir}/ctdb/nfs-ganesha-callout

%changelog
* Fri Jun 8 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.0-1
- Reboot, Initial version
