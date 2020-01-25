#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Apache
%define		pnam	NNTPGateway
Summary:	Apache::NNTPGateway - A NNTP interface for mod_perl enabled Apache web server
Summary(pl.UTF-8):	Apache::NNTPGateway - interfejs NNTP dla serwera WWW Apache z mod_perlem
Name:		perl-Apache-NNTPGateway
Version:	0.9
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b14703a19ed3c8a763d865a46b6116b5
URL:		http://search.cpan.org/dist/Apache-NNTPGateway/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{with tests}
BuildRequires:	apache1-mod_perl >= 1.20
BuildRequires:	perl-CGI >= 1.10
BuildRequires:	perl-MailTools >= 1.10
BuildRequires:	perl-libnet
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a per group interface to NNTP (Usenet)
News-Groups, it allow users to list, read, post, followup... articles
in a given newsgroup/newsserver depending of configuration. This is
not a replacement for a real powerful newsreader client but just
pretend to be a simple, useful mapping of some news articles into a
web space.

%description -l pl.UTF-8
Ten moduł jest implementacją interfejsu do usenetowych grup
dyskusyjnych (NNTP). Pozwala użytkownikom przeglądać, czytać, wysyłać,
odpowiadać... na artykuły z podanej grupy i serwera, w zależności od
konfiguracji. Nie jest to zamiennik klienta newsów z prawdziwego
zdarzenia, ale ma być prostym, użytecznym odwzorowaniem artykułów
newsowych w przestrzeni WWW.

%prep
%setup -q -n %{pnam}-%{version}
%{__perl} -pi -e 's/^(require 5.005)(02;)$/$1_$2/' NNTPGateway.pm

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
%doc Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
