Name:		nagios-plugins-apache-threads
Version:	0.0
#Release:	1%{?dist}
Release:	1
Summary:	Nagios Plugin - check_apache_threads

Group:		Applications/Systems
License:	CC-BY-SA 4.0
URL:		https://bgstack15.wordpress.com/
Source0:	nagios-plugins-apache-threads.tgz

#BuildRequires:	
Requires:	nagios-plugins

%description
Provides check_apache_threads support for Nagios. 
In nagios/nconf, use this checkcommand check command line: $USER1$/check_by_ssh -H $HOSTADDRESS$ -C "$USER1$/check_apache_threads -w $ARG1$ -c $ARG2$"

%prep
%setup -q

%build

%install
#make install DESTDIR=%{buildroot}
rm -rf %{buildroot}
rsync -a . %{buildroot}/ --exclude='**/.*.swp'

%files
%doc %attr(0444, -, -) /usr/share/nagios-plugins-apache-threads/README.txt
/usr/share/nagios-plugins-apache-threads/nagios-plugins-apache-threads.spec
/usr/share/nagios-plugins-apache-threads/pack
/usr/share/nagios-plugins-apache-threads/localize_git.sh
%doc %attr(0444, -, -) /usr/share/nagios-plugins-apache-threads/scrub.txt
%doc %attr(0444, -, -) /usr/share/nagios-plugins-apache-threads/files-for-versioning.txt
%attr(0755, root, root) /usr/lib/nagios/plugins/check_apache_threads
%changelog
* Tue Jan 10 2017 B Stack <bgstack15@gmail.com> 0.0-1
- Initial build
