#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	CSV_File
Summary:	Tie::CSV_File - ties a csv-file to an array of arrays
#Summary(pl):	
Name:		perl-Tie-CSV_File
Version:	0.11
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Data-Compare
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-Tie-File
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C<Tie::CSV_File> represents a regular csv file as a Perl array of arrays.
The first dimension of the represents the line-nr in the original
file, the second dimension represents the col-nr.  Both indices are
starting with 0.  You can also access with the normal array value,
e.g. C<$data[-1][-1]> stands for the last field in the last line, or
C<@{$data[1]}> stands for the columns of the second line.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
