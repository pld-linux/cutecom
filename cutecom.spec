Summary:	A graphical serial terminal
Summary(pl.UTF-8):	Graficzny terminal szeregowy
Name:		cutecom
Version:	0.20.0
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://cutecom.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	a42394c3a29a2dc30edab721469f5eee
URL:		http://cutecom.sourceforge.net/
Patch0:		%{name}-man_path.patch
BuildRequires:	cmake > 2.4.3
BuildRequires:	qt4-build
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
%patch0 -p1

echo "Categories=Qt;TerminalEmulator;" >> ./cutecom.desktop

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install cutecom.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/cutecom
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
