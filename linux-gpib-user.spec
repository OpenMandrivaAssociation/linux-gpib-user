%define oname linux-gpib
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%define pymodule python-gpib
%define tclname tcl-gpib

Name:		linux-gpib-user
Version:	4.3.7
Release:	1
Summary:	The Linux GPIB support package for the kernel GPIB (IEEE 488) modules.
URL:		https://sourceforge.net/projects/linux-gpib/
License:	GPL-2.0-only
Group:		System/Utilities
Source0:	https://sourceforge.net/projects/linux-gpib/files/linux-gpib%20for%203.x.x%20and%202.6.x%20kernels/%{version}/linux-gpib-%{version}.tar.gz

#BuildSystem:	autotools

BuildRequires:	autoconf automake slibtool
BuildRequires:	bison
BuildRequires:	docbook2x
BuildRequires:	docbook-utils
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-style-xsl-ns
BuildRequires:	flex
BuildRequires:	opensp
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(tcl)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	xsltproc

Recommends:	%{name}-doc = %{version}-%{release}

%description
The Linux GPIB support package for the kernel GPIB (IEEE 488) modules.


%package -n %{libname}
Summary:	Shared libraries for the Linux GPIB support package
Group:	Development/C
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the shared libraries for the Linux GPIB
support for the kernel GPIB (IEEE 488) modules.


%package -n %{devname}
Summary:	Development headers and libraries for the Linux GPIB support package
Group:	Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the development headers and libraries for
the Linux GPIB support for the kernel GPIB (IEEE 488) modules.


%package -n %{pymodule}
Summary:	Pyhton bindings for the Linux GPIB support package
Group:	Development/Python

%description -n %{pymodule}
This package contains the python bindings for the Linux GPIB
support for the kernel GPIB (IEEE 488) modules.
Requires:	%{name} = %{version}-%{release}


%package -n %{tclname}
Summary:	TCL bindings for the Linux GPIB support package
Group:	Development/TCL
Requires:	%{name} = %{version}-%{release}

%description -n %{tclname}
This package contains the TCL bindings for the Linux GPIB
support for the kernel GPIB (IEEE 488) modules.


%package doc
Summary:	Documentation for for the Linux GPIB support package
Group:	Documentation
BuildArch: noarch

%description doc
This package contains the documentation for the Linux GPIB
support for the kernel GPIB (IEEE 488) modules.


%prep
%autosetup -n %{oname}-%{version} -p1

echo $PWD
tar xf %{name}-%{version}.tar.gz -C %{builddir}/%{oname}-%{version} --strip-components=1

%build
./configure --help
./configure  \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--sysconfdir=%{_sysconfdir}
%make_build

%install
%make_install

# Copy device readme files into docdir
cp -f ./{README.HAMEG,README.hp82335} %{buildroot}%{_docdir}/%{name}


%files
%doc README
%license COPYING
%{_bindir}/findlisteners
%{_bindir}/ibterm
%{_bindir}/ibtest
%{_prefix}/sbin/gpib_config
%{_prefix}/lib/udev/gpib_udev_config
%{_prefix}/lib/udev/gpib_udev_fxloader
%{_prefix}/lib/udev/gpib_udevadm_wrapper
%config(noreplace) %{_sysconfdir}/gpib.conf
%{_sysconfdir}/udev/rules.d/

%files -n %{libname}
%exclude %{_libdir}/libgpib_tcl*
%{_libdir}/libgpib*.so.*

%files -n %{devname}
%license COPYING
%{_includedir}/gpib/*
%exclude %{_libdir}/libgpib_tcl*
%{_libdir}/libgpib*.so
%{_libdir}/pkgconfig/libgpib.pc

%files -n %{pymodule}
%{_libdir}/python%{pyver}/*

%files -n %{tclname}
%{_libdir}/libgpib_tcl*

%files doc
%exclude %{_docdir}/linux-gpib-user/README
%{_docdir}/linux-gpib-user/*
%{_mandir}/*
