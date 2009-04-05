Name:           ocaml-type-conv
Version:        1.6.7
Release:        %mkrel 1
Summary:        OCaml base library for type conversion

Group:          Development/Other
License:        LGPLv2+ with exceptions and BSD
URL:            http://www.ocaml.info/home/ocaml_sources.html#type-conv
Source0:        http://hg.ocaml.info/release/type-conv/archive/type-conv-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/type-conv/archive/release-%{version}.tar.bz2 > type-conv-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRequires:  dos2unix

%description
The type-conv mini library factors out functionality needed by
different preprocessors that generate code from type specifications,
because this functionality cannot be duplicated without losing the
ability to use these preprocessors simultaneously.

%prep
%setup -q -n type-conv-release-%{version}
dos2unix LICENSE.Tywith

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE LICENSE.Tywith CHANGES COPYRIGHT README.txt
%{_libdir}/ocaml/type-conv

