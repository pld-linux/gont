Summary:	The Gont compiler
Summary(pl):	Kompilator jêzyka Gont
Name:		gont
Version:	0.0.5
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	ftp://ftp.kernel.pl/pub/People/malekith/gont/%{name}-%{version}.tar.bz2
URL:		http://gont.pld.org.pl/
BuildRequires:	bison
BuildRequires:	gc-devel
BuildRequires:	gperf
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	gcc-ksi
BuildRequires:	perl
Requires:	gcc-ksi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gont tries to merge imperative look and feel of C with with polymorphic
typesystem, higher order functions and high level data structures. It
is meant to be easy to learn and safe but yet powerful and general. 
Both compiler and language are under heavy development.

%description -l pl
Gont próbuje ³±czyæ imperatywny styl znany z C z polimorficznym systemem
typów, funkcjami wy¿szych rzêdów oraz wysoko-poziomowymi strukturami danych.
W za³o¿eniach ma byæ ³atwy do nauczenia i bezpieczny ale mimo to
silny i ogólny. Zarówno kompilator jak i jêzyk podlegaj± silnemu rozwojowi.

%prep
%setup -q

%build
./configure \
	-prefix %{_prefix}

%{__make} boot BOOT_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{faq,manual,hacker} doc/gont.vim COPYRIGHT NEWS TODO
%doc lib/*/*.gi t/hello.g*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_includedir}/%{name}
%{_mandir}/man*/*
