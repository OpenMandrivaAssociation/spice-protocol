%define _disable_rebuild_configure 1

Name:		spice-protocol
Version:	0.14.3
Release:	1
Summary:	Spice protocol header files
Group:		System/Libraries
# Main headers are BSD, controller / foreign menu are LGPL, macros.h is GPL?
License:	BSD and LGPLv2+ and GPLv2+
URL:		http://www.spice-space.org/
Source0:	http://www.spice-space.org/download/releases/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildArch:	noarch
BuildRequires:	meson

###########################################################################
# Import cross patches spice-gtk, spice-protocol and spice-vdagent (angry)#
###########################################################################

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING CHANGELOG.md
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc
