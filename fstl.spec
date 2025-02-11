Summary:	A fast STL file viewer 
Name:		fstl
Version:	0.11.0
Release:	1
License:	AGPLv3
Group: 		Graphics
URL:		https://github.com/mkeeter/fstl.git
Source0:	https://github.com/fstl-app/fstl/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	icoutils
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	ninja
BuildRequires:	qmake5

%description
Fast stl file viewer.

It is designed to quickly load and render very high-polygon models;
showing 2 million triangles at 60+ FPS on a mid-range laptop.

%files
%{_bindir}/fstl
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_qt5 \
	-G Ninja
%ninja_build

%install
%ninja_install -C build


# icons
icotool -x exe/fstl.ico
#install -Dm 0644 %{name}.svg -t %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
i=1
for d in 16 32 48 64 128 256
do
	install -Dm 0755 fstl_${i}_${d}x${d}x32.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
	let "i+=1"
done
#install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
#convert -scale 32x32 %{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# .desktop
install -pm 0755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=FSTL
GenericName=Fast STL file viewer 
Comment=A fast STL file viewer 
Exec=%{name}
Icon=%{name}
MimeType=
Terminal=False
Type=Application
Categories=Qt;Graphics;3DGraphics;Viewer
EOF

