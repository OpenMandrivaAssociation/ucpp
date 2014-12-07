%define	major	13
%define libname %mklibname ucpp %{major}
%define devname %mklibname ucpp -d 

Summary:	A quick and light preprocessor, but anyway fully compliant to C99
Name:		ucpp
Version:	1.3.4
Release:	9
License:	BSD-3-Clause
Group:		Development/C++
Url:		http://code.google.com/p/ucpp/
Source0:	http://dev.gentooexperimental.org/~scarabeus/%{name}-%{version}.tar.xz

%description
A C preprocessor is a part of a C compiler responsible for macro
replacement, conditional compilation and inclusion of header files.
It is often found as a stand-alone program on Unix systems.

ucpp is such a preprocessor; it is designed to be quick and light,
but anyway fully compliant to the ISO standard 9899:1999, also known
as C99. ucpp can be compiled as a stand-alone program, or linked to
some other code; in the latter case, ucpp will output tokens, one
at a time, on demand, as an integrated lexer.

ucpp operates in two modes:
-- lexer mode: ucpp is linked to some other code and outputs a stream of
tokens (each call to the lex() function will yield one token)
-- non-lexer mode: ucpp preprocesses text and outputs the resulting text
to a file descriptor; if linked to some other code, the cpp() function
must be called repeatedly, otherwise ucpp is a stand-alone binary.

%package -n %{libname}
Summary:	A Mixed Integer Linear Programming (MILP) Solver Library
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}

%package -n %{devname}
Summary:	Files for Developing with ucpp
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Includes and definitions for developing with the ucpp library.

%prep
%setup -q

%build
CFLAGS="%{optflags} -Qunused-arguments" \
CXXFLAGS="%{optflags} -Qunused-arguments" \
%configure \
	--disable-static

%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/man1/ucpp.1*

%files -n %{libname}
%{_libdir}/libucpp.so.%{major}*

%files -n %{devname}
%{_includedir}/lib%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}*.pc

