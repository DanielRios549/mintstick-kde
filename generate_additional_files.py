#!/usr/bin/python3

DOMAIN = "mintstick"
PATH = "/usr/share/linuxmint/locale"

import os, gettext
from mintcommon import additionalfiles

os.environ['LANGUAGE'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)

prefix="""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE policyconfig PUBLIC
 "-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
 "http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>

  <vendor>Linux Mint</vendor>
  <vendor_url>https://linuxmint.com</vendor_url>

  <action id="com.linuxmint.mintstick">
    <description>USB Image Writer / USB Stick Formatter</description>
"""

suffix="""
    <icon_name>mintstick</icon_name>
    <defaults>
      <allow_any>no</allow_any>
      <allow_inactive>no</allow_inactive>
      <allow_active>auth_self_keep</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">/usr/bin/python3</annotate>
    <annotate key="org.freedesktop.policykit.exec.argv1">/usr/lib/linuxmint/mintstick/raw_write.py</annotate>
    <annotate key="org.freedesktop.policykit.exec.argv1">/usr/lib/linuxmint/mintstick/raw_format.py</annotate>
  </action>

</policyconfig>
"""

additionalfiles.generate_polkit_policy(DOMAIN, PATH, "share/polkit/com.linuxmint.mintstick.policy", prefix, _("This will destroy all data on the USB stick, are you sure you want to proceed?"), suffix)

