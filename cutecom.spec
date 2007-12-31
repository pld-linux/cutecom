Summary:	A graphical serial terminal
Summary(pl.UTF-8):	Graficzny terminal szeregowy
Name:		cutecom
Version:	0.14.1
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://cutecom.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	6e6057b82cbe086806c6d66a1b48c753
URL:		http://cutecom.sourceforge.net
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cutecom is a graphical serial terminal, like minicom. It is aimed
mainly at hardware developers or other people who need a terminal to
talk to their devices.

%description -l pl.UTF-8
Cutecom to graficzny terminal szeregowy podobny do minicoma. Jest
przeznaczony głównie dla twórców sprzętu i innych ludzi potrzebujących
terminala do komunikacji ze swoimi urządzeniami.

%prep
%setup -q

%build
qmake \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}"
%{__make} \
	QTDIR=%{_prefix}

echo "Categories=Qt;Utility;" >> ./cutecom.desktop

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install cutecom $RPM_BUILD_ROOT%{_bindir}
install cutecom.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
