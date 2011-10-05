%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from merb-core-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname merb-core
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Merb plugin that provides caching (page, action, fragment, object)
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 1.1.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://merbivore.com/
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
Requires: %{?ruby_dist_dash}rubygem(extlib) >= 0.9.13
Requires: %{?ruby_dist_dash}rubygem(erubis) >= 2.6.2
Requires: %{?ruby_dist_dash}rubygem(rake) >= 0
Requires: %{?ruby_dist_dash}rubygem(rack) >= 0
Requires: %{?ruby_dist_dash}rubygem(mime-types) >= 1.16
Requires: %{?ruby_dist_dash}rubygem(bundler) >= 0
BuildRequires: %{?ruby_dist_dash}rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
Merb. Pocket rocket web framework.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
                --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x
rm -rf %{buildroot}%{geminstdir}/spec10

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/merb
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/TODO
%doc %{geminstdir}/CHANGELOG
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.1.3-1.hhg
- Rebuild for Ruby Enterprise Edition

* Thu Apr 28 2011 Sergio Rubio <rubiojr@frameos.org> - 1.1.3-1
- Initial package
