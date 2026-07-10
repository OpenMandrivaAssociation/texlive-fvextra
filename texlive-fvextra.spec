%global tl_name fvextra
%global tl_revision 78296

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.14.0
Release:	%{tl_revision}.1
Summary:	Extensions and patches for fancyvrb
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fvextra
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fvextra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fvextra.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fvextra.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(fancyvrb)
Requires:	texlive(lineno)
Requires:	texlive(upquote)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides several extensions to fancyvrb, including
automatic line breaking and improved math mode. It also patches some
fancyvrb internals. Parts of fvextra were originally developed as part
of pythontex and minted.

