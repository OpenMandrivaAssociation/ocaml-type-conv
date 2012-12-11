Name:           ocaml-type-conv
Version:        2.0.1
Release:        %mkrel 1
Summary:        OCaml base library for type conversion

Group:          Development/Other
License:        LGPLv2+ with exceptions and BSD
URL:            http://www.ocaml.info/home/ocaml_sources.html#type-conv
Source0:        http://hg.ocaml.info/release/type-conv/archive/release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/type-conv/archive/release-%{version}.tar.bz2 > type-conv-release-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRequires:  dos2unix
Requires:       camlp4

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
%doc LICENSE LICENSE.Tywith Changelog COPYRIGHT README.txt
%{_libdir}/ocaml/type-conv



%changelog
* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 583579
- New version 2.0.1

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.10-3mdv2010.1
+ Revision: 496359
- rebuild

* Tue Sep 22 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.10-2mdv2010.0
+ Revision: 447061
- rebuild
- new version

* Sat Sep 12 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.8-3mdv2010.0
+ Revision: 438545
- added Requires: camlp4

* Tue Jul 28 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.8-2mdv2010.0
+ Revision: 401362
- updated version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.7-2mdv2010.0
+ Revision: 390308
- rebuild

* Sun Apr 05 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.7-1mdv2010.0
+ Revision: 364185
- updated version
- The initial RPM release was made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones

* Wed Jan 07 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.5-1mdv2009.1
+ Revision: 326698
- corrected group
- import ocaml-type-conv


* Sat Dec 20 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.6.5-1mdv
- Initial RPM release made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones
# found there: http://cvs.fedoraproject.org/viewvc/devel/ocaml-type-conv/ocaml-type-conv.spec
