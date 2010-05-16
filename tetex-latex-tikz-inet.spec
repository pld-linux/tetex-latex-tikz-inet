
%define short_name tikz-inet
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Draw interaction nets with TikZ
Summary(hu.UTF-8):	Hálózatok rajzolása TikZ-zel
Name:		tetex-latex-%{short_name}
Version:	0.1.1
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=tikz-inet
Source0:	http://www.ctan.org/get/graphics/pgf/contrib/%{short_name}.zip
# Source0-md5:	7ac97b9ad3d4d6ed5b6ec45894f1496c
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
Requires:	tetex-pgf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package extends TikZ with macros to draw interaction nets.

%description -l hu.UTF-8
Ez a csomag a TikZ-et kiterjeszti olyan makrókkal, amelyekkel
hálózatokat lehet rajzolni.

%prep
%setup -q -n %{short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/tikz/%{short_name}
install %{short_name}-doc.pdf %{short_name}-doc.tex $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/tikz/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/texmf/doc/latex/tikz
%{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/doc/latex/tikz/%{short_name}
