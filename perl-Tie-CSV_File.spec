#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	CSV_File
Summary:	Tie::CSV_File Perl module - ties a csv-file to an array of arrays
Summary(pl):	Modu� Perla Tie::CSV_File - zwi�zanie pliku CSV z tablic� tablic
Name:		perl-Tie-CSV_File
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a9a4a436b96a5e88538264612af3a1e
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Data-Compare
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warn >= 0.05
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-Tie-File
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::CSV_File represents a regular csv file as a Perl array of arrays.
The first dimension of the array represents the line-nr in the
original file, the second dimension represents the col-nr. Both
indices are starting with 0. You can also access with the normal array
value, e.g. $data[-1][-1] stands for the last field in the last line,
or @{$data[1]} stands for the columns of the second line.

%description -l pl
Tie::CSV_File reprezentuje zwyk�y plik CSV jako perlow� tablic�
tablic. Pierwszy wymiar reprezentuje numer linii w pliku, drugi wymiar
numer kolumny. Oba indeksy zaczynaj� si� od 0. Mo�na korzysta� z
w�asno�ci tablic, np. $data[-1][-1] oznacza ostatnie pole w ostatniej
linii, a @{$data[1]} oznacza kolumny z drugiej linii.

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
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
