#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	NNTPGateway
Summary:	Apache::NNTPGateway - A NNTP interface for mod_perl enabled Apache web server
#Summary(pl):	
Name:		perl-Apache-NNTPGateway
Version:	0.9
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	apache-mod_perl >= 1.20
BuildRequires:	perl-CGI >= 1.10
BuildRequires:	perl-libnet
BuildRequires:	perl-MailTools >= 1.10
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a per group interface to NNTP (Usenet) News-Groups,
it allow users to list, read, post, followup ... articles in a given
newsgroup/newsserver depending of configuration.  This is not a
replacement for a real powerful newsreader client but just pretend to
be a simple, useful mapping of some news articles into a web space.

# %description -l pl
# TODO

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
