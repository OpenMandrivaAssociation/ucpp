#
# spec file for package ucpp
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define libname libucpp13

Name:           ucpp
Summary:        A quick and light preprocessor, but anyway fully compliant to C99
License:        BSD-3-Clause
Group:          Development/Tools/Building
Version:        1.3.4
Release:        4.2
Url:            http://code.google.com/p/ucpp/
# http://github.com/scarabeusiv/ucpp
Source:         http://dev.gentooexperimental.org/~scarabeus/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  xz

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
Summary:        A Mixed Integer Linear Programming (MILP) Solver Library
Group:          Development/Libraries/Other

%description -n %{libname}
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

%package devel
Requires:       %{libname} = %{version}
Summary:        Files for Developing with ucpp
Group:          Development/Libraries/C and C++

%description devel
Includes and definitions for developing with the ucpp library.

%prep
%setup -q

%build
%configure \
	--disable-werror \
	--disable-static \
	--docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/ucpp.1.gz

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.1*

%files devel
%defattr(-,root,root,-)
%{_includedir}/lib%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}*.pc

%changelog
* Sat Apr 20 2013 tchvatal@suse.com
- Add http url path.
* Wed Dec 19 2012 tchvatal@suse.com
- Version bump to 1.3.4
  * this version moves all the options from header to conf switches
  * add possibility to use the headers in c++ apps
  * silences warnings
  * remove weird exit so buildservice does not complain
* Thu Nov 22 2012 tchvatal@suse.com
- Depend on xz for unpacking.
* Wed Nov 21 2012 tchvatal@suse.com
- Initial commit, required by libreoffice-4.0
