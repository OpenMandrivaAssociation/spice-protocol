Name:           spice-protocol
Version:        0.12.6
Release:        7
Summary:        Spice protocol header files
Group:          System/Libraries
# Main headers are BSD, controller / foreign menu are LGPL, macros.h is GPL?
License:        BSD and LGPLv2+ and GPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
BuildArch:      noarch

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING NEWS
%{_includedir}/spice-1
%{_datadir}/pkgconfig/spice-protocol.pc
