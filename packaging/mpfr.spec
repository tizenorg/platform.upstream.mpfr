%define keepstatic 1
Name:           mpfr
Version:        3.1.2
Release:        0
License:        LGPL-3.0+
Summary:        The GNU multiple-precision floating-point library
Url:            http://www.mpfr.org/
Group:          Base/Libraries
Source:         mpfr-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001:     mpfr.manifest
BuildRequires:  gmp-devel

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

The main goal of MPFR is to provide a library for multiple-precision
floating-point computation which is both efficient and has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit
mantissa).

%package -n libmpfr
Summary:        The GNU multiple-precision floating-point shared library
Group:          Base/Libraries

%description -n libmpfr
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%package devel
Summary:        Development files for the GNU multiple-precision floating-point library
Group:          Base/Libraries
Requires:       gmp-devel
Requires:       libmpfr = %{version}

%description devel
Development files for the GNU multiple-precision floating-point library.

The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure \
    --enable-thread-safe \
    --enable-shared
%__make %{?_smp_mflags}

%check
%__make check %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -n libmpfr -p /sbin/ldconfig

%postun -n libmpfr -p /sbin/ldconfig


%files -n libmpfr
%manifest %{name}.manifest
%license COPYING.LESSER COPYING
%defattr(-,root,root)
%{_libdir}/libmpfr.so.4*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libmpfr.a
%{_libdir}/libmpfr.so
%{_includedir}/mpf2mpfr.h
%{_includedir}/mpfr.h
