Summary:	Cataloging software for CDs and DVDs
Summary(hu.UTF-8):	CD-k és DVD-k katalogizálása
Name:		gnomecatalog
Version:	0.3.4.2
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/project/gnomecatalog/%{name}-%{version}.tar.bz2
# Source0-md5:	ab5d51e0bdc8bc14c1c4d34c9ca337d3
URL:		http://www.gnomecatalog.org/
BuildRequires:	python-devel
Requires:	python-gnome-ui
Requires:	python-kaa-metadata
Requires:	python-pygtk-gtk
Requires:	python-sqlite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cataloging software for CDs and DVDs. Catalog your dvds/cds and files
in your hard disk. Generate thumbnails of files and saves it in the
database files. Save the metadata of the files mp3, avis, images. You
can export to csv files and import cdcat files.

%description -l hu.UTF-8
CD-k és DVD-k katalogizálása. A dvd/cd-idet és fájljaidat
katagerizálja a merevlemezedre. Bélyegképeket készít a fájlokból és
azokat egy adatbázisba menti. Az mp3, avi és képek metainformációit is
eltárolja. Exportálhatod csv fájlokba és importálhatsz cdcat fájlokat.

%prep
%setup -q

%build
%{__python} setup.py build --executable %{__python}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root $RPM_BUILD_ROOT
%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc AUTHORS ChangeLog NEWS README TODO
%{_mandir}/man1/%{name}*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/48x48/mimetypes/gnome-mime-application-x-gcatalog.png
%{_datadir}/%{name}
%{_datadir}/mime/packages/%{name}.xml
%{py_sitescriptdir}/%{name}
%{_datadir}/application-registry/%{name}*
%{_datadir}/mime-info/%{name}*
# Doesn't include %find_lang
%{_datadir}/locale/en/LC_MESSAGES/gnomecatalog.mo
%{py_sitescriptdir}/gnomecatalog-0.3.4-py2.6.egg-info
