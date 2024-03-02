# qmake sucks
%undefine _debugsource_packages

Name: polyphone
Version: 2.3.1
Release: 1
Source0: polyphone-2.3.1.zip
Summary: The Polyphone soundfont editor
URL: https://www.polyphone-soundfonts.com/
License: GPL-3.0
Group: Publishing
BuildRequires: pkgconfig(rtmidi)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisfile)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: qmake5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Svg)

%description
The Polyphone soundfont editor

%prep
%autosetup -p1 -c %{name}
sed -i \
	-e 's,#DEFINES += USE_LOCAL_STK,DEFINES += USE_LOCAL_STK,' \
	-e 's,#DEFINES += USE_LOCAL_QCUSTOMPLOT,DEFINES += USE_LOCAL_QCUSTOMPLOT,' \
	*.pro
qmake *.pro PREFIX=%{_prefix}

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-man

%files -f %{name}.lang
%{_bindir}/polyphone
%{_datadir}/mime/packages/polyphone.xml
%{_datadir}/icons/*/*/*/*
%{_datadir}/applications/com.polyphone_soundfonts.polyphone.desktop
%{_datadir}/metainfo/com.polyphone_soundfonts.polyphone.metainfo.xml
%{_mandir}/man1/polyphone.1*
%doc %{_docdir}/polyphone/changelog
