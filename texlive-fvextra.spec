Name:		texlive-fvextra
Version:	72706
Release:	1
Summary:	Extensions and patches for fancyvrb
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fvextra
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fvextra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fvextra.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fvextra.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
fvextra provides several extensions to fancyvrb, including
automatic line breaking and improved math mode. It also patches
some fancyvrb internals. Parts of fvextra were originally
developed as part of pythontex and minted.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fvextra
%{_texmfdistdir}/tex/latex/fvextra
%doc %{_texmfdistdir}/doc/latex/fvextra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
