%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml base library for type conversion
Name:		ocaml-type-conv
Version:	2.0.1
Release:	2
Group:		Development/Other
License:	LGPLv2+ with exceptions and BSD
Url:		http://www.ocaml.info/home/ocaml_sources.html#type-conv
Source0:	http://hg.ocaml.info/release/type-conv/archive/release-%{version}.tar.bz2
BuildRequires:	ocaml >= 3.10.0
BuildRequires:	ocaml-findlib
BuildRequires:	camlp4
BuildRequires:	dos2unix
Requires:	camlp4

%description
The type-conv mini library factors out functionality needed by
different preprocessors that generate code from type specifications,
because this functionality cannot be duplicated without losing the
ability to use these preprocessors simultaneously.

%files
%doc LICENSE LICENSE.Tywith Changelog COPYRIGHT README.txt
%{_libdir}/ocaml/type-conv

#----------------------------------------------------------------------------

%prep
%setup -q -n type-conv-release-%{version}
dos2unix LICENSE.Tywith

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

