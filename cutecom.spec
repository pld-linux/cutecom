Summary:	A graphical serial terminal
Summary(pl):	Graficzny terminal szeregowy
Name:		cutecom
Version:	0.13.2
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://cutecom.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	d115eb003ef8b119503050da0b4486e0
URL:		http://cutecom.sourceforge.net
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cutecom is a graphical serial terminal, like minicom. It is aimed
mainly at hardware developers or other people who need a terminal to
talk to their devices.

%description -l pl
Cutecom to graficzny terminal szeregowy podobny do minicoma. Jest
przeznaczony g³ównie dla twórców sprzêtu i innych ludzi potrzebuj±cych
terminala do komunikacji ze swoimi urz±dzeniami.
%prep
%setup -q

%build
./configure
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
%{_desktopdir}/*
