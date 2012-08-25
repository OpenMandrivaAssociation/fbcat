Summary:	Framebuffer screenshot program
Name:		fbcat
Version:	0.3
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphics
Url:		http://code.google.com/p/fbcat/
Source:		http://fbcat.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
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
%__mkdir_p %{buildroot}%{_bindir}
%__install -m 755 fbcat %{buildroot}%{_bindir}/
%__install -m 755 fbgrab %{buildroot}%{_bindir}/
%__mkdir_p %{buildroot}%{_mandir}/man1/
%__install -m 755 doc/fbcat.1 %{buildroot}%{_mandir}/man1/
%__install -m 755 doc/fbgrab.1 %{buildroot}%{_mandir}/man1/

%files
%doc COPYING
%{_bindir}/fbcat
%{_bindir}/fbgrab
%{_mandir}/man1/fbcat.1*
%{_mandir}/man1/fbgrab.1*

