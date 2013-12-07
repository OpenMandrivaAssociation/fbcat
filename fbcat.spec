Summary:	Framebuffer screenshot program
Name:		fbcat
Epoch:		1
Version:	0.3
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		http://code.google.com/p/fbcat/
Source0:	http://fbcat.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	docbook-style-xsl
BuildRequires:	xsltproc
%rename fbgrab

%description
fbcat takes a screenshot using the framebuffer device.

The following visuals are supported:
    TRUECOLOR,
    DIRECTCOLOR,
    PSEUDOCOLOR,
    STATIC_PSEUDOCOLOR.

It's a modern replacement for fbgrab.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"
%make -C doc

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 fbcat %{buildroot}%{_bindir}/
install -m 755 fbgrab %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 755 doc/fbcat.1 %{buildroot}%{_mandir}/man1/
install -m 755 doc/fbgrab.1 %{buildroot}%{_mandir}/man1/

%files
%doc COPYING
%{_bindir}/fbcat
%{_bindir}/fbgrab
%{_mandir}/man1/fbcat.1*
%{_mandir}/man1/fbgrab.1*

