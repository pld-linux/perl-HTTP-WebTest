#
# Conditional build:
%bcond_with tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTTP
%define		pnam	WebTest
Summary:	HTTP::WebTest - test static and dynamic web content
Summary(pl):	HTTP::WebTest - testowanie statycznych i dynamicznych tre�ci z WWW
Name:		perl-HTTP-WebTest
Version:	2.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16bfb8e76bf301e788241d774cab7cee
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Algorithm-Diff
BuildRequires:	perl-Test-Builder-Tester
# Not in PLD yet
BuildRequires:	perl-Test-MockObject
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module runs tests on remote URLs containing
Perl/JSP/HTML/JavaScript/etc. and generates a detailed test report.
This module can be used "as-is" or its functionality can be extended
using plugins. Plugins can define test types and provide additional
report capabilities. This module comes with a set of default plugins
but can be easily extended with third party plugins.

The wt script is provided for running HTTP::WebTest from the command
line.

%description -l pl
Ten modu� uruchamia testy na zdalnych URL-ach zawieraj�cych
Perla/JSP/HTML/JavaScript/itp. i generuje szczeg�owy raport z testu.
Ten modu� mo�e by� u�ywany samodzielnie lub z funkcjonalno�ci�
rozszerzon� przy pomocy wtyczek. Wtyczki mog� definiowa� rodzaje
test�w i dostarcza� dodatkowe mo�liwo�ci raportowania. Ten modu�
zawiera zestaw domy�lnych wtyczek, ale mo�na go �atwo rozszerzy� o
zewn�trzne wtyczki.

Za��czony jest skrypt wt do uruchamiania HTTP::WebTest z linii
polece�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/wt
%{perl_vendorlib}/HTTP/*.pm
%dir %{perl_vendorlib}/HTTP/WebTest
%{perl_vendorlib}/HTTP/WebTest/*.pm
%dir %{perl_vendorlib}/HTTP/WebTest/Plugin
%{perl_vendorlib}/HTTP/WebTest/Plugin/*.pm
%{_mandir}/man3/*
%{_mandir}/man1/*
