Name:		texlive-biblatex-ext
Version:	70744
Release:	1
Summary:	Extended BibLaTeX standard styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-ext
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ext.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The BibLaTeX-ext bundle provides styles that slightly extend
the standard styles that ship with BibLaTeX. The styles offered
in this bundle provide a simple interface to change some of the
stylistic decisions made in the standard styles. At the same
time they stay as close to their standard counterparts as
possible, so that most customisation methods can be applied
here as well.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-ext
%doc %{_texmfdistdir}/doc/latex/biblatex-ext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
