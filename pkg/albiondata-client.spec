Name:           albiondata-client
Version:        0.1.7
Release:        0
Summary:        Distributed client for the Albion Online Data project.
Group:          Applications/Networking
License:        MIT
URL:            https://github.com/broderickhyman/albiondata-client
Source:         https://github.com/broderickhyman/albiondata-client/archive/refs/tags/%version.tar.gz
Packager: 	    willwh

BuildRequires:  golang
BuildRequires:  git

%description
Distributed client for the Albion Online Data project.

%global debug_package %{nil}

%prep
%autosetup

%build
go build -v -o %{name}

%install
mkdir -p %{buildroot}/usr/bin
cp %{name} %{buildroot}/usr/bin/

%post
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/%name

%files
/usr/bin/%{name}