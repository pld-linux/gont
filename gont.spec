Summary:	The Gont compiler
Summary(pl.UTF-8):	Kompilator języka Gont
Name:		gont
Version:	0.0.10
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	ftp://ftp.kernel.pl/pub/People/malekith/gont/%{name}-%{version}.tar.bz2
# Source0-md5:	03a48e9c9976d9011b8db9f962a6f3ae
URL:		http://gont.pld.org.pl/
BuildRequires:	bison
BuildRequires:	gc-devel
BuildRequires:	gcc-ksi
BuildRequires:	gperf
BuildRequires:	iconv
BuildRequires:	libxml2-devel
BuildRequires:	perl
BuildRequires:	pkgconfig
Requires:	gcc-ksi
Requires:	iconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gont tries to merge imperative look and feel of C with with polymorphic
typesystem, higher order functions and high level data structures. It
is meant to be easy to learn and safe but yet powerful and general.
Both compiler and language are under heavy development.

%description -l pl.UTF-8
Gont próbuje łączyć imperatywny styl znany z C z polimorficznym systemem
typów, funkcjami wyższych rzędów oraz wysoko-poziomowymi strukturami danych.
W założeniach ma być łatwy do nauczenia i bezpieczny ale mimo to
silny i ogólny. Zarówno kompilator jak i język podlegają silnemu rozwojowi.

%prep
%setup -q

%build
./configure \
	-prefix %{_prefix} \
	-ksic %{__cc}

%{__make} boot \
	BOOT_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp doc/tutorial/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{faq,manual,hacker,proposals,libref} doc/gont.vim COPYRIGHT NEWS TODO
%doc lib/*/*.gi
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_includedir}/%{name}
%{_mandir}/man*/*
%{_examplesdir}/%{name}-%{version}
