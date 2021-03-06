#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	CSV_File
Summary:	Tie::CSV_File Perl module - ties a csv-file to an array of arrays
Summary(pl.UTF-8):	Moduł Perla Tie::CSV_File - związanie pliku CSV z tablicą tablic
Name:		perl-Tie-CSV_File
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce2ce8d542563731dbcd0ae7917946a4
URL:		http://search.cpan.org/dist/Tie-CSV_File/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-Compare
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-ManyParams
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warn >= 0.05
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-Tie-File
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::CSV_File represents a regular csv file as a Perl array of arrays.
The first dimension of the array represents the line-nr in the
original file, the second dimension represents the col-nr. Both
indices are starting with 0. You can also access with the normal array
value, e.g. $data[-1][-1] stands for the last field in the last line,
or @{$data[1]} stands for the columns of the second line.

%description -l pl.UTF-8
Tie::CSV_File reprezentuje zwykły plik CSV jako perlową tablicę
tablic. Pierwszy wymiar reprezentuje numer linii w pliku, drugi wymiar
numer kolumny. Oba indeksy zaczynają się od 0. Można korzystać z
własności tablic, np. $data[-1][-1] oznacza ostatnie pole w ostatniej
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
