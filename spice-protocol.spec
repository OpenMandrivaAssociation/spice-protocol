%define _disable_rebuild_configure 1

Name:		spice-protocol
Version:	0.14.0
Release:	1
Summary:	Spice protocol header files
Group:		System/Libraries
# Main headers are BSD, controller / foreign menu are LGPL, macros.h is GPL?
License:	BSD and LGPLv2+ and GPLv2+
URL:		http://www.spice-space.org/
Source0:	http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
BuildArch:	noarch

###########################################################################
# Import cross patches spice-gtk, spice-protocol and spice-vdagent (angry)#
###########################################################################

# clipboard-race patches: together with patches for vdagent
# and spice-gtk these fix problems interacting with mutter's new
# clipboard manager
# https://bugzilla.redhat.com/show_bug.cgi?id=1755038
# all rebased by Jakub Janků:
# https://github.com/jjanku/spice-protocol/tree/clipboard-race
# https://patchwork.freedesktop.org/patch/293583/
Patch0:         0002-vdagent-introduce-VD_AGENT_CAP_CLIPBOARD_NO_RELEASE_.patch
# https://patchwork.freedesktop.org/patch/293584/
Patch1:         0003-vdagent-introduce-VD_AGENT_CAP_CLIPBOARD_GRAB_SERIAL.patch

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING CHANGELOG.md
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc
