#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class vpnsessionaction(base_resource) :
	""" Configuration for VPN session action resource. """
	def __init__(self) :
		self._name = ""
		self._useraccounting = ""
		self._httpport = []
		self._winsip = ""
		self._dnsvservername = ""
		self._splitdns = ""
		self._sesstimeout = 0
		self._clientsecurity = ""
		self._clientsecuritygroup = ""
		self._clientsecuritymessage = ""
		self._clientsecuritylog = ""
		self._splittunnel = ""
		self._locallanaccess = ""
		self._rfc1918 = ""
		self._spoofiip = ""
		self._killconnections = ""
		self._transparentinterception = ""
		self._windowsclienttype = ""
		self._defaultauthorizationaction = ""
		self._authorizationgroup = ""
		self._clientidletimeout = 0
		self._proxy = ""
		self._allprotocolproxy = ""
		self._httpproxy = ""
		self._ftpproxy = ""
		self._socksproxy = ""
		self._gopherproxy = ""
		self._sslproxy = ""
		self._proxyexception = ""
		self._proxylocalbypass = ""
		self._clientcleanupprompt = ""
		self._forcecleanup = []
		self._clientoptions = []
		self._clientconfiguration = []
		self._sso = ""
		self._ssocredential = ""
		self._windowsautologon = ""
		self._usemip = ""
		self._useiip = ""
		self._clientdebug = ""
		self._loginscript = ""
		self._logoutscript = ""
		self._homepage = ""
		self._icaproxy = ""
		self._wihome = ""
		self._wihomeaddresstype = ""
		self._citrixreceiverhome = ""
		self._wiportalmode = ""
		self._clientchoices = ""
		self._epaclienttype = ""
		self._iipdnssuffix = ""
		self._forcedtimeout = 0
		self._forcedtimeoutwarning = 0
		self._ntdomain = ""
		self._clientlessvpnmode = ""
		self._emailhome = ""
		self._clientlessmodeurlencoding = ""
		self._clientlesspersistentcookie = ""
		self._allowedlogingroups = ""
		self._securebrowse = ""
		self._storefronturl = ""
		self._kcdaccount = ""
		self._clientidletimeoutwarning = 0
		self._builtin = []
		self.___count = 0

	@property
	def name(self) :
		"""Name for the NetScaler Gateway profile (action). Must begin with an ASCII alphabetic or underscore (_) character, and must consist only of ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		"""Name for the NetScaler Gateway profile (action). Must begin with an ASCII alphabetic or underscore (_) character, and must consist only of ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def useraccounting(self) :
		"""The name of the radiusPolicy to use for RADIUS user accounting info on the session.
		"""
		try :
			return self._useraccounting
		except Exception as e:
			raise e

	@useraccounting.setter
	def useraccounting(self, useraccounting) :
		"""The name of the radiusPolicy to use for RADIUS user accounting info on the session.
		"""
		try :
			self._useraccounting = useraccounting
		except Exception as e:
			raise e

	@property
	def httpport(self) :
		"""Destination port numbers other than port 80, added as a comma-separated list. Traffic to these ports is processed as HTTP traffic, which allows functionality, such as HTTP authorization and single sign-on to a web application to work.<br/>Minimum length =  1.
		"""
		try :
			return self._httpport
		except Exception as e:
			raise e

	@httpport.setter
	def httpport(self, httpport) :
		"""Destination port numbers other than port 80, added as a comma-separated list. Traffic to these ports is processed as HTTP traffic, which allows functionality, such as HTTP authorization and single sign-on to a web application to work.<br/>Minimum length =  1
		"""
		try :
			self._httpport = httpport
		except Exception as e:
			raise e

	@property
	def winsip(self) :
		"""WINS server IP address to add to NetScaler Gateway for name resolution.
		"""
		try :
			return self._winsip
		except Exception as e:
			raise e

	@winsip.setter
	def winsip(self, winsip) :
		"""WINS server IP address to add to NetScaler Gateway for name resolution.
		"""
		try :
			self._winsip = winsip
		except Exception as e:
			raise e

	@property
	def dnsvservername(self) :
		"""Name of the DNS virtual server for the user session.<br/>Minimum length =  1.
		"""
		try :
			return self._dnsvservername
		except Exception as e:
			raise e

	@dnsvservername.setter
	def dnsvservername(self, dnsvservername) :
		"""Name of the DNS virtual server for the user session.<br/>Minimum length =  1
		"""
		try :
			self._dnsvservername = dnsvservername
		except Exception as e:
			raise e

	@property
	def splitdns(self) :
		"""Route the DNS requests to the local DNS server configured on the user device, or NetScaler Gateway (remote), or both.<br/>Possible values = LOCAL, REMOTE, BOTH.
		"""
		try :
			return self._splitdns
		except Exception as e:
			raise e

	@splitdns.setter
	def splitdns(self, splitdns) :
		"""Route the DNS requests to the local DNS server configured on the user device, or NetScaler Gateway (remote), or both.<br/>Possible values = LOCAL, REMOTE, BOTH
		"""
		try :
			self._splitdns = splitdns
		except Exception as e:
			raise e

	@property
	def sesstimeout(self) :
		"""Number of minutes after which the session times out.<br/>Minimum length =  1.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		"""Number of minutes after which the session times out.<br/>Minimum length =  1
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def clientsecurity(self) :
		"""Specify the client security check for the user device to permit a NetScaler Gateway session. The web address or IP address is not included in the expression for the client security check.
		"""
		try :
			return self._clientsecurity
		except Exception as e:
			raise e

	@clientsecurity.setter
	def clientsecurity(self, clientsecurity) :
		"""Specify the client security check for the user device to permit a NetScaler Gateway session. The web address or IP address is not included in the expression for the client security check.
		"""
		try :
			self._clientsecurity = clientsecurity
		except Exception as e:
			raise e

	@property
	def clientsecuritygroup(self) :
		"""The client security group that will be assigned on failure of the client security check. Users can in general be organized into Groups. In this case, the Client Security Group may have a more restrictive security policy.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecuritygroup
		except Exception as e:
			raise e

	@clientsecuritygroup.setter
	def clientsecuritygroup(self, clientsecuritygroup) :
		"""The client security group that will be assigned on failure of the client security check. Users can in general be organized into Groups. In this case, the Client Security Group may have a more restrictive security policy.<br/>Minimum length =  1
		"""
		try :
			self._clientsecuritygroup = clientsecuritygroup
		except Exception as e:
			raise e

	@property
	def clientsecuritymessage(self) :
		"""The client security message that will be displayed on failure of the client security check.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._clientsecuritymessage
		except Exception as e:
			raise e

	@clientsecuritymessage.setter
	def clientsecuritymessage(self, clientsecuritymessage) :
		"""The client security message that will be displayed on failure of the client security check.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._clientsecuritymessage = clientsecuritymessage
		except Exception as e:
			raise e

	@property
	def clientsecuritylog(self) :
		"""Set the logging of client security checks.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._clientsecuritylog
		except Exception as e:
			raise e

	@clientsecuritylog.setter
	def clientsecuritylog(self, clientsecuritylog) :
		"""Set the logging of client security checks.<br/>Possible values = ON, OFF
		"""
		try :
			self._clientsecuritylog = clientsecuritylog
		except Exception as e:
			raise e

	@property
	def splittunnel(self) :
		"""Send, through the tunnel, traffic only for intranet applications that are defined in NetScaler Gateway. Route all other traffic directly to the Internet. The OFF setting routes all traffic through NetScaler Gateway. With the REVERSE setting, intranet applications define the network traffic that is not intercepted. All network traffic directed to internal IP addresses bypasses the VPN tunnel, while other traffic goes through NetScaler Gateway. Reverse split tunneling can be used to log all non-local LAN traffic. For example, if users have a home network and are logged on through the NetScaler Gateway Plug-in, network traffic destined to a printer or another device within the home network is not intercepted.<br/>Possible values = ON, OFF, REVERSE.
		"""
		try :
			return self._splittunnel
		except Exception as e:
			raise e

	@splittunnel.setter
	def splittunnel(self, splittunnel) :
		"""Send, through the tunnel, traffic only for intranet applications that are defined in NetScaler Gateway. Route all other traffic directly to the Internet. The OFF setting routes all traffic through NetScaler Gateway. With the REVERSE setting, intranet applications define the network traffic that is not intercepted. All network traffic directed to internal IP addresses bypasses the VPN tunnel, while other traffic goes through NetScaler Gateway. Reverse split tunneling can be used to log all non-local LAN traffic. For example, if users have a home network and are logged on through the NetScaler Gateway Plug-in, network traffic destined to a printer or another device within the home network is not intercepted.<br/>Possible values = ON, OFF, REVERSE
		"""
		try :
			self._splittunnel = splittunnel
		except Exception as e:
			raise e

	@property
	def locallanaccess(self) :
		"""Set local LAN access. If split tunneling is OFF, and you set local LAN access to ON, the local client can route traffic to its local interface. When the local area network switch is specified, this combination of switches is useful. The client can allow local LAN access to devices that commonly have non-routable addresses, such as local printers or local file servers.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._locallanaccess
		except Exception as e:
			raise e

	@locallanaccess.setter
	def locallanaccess(self, locallanaccess) :
		"""Set local LAN access. If split tunneling is OFF, and you set local LAN access to ON, the local client can route traffic to its local interface. When the local area network switch is specified, this combination of switches is useful. The client can allow local LAN access to devices that commonly have non-routable addresses, such as local printers or local file servers.<br/>Possible values = ON, OFF
		"""
		try :
			self._locallanaccess = locallanaccess
		except Exception as e:
			raise e

	@property
	def rfc1918(self) :
		"""As defined in the local area network, allow only the following local area network addresses to bypass the VPN tunnel when the local LAN access feature is enabled:
		* 10.*.*.*,
		* 172.16.*.*,
		* 192.168.*.*.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._rfc1918
		except Exception as e:
			raise e

	@rfc1918.setter
	def rfc1918(self, rfc1918) :
		"""As defined in the local area network, allow only the following local area network addresses to bypass the VPN tunnel when the local LAN access feature is enabled:
		* 10.*.*.*,
		* 172.16.*.*,
		* 192.168.*.*.<br/>Possible values = ON, OFF
		"""
		try :
			self._rfc1918 = rfc1918
		except Exception as e:
			raise e

	@property
	def spoofiip(self) :
		"""IP address that the intranet application uses to route the connection through the virtual adapter.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._spoofiip
		except Exception as e:
			raise e

	@spoofiip.setter
	def spoofiip(self, spoofiip) :
		"""IP address that the intranet application uses to route the connection through the virtual adapter.<br/>Possible values = ON, OFF
		"""
		try :
			self._spoofiip = spoofiip
		except Exception as e:
			raise e

	@property
	def killconnections(self) :
		"""Specify whether the NetScaler Gateway Plug-in should disconnect all preexisting connections, such as the connections existing before the user logged on to NetScaler Gateway, and prevent new incoming connections on the NetScaler Gateway Plug-in for Windows and MAC when the user is connected to NetScaler Gateway and split tunneling is disabled.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._killconnections
		except Exception as e:
			raise e

	@killconnections.setter
	def killconnections(self, killconnections) :
		"""Specify whether the NetScaler Gateway Plug-in should disconnect all preexisting connections, such as the connections existing before the user logged on to NetScaler Gateway, and prevent new incoming connections on the NetScaler Gateway Plug-in for Windows and MAC when the user is connected to NetScaler Gateway and split tunneling is disabled.<br/>Possible values = ON, OFF
		"""
		try :
			self._killconnections = killconnections
		except Exception as e:
			raise e

	@property
	def transparentinterception(self) :
		"""Allow access to network resources by using a single IP address and subnet mask or a range of IP addresses. The OFF setting sets the mode to proxy, in which you configure destination and source IP addresses and port numbers. If you are using the NetScaler Gateway Plug-in for Windows, set this parameter to ON, in which the mode is set to transparent. If you are using the NetScaler Gateway Plug-in for Java, set this parameter to OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._transparentinterception
		except Exception as e:
			raise e

	@transparentinterception.setter
	def transparentinterception(self, transparentinterception) :
		"""Allow access to network resources by using a single IP address and subnet mask or a range of IP addresses. The OFF setting sets the mode to proxy, in which you configure destination and source IP addresses and port numbers. If you are using the NetScaler Gateway Plug-in for Windows, set this parameter to ON, in which the mode is set to transparent. If you are using the NetScaler Gateway Plug-in for Java, set this parameter to OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._transparentinterception = transparentinterception
		except Exception as e:
			raise e

	@property
	def windowsclienttype(self) :
		"""Choose between two types of Windows Client\
		a) Application Agent - which always runs in the task bar as a standalone application and also has a supporting service which runs permanently when installed\
		b) Activex Control - ActiveX control run by Microsoft Internet Explorer.<br/>Possible values = AGENT, PLUGIN.
		"""
		try :
			return self._windowsclienttype
		except Exception as e:
			raise e

	@windowsclienttype.setter
	def windowsclienttype(self, windowsclienttype) :
		"""Choose between two types of Windows Client\
		a) Application Agent - which always runs in the task bar as a standalone application and also has a supporting service which runs permanently when installed\
		b) Activex Control - ActiveX control run by Microsoft Internet Explorer.<br/>Possible values = AGENT, PLUGIN
		"""
		try :
			self._windowsclienttype = windowsclienttype
		except Exception as e:
			raise e

	@property
	def defaultauthorizationaction(self) :
		"""Specify the network resources that users have access to when they log on to the internal network. The default setting for authorization is to deny access to all network resources. Citrix recommends using the default global setting and then creating authorization policies to define the network resources users can access. If you set the default authorization policy to DENY, you must explicitly authorize access to any network resource, which improves security.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._defaultauthorizationaction
		except Exception as e:
			raise e

	@defaultauthorizationaction.setter
	def defaultauthorizationaction(self, defaultauthorizationaction) :
		"""Specify the network resources that users have access to when they log on to the internal network. The default setting for authorization is to deny access to all network resources. Citrix recommends using the default global setting and then creating authorization policies to define the network resources users can access. If you set the default authorization policy to DENY, you must explicitly authorize access to any network resource, which improves security.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._defaultauthorizationaction = defaultauthorizationaction
		except Exception as e:
			raise e

	@property
	def authorizationgroup(self) :
		"""Comma-separated list of groups in which the user is placed when none of the groups that the user is a part of is configured on NetScaler Gateway. The authorization policy can be bound to these groups to control access to the resources.<br/>Minimum length =  1.
		"""
		try :
			return self._authorizationgroup
		except Exception as e:
			raise e

	@authorizationgroup.setter
	def authorizationgroup(self, authorizationgroup) :
		"""Comma-separated list of groups in which the user is placed when none of the groups that the user is a part of is configured on NetScaler Gateway. The authorization policy can be bound to these groups to control access to the resources.<br/>Minimum length =  1
		"""
		try :
			self._authorizationgroup = authorizationgroup
		except Exception as e:
			raise e

	@property
	def clientidletimeout(self) :
		"""Time, in minutes, after which to time out the user session if NetScaler Gateway does not detect mouse or keyboard activity.<br/>Minimum length =  1<br/>Maximum length =  9999.
		"""
		try :
			return self._clientidletimeout
		except Exception as e:
			raise e

	@clientidletimeout.setter
	def clientidletimeout(self, clientidletimeout) :
		"""Time, in minutes, after which to time out the user session if NetScaler Gateway does not detect mouse or keyboard activity.<br/>Minimum length =  1<br/>Maximum length =  9999
		"""
		try :
			self._clientidletimeout = clientidletimeout
		except Exception as e:
			raise e

	@property
	def proxy(self) :
		"""Set options to apply proxy for accessing the internal resources. Available settings function as follows:
		* BROWSER - Proxy settings are configured only in Internet Explorer and Firefox browsers.
		* NS - Proxy settings are configured on the NetScaler appliance.
		* OFF - Proxy settings are not configured.<br/>Possible values = BROWSER, NS, OFF.
		"""
		try :
			return self._proxy
		except Exception as e:
			raise e

	@proxy.setter
	def proxy(self, proxy) :
		"""Set options to apply proxy for accessing the internal resources. Available settings function as follows:
		* BROWSER - Proxy settings are configured only in Internet Explorer and Firefox browsers.
		* NS - Proxy settings are configured on the NetScaler appliance.
		* OFF - Proxy settings are not configured.<br/>Possible values = BROWSER, NS, OFF
		"""
		try :
			self._proxy = proxy
		except Exception as e:
			raise e

	@property
	def allprotocolproxy(self) :
		"""IP address of the proxy server to use for all protocols supported by NetScaler Gateway.<br/>Minimum length =  1.
		"""
		try :
			return self._allprotocolproxy
		except Exception as e:
			raise e

	@allprotocolproxy.setter
	def allprotocolproxy(self, allprotocolproxy) :
		"""IP address of the proxy server to use for all protocols supported by NetScaler Gateway.<br/>Minimum length =  1
		"""
		try :
			self._allprotocolproxy = allprotocolproxy
		except Exception as e:
			raise e

	@property
	def httpproxy(self) :
		"""IP address of the proxy server to be used for HTTP access for all subsequent connections to the internal network.<br/>Minimum length =  1.
		"""
		try :
			return self._httpproxy
		except Exception as e:
			raise e

	@httpproxy.setter
	def httpproxy(self, httpproxy) :
		"""IP address of the proxy server to be used for HTTP access for all subsequent connections to the internal network.<br/>Minimum length =  1
		"""
		try :
			self._httpproxy = httpproxy
		except Exception as e:
			raise e

	@property
	def ftpproxy(self) :
		"""IP address of the proxy server to be used for FTP access for all subsequent connections to the internal network.<br/>Minimum length =  1.
		"""
		try :
			return self._ftpproxy
		except Exception as e:
			raise e

	@ftpproxy.setter
	def ftpproxy(self, ftpproxy) :
		"""IP address of the proxy server to be used for FTP access for all subsequent connections to the internal network.<br/>Minimum length =  1
		"""
		try :
			self._ftpproxy = ftpproxy
		except Exception as e:
			raise e

	@property
	def socksproxy(self) :
		"""IP address of the proxy server to be used for SOCKS access for all subsequent connections to the internal network.<br/>Minimum length =  1.
		"""
		try :
			return self._socksproxy
		except Exception as e:
			raise e

	@socksproxy.setter
	def socksproxy(self, socksproxy) :
		"""IP address of the proxy server to be used for SOCKS access for all subsequent connections to the internal network.<br/>Minimum length =  1
		"""
		try :
			self._socksproxy = socksproxy
		except Exception as e:
			raise e

	@property
	def gopherproxy(self) :
		"""IP address of the proxy server to be used for GOPHER access for all subsequent connections to the internal network.<br/>Minimum length =  1.
		"""
		try :
			return self._gopherproxy
		except Exception as e:
			raise e

	@gopherproxy.setter
	def gopherproxy(self, gopherproxy) :
		"""IP address of the proxy server to be used for GOPHER access for all subsequent connections to the internal network.<br/>Minimum length =  1
		"""
		try :
			self._gopherproxy = gopherproxy
		except Exception as e:
			raise e

	@property
	def sslproxy(self) :
		"""IP address of the proxy server to be used for SSL access for all subsequent connections to the internal network.<br/>Minimum length =  1.
		"""
		try :
			return self._sslproxy
		except Exception as e:
			raise e

	@sslproxy.setter
	def sslproxy(self, sslproxy) :
		"""IP address of the proxy server to be used for SSL access for all subsequent connections to the internal network.<br/>Minimum length =  1
		"""
		try :
			self._sslproxy = sslproxy
		except Exception as e:
			raise e

	@property
	def proxyexception(self) :
		"""Proxy exception string that will be configured in the browser for bypassing the previously configured proxies. Allowed only if proxy type is Browser.<br/>Minimum length =  1.
		"""
		try :
			return self._proxyexception
		except Exception as e:
			raise e

	@proxyexception.setter
	def proxyexception(self, proxyexception) :
		"""Proxy exception string that will be configured in the browser for bypassing the previously configured proxies. Allowed only if proxy type is Browser.<br/>Minimum length =  1
		"""
		try :
			self._proxyexception = proxyexception
		except Exception as e:
			raise e

	@property
	def proxylocalbypass(self) :
		"""Bypass proxy server for local addresses option in Internet Explorer and Firefox proxy server settings.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._proxylocalbypass
		except Exception as e:
			raise e

	@proxylocalbypass.setter
	def proxylocalbypass(self, proxylocalbypass) :
		"""Bypass proxy server for local addresses option in Internet Explorer and Firefox proxy server settings.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._proxylocalbypass = proxylocalbypass
		except Exception as e:
			raise e

	@property
	def clientcleanupprompt(self) :
		"""Prompt for client-side cache clean-up when a client-initiated session closes.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._clientcleanupprompt
		except Exception as e:
			raise e

	@clientcleanupprompt.setter
	def clientcleanupprompt(self, clientcleanupprompt) :
		"""Prompt for client-side cache clean-up when a client-initiated session closes.<br/>Possible values = ON, OFF
		"""
		try :
			self._clientcleanupprompt = clientcleanupprompt
		except Exception as e:
			raise e

	@property
	def forcecleanup(self) :
		"""Force cache clean-up when the user closes a session. You can specify all, none, or any combination of the client-side items.<br/>Possible values = none, all, cookie, addressbar, plugin, filesystemapplication, application, applicationdata, clientcertificate, autocomplete, cache.
		"""
		try :
			return self._forcecleanup
		except Exception as e:
			raise e

	@forcecleanup.setter
	def forcecleanup(self, forcecleanup) :
		"""Force cache clean-up when the user closes a session. You can specify all, none, or any combination of the client-side items.<br/>Possible values = none, all, cookie, addressbar, plugin, filesystemapplication, application, applicationdata, clientcertificate, autocomplete, cache
		"""
		try :
			self._forcecleanup = forcecleanup
		except Exception as e:
			raise e

	@property
	def clientoptions(self) :
		"""Display only the configured menu options when you select the "Configure NetScaler Gateway" option in the NetScaler Gateway Plug-in system tray icon for Windows.<br/>Possible values = none, all, services, filetransfer, configuration.
		"""
		try :
			return self._clientoptions
		except Exception as e:
			raise e

	@clientoptions.setter
	def clientoptions(self, clientoptions) :
		"""Display only the configured menu options when you select the "Configure NetScaler Gateway" option in the NetScaler Gateway Plug-in system tray icon for Windows.<br/>Possible values = none, all, services, filetransfer, configuration
		"""
		try :
			self._clientoptions = clientoptions
		except Exception as e:
			raise e

	@property
	def clientconfiguration(self) :
		"""Display only the configured tabs when you select the "Configure NetSCaler Gateway" option in the NetScaler Gateway Plug-in system tray icon for Windows.<br/>Possible values = none, all, general, tunnel, trace, compression.
		"""
		try :
			return self._clientconfiguration
		except Exception as e:
			raise e

	@clientconfiguration.setter
	def clientconfiguration(self, clientconfiguration) :
		"""Display only the configured tabs when you select the "Configure NetSCaler Gateway" option in the NetScaler Gateway Plug-in system tray icon for Windows.<br/>Possible values = none, all, general, tunnel, trace, compression
		"""
		try :
			self._clientconfiguration = clientconfiguration
		except Exception as e:
			raise e

	@property
	def sso(self) :
		"""Set single sign-on (SSO) for the session. When the user accesses a server, the user's logon credentials are passed to the server for authentication.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sso
		except Exception as e:
			raise e

	@sso.setter
	def sso(self, sso) :
		"""Set single sign-on (SSO) for the session. When the user accesses a server, the user's logon credentials are passed to the server for authentication.<br/>Possible values = ON, OFF
		"""
		try :
			self._sso = sso
		except Exception as e:
			raise e

	@property
	def ssocredential(self) :
		"""Specify whether to use the primary or secondary authentication credentials for single sign-on to the server.<br/>Possible values = PRIMARY, SECONDARY.
		"""
		try :
			return self._ssocredential
		except Exception as e:
			raise e

	@ssocredential.setter
	def ssocredential(self, ssocredential) :
		"""Specify whether to use the primary or secondary authentication credentials for single sign-on to the server.<br/>Possible values = PRIMARY, SECONDARY
		"""
		try :
			self._ssocredential = ssocredential
		except Exception as e:
			raise e

	@property
	def windowsautologon(self) :
		"""Enable or disable the Windows Auto Logon for the session. If a VPN session is established after this setting is enabled, the user is automatically logged on by using Windows credentials after the system is restarted.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._windowsautologon
		except Exception as e:
			raise e

	@windowsautologon.setter
	def windowsautologon(self, windowsautologon) :
		"""Enable or disable the Windows Auto Logon for the session. If a VPN session is established after this setting is enabled, the user is automatically logged on by using Windows credentials after the system is restarted.<br/>Possible values = ON, OFF
		"""
		try :
			self._windowsautologon = windowsautologon
		except Exception as e:
			raise e

	@property
	def usemip(self) :
		"""Enable or disable the use of a unique IP address alias, or a mapped IP address, as the client IP address for each client session. Allow NetScaler Gateway to use the mapped IP address as an intranet IP address when all other IP addresses are not available. 
		When IP pooling is configured and the mapped IP is used as an intranet IP address, the mapped IP address is used when an intranet IP address cannot be assigned.<br/>Possible values = NS, OFF.
		"""
		try :
			return self._usemip
		except Exception as e:
			raise e

	@usemip.setter
	def usemip(self, usemip) :
		"""Enable or disable the use of a unique IP address alias, or a mapped IP address, as the client IP address for each client session. Allow NetScaler Gateway to use the mapped IP address as an intranet IP address when all other IP addresses are not available. 
		When IP pooling is configured and the mapped IP is used as an intranet IP address, the mapped IP address is used when an intranet IP address cannot be assigned.<br/>Possible values = NS, OFF
		"""
		try :
			self._usemip = usemip
		except Exception as e:
			raise e

	@property
	def useiip(self) :
		"""Define IP address pool options. Available settings function as follows: 
		* SPILLOVER - When an address pool is configured and the mapped IP is used as an intranet IP address, the mapped IP address is used when an intranet IP address cannot be assigned. 
		* NOSPILLOVER - When intranet IP addresses are enabled and the mapped IP address is not used, the Transfer Login page appears for users who have used all available intranet IP addresses. 
		* OFF - Address pool is not configured.<br/>Possible values = NOSPILLOVER, SPILLOVER, OFF.
		"""
		try :
			return self._useiip
		except Exception as e:
			raise e

	@useiip.setter
	def useiip(self, useiip) :
		"""Define IP address pool options. Available settings function as follows: 
		* SPILLOVER - When an address pool is configured and the mapped IP is used as an intranet IP address, the mapped IP address is used when an intranet IP address cannot be assigned. 
		* NOSPILLOVER - When intranet IP addresses are enabled and the mapped IP address is not used, the Transfer Login page appears for users who have used all available intranet IP addresses. 
		* OFF - Address pool is not configured.<br/>Possible values = NOSPILLOVER, SPILLOVER, OFF
		"""
		try :
			self._useiip = useiip
		except Exception as e:
			raise e

	@property
	def clientdebug(self) :
		"""Set the trace level on NetScaler Gateway. Technical support technicians use these debug logs for in-depth debugging and troubleshooting purposes. Available settings function as follows: 
		* DEBUG - Detailed debug messages are collected and written into the specified file.
		* STATS - Application audit level error messages and debug statistic counters are written into the specified file. 
		* EVENTS - Application audit-level error messages are written into the specified file. 
		* OFF - Only critical events are logged into the Windows Application Log.<br/>Possible values = debug, stats, events, OFF.
		"""
		try :
			return self._clientdebug
		except Exception as e:
			raise e

	@clientdebug.setter
	def clientdebug(self, clientdebug) :
		"""Set the trace level on NetScaler Gateway. Technical support technicians use these debug logs for in-depth debugging and troubleshooting purposes. Available settings function as follows: 
		* DEBUG - Detailed debug messages are collected and written into the specified file.
		* STATS - Application audit level error messages and debug statistic counters are written into the specified file. 
		* EVENTS - Application audit-level error messages are written into the specified file. 
		* OFF - Only critical events are logged into the Windows Application Log.<br/>Possible values = debug, stats, events, OFF
		"""
		try :
			self._clientdebug = clientdebug
		except Exception as e:
			raise e

	@property
	def loginscript(self) :
		"""Path to the logon script that is run when a session is established. Separate multiple scripts by using comma. A "$" in the path signifies that the word following the "$" is an environment variable.<br/>Minimum length =  1.
		"""
		try :
			return self._loginscript
		except Exception as e:
			raise e

	@loginscript.setter
	def loginscript(self, loginscript) :
		"""Path to the logon script that is run when a session is established. Separate multiple scripts by using comma. A "$" in the path signifies that the word following the "$" is an environment variable.<br/>Minimum length =  1
		"""
		try :
			self._loginscript = loginscript
		except Exception as e:
			raise e

	@property
	def logoutscript(self) :
		"""Path to the logout script. Separate multiple scripts by using comma. A "$" in the path signifies that the word following the "$" is an environment variable.<br/>Minimum length =  1.
		"""
		try :
			return self._logoutscript
		except Exception as e:
			raise e

	@logoutscript.setter
	def logoutscript(self, logoutscript) :
		"""Path to the logout script. Separate multiple scripts by using comma. A "$" in the path signifies that the word following the "$" is an environment variable.<br/>Minimum length =  1
		"""
		try :
			self._logoutscript = logoutscript
		except Exception as e:
			raise e

	@property
	def homepage(self) :
		"""Web address of the home page that appears when users log on. Otherwise, users receive the default home page for NetScaler Gateway, which is the Access Interface.
		"""
		try :
			return self._homepage
		except Exception as e:
			raise e

	@homepage.setter
	def homepage(self, homepage) :
		"""Web address of the home page that appears when users log on. Otherwise, users receive the default home page for NetScaler Gateway, which is the Access Interface.
		"""
		try :
			self._homepage = homepage
		except Exception as e:
			raise e

	@property
	def icaproxy(self) :
		"""Enable ICA proxy to configure secure Internet access to servers running Citrix XenApp or XenDesktop by using Citrix Receiver instead of the NetScaler Gateway Plug-in.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._icaproxy
		except Exception as e:
			raise e

	@icaproxy.setter
	def icaproxy(self, icaproxy) :
		"""Enable ICA proxy to configure secure Internet access to servers running Citrix XenApp or XenDesktop by using Citrix Receiver instead of the NetScaler Gateway Plug-in.<br/>Possible values = ON, OFF
		"""
		try :
			self._icaproxy = icaproxy
		except Exception as e:
			raise e

	@property
	def wihome(self) :
		"""Web address of the Web Interface server, such as http://<ipAddress>/Citrix/XenApp, or Receiver for Web, which enumerates the virtualized resources, such as XenApp, XenDesktop, and cloud applications. This web address is used as the home page in ICA proxy mode. 
		If Client Choices is ON, you must configure this setting. Because the user can choose between FullClient and ICAProxy, the user may see a different home page. An Internet web site may appear if the user gets the FullClient option, or a Web Interface site if the user gets the ICAProxy option. If the setting is not configured, the XenApp option does not appear as a client choice.
		"""
		try :
			return self._wihome
		except Exception as e:
			raise e

	@wihome.setter
	def wihome(self, wihome) :
		"""Web address of the Web Interface server, such as http://<ipAddress>/Citrix/XenApp, or Receiver for Web, which enumerates the virtualized resources, such as XenApp, XenDesktop, and cloud applications. This web address is used as the home page in ICA proxy mode. 
		If Client Choices is ON, you must configure this setting. Because the user can choose between FullClient and ICAProxy, the user may see a different home page. An Internet web site may appear if the user gets the FullClient option, or a Web Interface site if the user gets the ICAProxy option. If the setting is not configured, the XenApp option does not appear as a client choice.
		"""
		try :
			self._wihome = wihome
		except Exception as e:
			raise e

	@property
	def wihomeaddresstype(self) :
		"""Type of the wihome address(IPV4/V6).<br/>Possible values = IPV4, IPV6.
		"""
		try :
			return self._wihomeaddresstype
		except Exception as e:
			raise e

	@wihomeaddresstype.setter
	def wihomeaddresstype(self, wihomeaddresstype) :
		"""Type of the wihome address(IPV4/V6).<br/>Possible values = IPV4, IPV6
		"""
		try :
			self._wihomeaddresstype = wihomeaddresstype
		except Exception as e:
			raise e

	@property
	def citrixreceiverhome(self) :
		"""Web address for the Citrix Receiver home page. Configure NetScaler Gateway so that when users log on to the appliance, the NetScaler Gateway Plug-in opens a web browser that allows single sign-on to the Citrix Receiver home page.
		"""
		try :
			return self._citrixreceiverhome
		except Exception as e:
			raise e

	@citrixreceiverhome.setter
	def citrixreceiverhome(self, citrixreceiverhome) :
		"""Web address for the Citrix Receiver home page. Configure NetScaler Gateway so that when users log on to the appliance, the NetScaler Gateway Plug-in opens a web browser that allows single sign-on to the Citrix Receiver home page.
		"""
		try :
			self._citrixreceiverhome = citrixreceiverhome
		except Exception as e:
			raise e

	@property
	def wiportalmode(self) :
		"""Layout on the Access Interface. The COMPACT value indicates the use of small icons.<br/>Possible values = NORMAL, COMPACT.
		"""
		try :
			return self._wiportalmode
		except Exception as e:
			raise e

	@wiportalmode.setter
	def wiportalmode(self, wiportalmode) :
		"""Layout on the Access Interface. The COMPACT value indicates the use of small icons.<br/>Possible values = NORMAL, COMPACT
		"""
		try :
			self._wiportalmode = wiportalmode
		except Exception as e:
			raise e

	@property
	def clientchoices(self) :
		"""Provide users with multiple logon options. With client choices, users have the option of logging on by using the NetScaler Gateway Plug-in for Windows, NetScaler Gateway Plug-in for Java, the Web Interface, or clientless access from one location. Depending on how NetScaler Gateway is configured, users are presented with up to three icons for logon choices. The most common are the NetScaler Gateway Plug-in for Windows, Web Interface, and clientless access.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._clientchoices
		except Exception as e:
			raise e

	@clientchoices.setter
	def clientchoices(self, clientchoices) :
		"""Provide users with multiple logon options. With client choices, users have the option of logging on by using the NetScaler Gateway Plug-in for Windows, NetScaler Gateway Plug-in for Java, the Web Interface, or clientless access from one location. Depending on how NetScaler Gateway is configured, users are presented with up to three icons for logon choices. The most common are the NetScaler Gateway Plug-in for Windows, Web Interface, and clientless access.<br/>Possible values = ON, OFF
		"""
		try :
			self._clientchoices = clientchoices
		except Exception as e:
			raise e

	@property
	def epaclienttype(self) :
		"""Choose between two types of End point Windows Client
		a) Application Agent - which always runs in the task bar as a standalone application and also has a supporting service which runs permanently when installed
		b) Activex Control - ActiveX control run by Microsoft Internet Explorer.<br/>Possible values = AGENT, PLUGIN.
		"""
		try :
			return self._epaclienttype
		except Exception as e:
			raise e

	@epaclienttype.setter
	def epaclienttype(self, epaclienttype) :
		"""Choose between two types of End point Windows Client
		a) Application Agent - which always runs in the task bar as a standalone application and also has a supporting service which runs permanently when installed
		b) Activex Control - ActiveX control run by Microsoft Internet Explorer.<br/>Possible values = AGENT, PLUGIN
		"""
		try :
			self._epaclienttype = epaclienttype
		except Exception as e:
			raise e

	@property
	def iipdnssuffix(self) :
		"""An intranet IP DNS suffix. When a user logs on to NetScaler Gateway and is assigned an IP address, a DNS record for the user name and IP address combination is added to the NetScaler Gateway DNS cache. You can configure a DNS suffix to append to the user name when the DNS record is added to the cache. You can reach to the host from where the user is logged on by using the user's name, which can be easier to remember than an IP address. When the user logs off from NetScaler Gateway, the record is removed from the DNS cache.<br/>Minimum length =  1.
		"""
		try :
			return self._iipdnssuffix
		except Exception as e:
			raise e

	@iipdnssuffix.setter
	def iipdnssuffix(self, iipdnssuffix) :
		"""An intranet IP DNS suffix. When a user logs on to NetScaler Gateway and is assigned an IP address, a DNS record for the user name and IP address combination is added to the NetScaler Gateway DNS cache. You can configure a DNS suffix to append to the user name when the DNS record is added to the cache. You can reach to the host from where the user is logged on by using the user's name, which can be easier to remember than an IP address. When the user logs off from NetScaler Gateway, the record is removed from the DNS cache.<br/>Minimum length =  1
		"""
		try :
			self._iipdnssuffix = iipdnssuffix
		except Exception as e:
			raise e

	@property
	def forcedtimeout(self) :
		"""Force a disconnection from the NetScaler Gateway Plug-in with NetScaler Gateway after a specified number of minutes. If the session closes, the user must log on again.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._forcedtimeout
		except Exception as e:
			raise e

	@forcedtimeout.setter
	def forcedtimeout(self, forcedtimeout) :
		"""Force a disconnection from the NetScaler Gateway Plug-in with NetScaler Gateway after a specified number of minutes. If the session closes, the user must log on again.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._forcedtimeout = forcedtimeout
		except Exception as e:
			raise e

	@property
	def forcedtimeoutwarning(self) :
		"""Number of minutes to warn a user before the user session is disconnected.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._forcedtimeoutwarning
		except Exception as e:
			raise e

	@forcedtimeoutwarning.setter
	def forcedtimeoutwarning(self, forcedtimeoutwarning) :
		"""Number of minutes to warn a user before the user session is disconnected.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._forcedtimeoutwarning = forcedtimeoutwarning
		except Exception as e:
			raise e

	@property
	def ntdomain(self) :
		"""Single sign-on domain to use for single sign-on to applications in the internal network. This setting can be overwritten by the domain that users specify at the time of logon or by the domain that the authentication server returns.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._ntdomain
		except Exception as e:
			raise e

	@ntdomain.setter
	def ntdomain(self, ntdomain) :
		"""Single sign-on domain to use for single sign-on to applications in the internal network. This setting can be overwritten by the domain that users specify at the time of logon or by the domain that the authentication server returns.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._ntdomain = ntdomain
		except Exception as e:
			raise e

	@property
	def clientlessvpnmode(self) :
		"""Enable clientless access for web, XenApp or XenDesktop, and FileShare resources without installing the NetScaler Gateway Plug-in. Available settings function as follows: 
		* ON - Allow only clientless access. 
		* OFF - Allow clientless access after users log on with the NetScaler Gateway Plug-in. 
		* DISABLED - Do not allow clientless access.<br/>Possible values = ON, OFF, DISABLED.
		"""
		try :
			return self._clientlessvpnmode
		except Exception as e:
			raise e

	@clientlessvpnmode.setter
	def clientlessvpnmode(self, clientlessvpnmode) :
		"""Enable clientless access for web, XenApp or XenDesktop, and FileShare resources without installing the NetScaler Gateway Plug-in. Available settings function as follows: 
		* ON - Allow only clientless access. 
		* OFF - Allow clientless access after users log on with the NetScaler Gateway Plug-in. 
		* DISABLED - Do not allow clientless access.<br/>Possible values = ON, OFF, DISABLED
		"""
		try :
			self._clientlessvpnmode = clientlessvpnmode
		except Exception as e:
			raise e

	@property
	def emailhome(self) :
		"""Web address for the web-based email, such as Outlook Web Access.
		"""
		try :
			return self._emailhome
		except Exception as e:
			raise e

	@emailhome.setter
	def emailhome(self, emailhome) :
		"""Web address for the web-based email, such as Outlook Web Access.
		"""
		try :
			self._emailhome = emailhome
		except Exception as e:
			raise e

	@property
	def clientlessmodeurlencoding(self) :
		"""When clientless access is enabled, you can choose to encode the addresses of internal web applications or to leave the address as clear text. Available settings function as follows: 
		* OPAQUE - Use standard encoding mechanisms to make the domain and protocol part of the resource unclear to users. 
		* CLEAR - Do not encode the web address and make it visible to users. 
		* ENCRYPT - Allow the domain and protocol to be encrypted using a session key. When the web address is encrypted, the URL is different for each user session for the same web resource. If users bookmark the encoded web address, save it in the web browser and then log off, they cannot connect to the web address when they log on and use the bookmark. If users save the encrypted bookmark in the Access Interface during their session, the bookmark works each time the user logs on.<br/>Possible values = TRANSPARENT, OPAQUE, ENCRYPT.
		"""
		try :
			return self._clientlessmodeurlencoding
		except Exception as e:
			raise e

	@clientlessmodeurlencoding.setter
	def clientlessmodeurlencoding(self, clientlessmodeurlencoding) :
		"""When clientless access is enabled, you can choose to encode the addresses of internal web applications or to leave the address as clear text. Available settings function as follows: 
		* OPAQUE - Use standard encoding mechanisms to make the domain and protocol part of the resource unclear to users. 
		* CLEAR - Do not encode the web address and make it visible to users. 
		* ENCRYPT - Allow the domain and protocol to be encrypted using a session key. When the web address is encrypted, the URL is different for each user session for the same web resource. If users bookmark the encoded web address, save it in the web browser and then log off, they cannot connect to the web address when they log on and use the bookmark. If users save the encrypted bookmark in the Access Interface during their session, the bookmark works each time the user logs on.<br/>Possible values = TRANSPARENT, OPAQUE, ENCRYPT
		"""
		try :
			self._clientlessmodeurlencoding = clientlessmodeurlencoding
		except Exception as e:
			raise e

	@property
	def clientlesspersistentcookie(self) :
		"""State of persistent cookies in clientless access mode. Persistent cookies are required for accessing certain features of SharePoint, such as opening and editing Microsoft Word, Excel, and PowerPoint documents hosted on the SharePoint server. A persistent cookie remains on the user device and is sent with each HTTP request. NetScaler Gateway encrypts the persistent cookie before sending it to the plug-in on the user device, and refreshes the cookie periodically as long as the session exists. The cookie becomes stale if the session ends. Available settings function as follows: 
		* ALLOW - Enable persistent cookies. Users can open and edit Microsoft documents stored in SharePoint. 
		* DENY - Disable persistent cookies. Users cannot open and edit Microsoft documents stored in SharePoint. 
		* PROMPT - Prompt users to allow or deny persistent cookies during the session. Persistent cookies are not required for clientless access if users do not connect to SharePoint.<br/>Possible values = ALLOW, DENY, PROMPT.
		"""
		try :
			return self._clientlesspersistentcookie
		except Exception as e:
			raise e

	@clientlesspersistentcookie.setter
	def clientlesspersistentcookie(self, clientlesspersistentcookie) :
		"""State of persistent cookies in clientless access mode. Persistent cookies are required for accessing certain features of SharePoint, such as opening and editing Microsoft Word, Excel, and PowerPoint documents hosted on the SharePoint server. A persistent cookie remains on the user device and is sent with each HTTP request. NetScaler Gateway encrypts the persistent cookie before sending it to the plug-in on the user device, and refreshes the cookie periodically as long as the session exists. The cookie becomes stale if the session ends. Available settings function as follows: 
		* ALLOW - Enable persistent cookies. Users can open and edit Microsoft documents stored in SharePoint. 
		* DENY - Disable persistent cookies. Users cannot open and edit Microsoft documents stored in SharePoint. 
		* PROMPT - Prompt users to allow or deny persistent cookies during the session. Persistent cookies are not required for clientless access if users do not connect to SharePoint.<br/>Possible values = ALLOW, DENY, PROMPT
		"""
		try :
			self._clientlesspersistentcookie = clientlesspersistentcookie
		except Exception as e:
			raise e

	@property
	def allowedlogingroups(self) :
		"""Specify groups that have permission to log on to NetScaler Gateway. Users who do not belong to this group or groups are denied access even if they have valid credentials.<br/>Minimum length =  1<br/>Maximum length =  511.
		"""
		try :
			return self._allowedlogingroups
		except Exception as e:
			raise e

	@allowedlogingroups.setter
	def allowedlogingroups(self, allowedlogingroups) :
		"""Specify groups that have permission to log on to NetScaler Gateway. Users who do not belong to this group or groups are denied access even if they have valid credentials.<br/>Minimum length =  1<br/>Maximum length =  511
		"""
		try :
			self._allowedlogingroups = allowedlogingroups
		except Exception as e:
			raise e

	@property
	def securebrowse(self) :
		"""Allow users to connect through NetScaler Gateway to network resources from iOS and Android mobile devices with Citrix Receiver. Users do not need to establish a full VPN tunnel to access resources in the secure network.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securebrowse
		except Exception as e:
			raise e

	@securebrowse.setter
	def securebrowse(self, securebrowse) :
		"""Allow users to connect through NetScaler Gateway to network resources from iOS and Android mobile devices with Citrix Receiver. Users do not need to establish a full VPN tunnel to access resources in the secure network.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securebrowse = securebrowse
		except Exception as e:
			raise e

	@property
	def storefronturl(self) :
		"""Web address for StoreFront to be used in this session for enumeration of resources from XenApp or XenDesktop.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._storefronturl
		except Exception as e:
			raise e

	@storefronturl.setter
	def storefronturl(self, storefronturl) :
		"""Web address for StoreFront to be used in this session for enumeration of resources from XenApp or XenDesktop.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._storefronturl = storefronturl
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		"""The kcd account details to be used in SSO.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		"""The kcd account details to be used in SSO.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def clientidletimeoutwarning(self) :
		"""The time after which the client gets a timeout warning, in minutes.
		"""
		try :
			return self._clientidletimeoutwarning
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnsessionaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnsessionaction
		except Exception as e :
			raise e

	def _get_object_name(self) :
		""" Returns the value of object identifier argument
		"""
		try :
			if (self.name) :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def add(cls, client, resource) :
		""" Use this API to add vpnsessionaction.
		"""
		try :
			if type(resource) is not list :
				addresource = vpnsessionaction()
				addresource.name = resource.name
				addresource.useraccounting = resource.useraccounting
				addresource.httpport = resource.httpport
				addresource.winsip = resource.winsip
				addresource.dnsvservername = resource.dnsvservername
				addresource.splitdns = resource.splitdns
				addresource.sesstimeout = resource.sesstimeout
				addresource.clientsecurity = resource.clientsecurity
				addresource.clientsecuritygroup = resource.clientsecuritygroup
				addresource.clientsecuritymessage = resource.clientsecuritymessage
				addresource.clientsecuritylog = resource.clientsecuritylog
				addresource.splittunnel = resource.splittunnel
				addresource.locallanaccess = resource.locallanaccess
				addresource.rfc1918 = resource.rfc1918
				addresource.spoofiip = resource.spoofiip
				addresource.killconnections = resource.killconnections
				addresource.transparentinterception = resource.transparentinterception
				addresource.windowsclienttype = resource.windowsclienttype
				addresource.defaultauthorizationaction = resource.defaultauthorizationaction
				addresource.authorizationgroup = resource.authorizationgroup
				addresource.clientidletimeout = resource.clientidletimeout
				addresource.proxy = resource.proxy
				addresource.allprotocolproxy = resource.allprotocolproxy
				addresource.httpproxy = resource.httpproxy
				addresource.ftpproxy = resource.ftpproxy
				addresource.socksproxy = resource.socksproxy
				addresource.gopherproxy = resource.gopherproxy
				addresource.sslproxy = resource.sslproxy
				addresource.proxyexception = resource.proxyexception
				addresource.proxylocalbypass = resource.proxylocalbypass
				addresource.clientcleanupprompt = resource.clientcleanupprompt
				addresource.forcecleanup = resource.forcecleanup
				addresource.clientoptions = resource.clientoptions
				addresource.clientconfiguration = resource.clientconfiguration
				addresource.sso = resource.sso
				addresource.ssocredential = resource.ssocredential
				addresource.windowsautologon = resource.windowsautologon
				addresource.usemip = resource.usemip
				addresource.useiip = resource.useiip
				addresource.clientdebug = resource.clientdebug
				addresource.loginscript = resource.loginscript
				addresource.logoutscript = resource.logoutscript
				addresource.homepage = resource.homepage
				addresource.icaproxy = resource.icaproxy
				addresource.wihome = resource.wihome
				addresource.wihomeaddresstype = resource.wihomeaddresstype
				addresource.citrixreceiverhome = resource.citrixreceiverhome
				addresource.wiportalmode = resource.wiportalmode
				addresource.clientchoices = resource.clientchoices
				addresource.epaclienttype = resource.epaclienttype
				addresource.iipdnssuffix = resource.iipdnssuffix
				addresource.forcedtimeout = resource.forcedtimeout
				addresource.forcedtimeoutwarning = resource.forcedtimeoutwarning
				addresource.ntdomain = resource.ntdomain
				addresource.clientlessvpnmode = resource.clientlessvpnmode
				addresource.emailhome = resource.emailhome
				addresource.clientlessmodeurlencoding = resource.clientlessmodeurlencoding
				addresource.clientlesspersistentcookie = resource.clientlesspersistentcookie
				addresource.allowedlogingroups = resource.allowedlogingroups
				addresource.securebrowse = resource.securebrowse
				addresource.storefronturl = resource.storefronturl
				addresource.kcdaccount = resource.kcdaccount
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnsessionaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i].name = resource[i].name
						addresources[i].useraccounting = resource[i].useraccounting
						addresources[i].httpport = resource[i].httpport
						addresources[i].winsip = resource[i].winsip
						addresources[i].dnsvservername = resource[i].dnsvservername
						addresources[i].splitdns = resource[i].splitdns
						addresources[i].sesstimeout = resource[i].sesstimeout
						addresources[i].clientsecurity = resource[i].clientsecurity
						addresources[i].clientsecuritygroup = resource[i].clientsecuritygroup
						addresources[i].clientsecuritymessage = resource[i].clientsecuritymessage
						addresources[i].clientsecuritylog = resource[i].clientsecuritylog
						addresources[i].splittunnel = resource[i].splittunnel
						addresources[i].locallanaccess = resource[i].locallanaccess
						addresources[i].rfc1918 = resource[i].rfc1918
						addresources[i].spoofiip = resource[i].spoofiip
						addresources[i].killconnections = resource[i].killconnections
						addresources[i].transparentinterception = resource[i].transparentinterception
						addresources[i].windowsclienttype = resource[i].windowsclienttype
						addresources[i].defaultauthorizationaction = resource[i].defaultauthorizationaction
						addresources[i].authorizationgroup = resource[i].authorizationgroup
						addresources[i].clientidletimeout = resource[i].clientidletimeout
						addresources[i].proxy = resource[i].proxy
						addresources[i].allprotocolproxy = resource[i].allprotocolproxy
						addresources[i].httpproxy = resource[i].httpproxy
						addresources[i].ftpproxy = resource[i].ftpproxy
						addresources[i].socksproxy = resource[i].socksproxy
						addresources[i].gopherproxy = resource[i].gopherproxy
						addresources[i].sslproxy = resource[i].sslproxy
						addresources[i].proxyexception = resource[i].proxyexception
						addresources[i].proxylocalbypass = resource[i].proxylocalbypass
						addresources[i].clientcleanupprompt = resource[i].clientcleanupprompt
						addresources[i].forcecleanup = resource[i].forcecleanup
						addresources[i].clientoptions = resource[i].clientoptions
						addresources[i].clientconfiguration = resource[i].clientconfiguration
						addresources[i].sso = resource[i].sso
						addresources[i].ssocredential = resource[i].ssocredential
						addresources[i].windowsautologon = resource[i].windowsautologon
						addresources[i].usemip = resource[i].usemip
						addresources[i].useiip = resource[i].useiip
						addresources[i].clientdebug = resource[i].clientdebug
						addresources[i].loginscript = resource[i].loginscript
						addresources[i].logoutscript = resource[i].logoutscript
						addresources[i].homepage = resource[i].homepage
						addresources[i].icaproxy = resource[i].icaproxy
						addresources[i].wihome = resource[i].wihome
						addresources[i].wihomeaddresstype = resource[i].wihomeaddresstype
						addresources[i].citrixreceiverhome = resource[i].citrixreceiverhome
						addresources[i].wiportalmode = resource[i].wiportalmode
						addresources[i].clientchoices = resource[i].clientchoices
						addresources[i].epaclienttype = resource[i].epaclienttype
						addresources[i].iipdnssuffix = resource[i].iipdnssuffix
						addresources[i].forcedtimeout = resource[i].forcedtimeout
						addresources[i].forcedtimeoutwarning = resource[i].forcedtimeoutwarning
						addresources[i].ntdomain = resource[i].ntdomain
						addresources[i].clientlessvpnmode = resource[i].clientlessvpnmode
						addresources[i].emailhome = resource[i].emailhome
						addresources[i].clientlessmodeurlencoding = resource[i].clientlessmodeurlencoding
						addresources[i].clientlesspersistentcookie = resource[i].clientlesspersistentcookie
						addresources[i].allowedlogingroups = resource[i].allowedlogingroups
						addresources[i].securebrowse = resource[i].securebrowse
						addresources[i].storefronturl = resource[i].storefronturl
						addresources[i].kcdaccount = resource[i].kcdaccount
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def delete(cls, client, resource) :
		""" Use this API to delete vpnsessionaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnsessionaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource.name = resource.name
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i].name
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def update(cls, client, resource) :
		""" Use this API to update vpnsessionaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = vpnsessionaction()
				updateresource.name = resource.name
				updateresource.useraccounting = resource.useraccounting
				updateresource.httpport = resource.httpport
				updateresource.winsip = resource.winsip
				updateresource.dnsvservername = resource.dnsvservername
				updateresource.splitdns = resource.splitdns
				updateresource.sesstimeout = resource.sesstimeout
				updateresource.clientsecurity = resource.clientsecurity
				updateresource.clientsecuritygroup = resource.clientsecuritygroup
				updateresource.clientsecuritymessage = resource.clientsecuritymessage
				updateresource.clientsecuritylog = resource.clientsecuritylog
				updateresource.splittunnel = resource.splittunnel
				updateresource.locallanaccess = resource.locallanaccess
				updateresource.rfc1918 = resource.rfc1918
				updateresource.spoofiip = resource.spoofiip
				updateresource.killconnections = resource.killconnections
				updateresource.transparentinterception = resource.transparentinterception
				updateresource.windowsclienttype = resource.windowsclienttype
				updateresource.defaultauthorizationaction = resource.defaultauthorizationaction
				updateresource.authorizationgroup = resource.authorizationgroup
				updateresource.clientidletimeout = resource.clientidletimeout
				updateresource.proxy = resource.proxy
				updateresource.allprotocolproxy = resource.allprotocolproxy
				updateresource.httpproxy = resource.httpproxy
				updateresource.ftpproxy = resource.ftpproxy
				updateresource.socksproxy = resource.socksproxy
				updateresource.gopherproxy = resource.gopherproxy
				updateresource.sslproxy = resource.sslproxy
				updateresource.proxyexception = resource.proxyexception
				updateresource.proxylocalbypass = resource.proxylocalbypass
				updateresource.clientcleanupprompt = resource.clientcleanupprompt
				updateresource.forcecleanup = resource.forcecleanup
				updateresource.clientoptions = resource.clientoptions
				updateresource.clientconfiguration = resource.clientconfiguration
				updateresource.sso = resource.sso
				updateresource.ssocredential = resource.ssocredential
				updateresource.windowsautologon = resource.windowsautologon
				updateresource.usemip = resource.usemip
				updateresource.useiip = resource.useiip
				updateresource.clientdebug = resource.clientdebug
				updateresource.loginscript = resource.loginscript
				updateresource.logoutscript = resource.logoutscript
				updateresource.homepage = resource.homepage
				updateresource.icaproxy = resource.icaproxy
				updateresource.wihome = resource.wihome
				updateresource.wihomeaddresstype = resource.wihomeaddresstype
				updateresource.citrixreceiverhome = resource.citrixreceiverhome
				updateresource.wiportalmode = resource.wiportalmode
				updateresource.clientchoices = resource.clientchoices
				updateresource.epaclienttype = resource.epaclienttype
				updateresource.iipdnssuffix = resource.iipdnssuffix
				updateresource.forcedtimeout = resource.forcedtimeout
				updateresource.forcedtimeoutwarning = resource.forcedtimeoutwarning
				updateresource.ntdomain = resource.ntdomain
				updateresource.clientlessvpnmode = resource.clientlessvpnmode
				updateresource.emailhome = resource.emailhome
				updateresource.clientlessmodeurlencoding = resource.clientlessmodeurlencoding
				updateresource.clientlesspersistentcookie = resource.clientlesspersistentcookie
				updateresource.allowedlogingroups = resource.allowedlogingroups
				updateresource.securebrowse = resource.securebrowse
				updateresource.storefronturl = resource.storefronturl
				updateresource.kcdaccount = resource.kcdaccount
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnsessionaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i].name = resource[i].name
						updateresources[i].useraccounting = resource[i].useraccounting
						updateresources[i].httpport = resource[i].httpport
						updateresources[i].winsip = resource[i].winsip
						updateresources[i].dnsvservername = resource[i].dnsvservername
						updateresources[i].splitdns = resource[i].splitdns
						updateresources[i].sesstimeout = resource[i].sesstimeout
						updateresources[i].clientsecurity = resource[i].clientsecurity
						updateresources[i].clientsecuritygroup = resource[i].clientsecuritygroup
						updateresources[i].clientsecuritymessage = resource[i].clientsecuritymessage
						updateresources[i].clientsecuritylog = resource[i].clientsecuritylog
						updateresources[i].splittunnel = resource[i].splittunnel
						updateresources[i].locallanaccess = resource[i].locallanaccess
						updateresources[i].rfc1918 = resource[i].rfc1918
						updateresources[i].spoofiip = resource[i].spoofiip
						updateresources[i].killconnections = resource[i].killconnections
						updateresources[i].transparentinterception = resource[i].transparentinterception
						updateresources[i].windowsclienttype = resource[i].windowsclienttype
						updateresources[i].defaultauthorizationaction = resource[i].defaultauthorizationaction
						updateresources[i].authorizationgroup = resource[i].authorizationgroup
						updateresources[i].clientidletimeout = resource[i].clientidletimeout
						updateresources[i].proxy = resource[i].proxy
						updateresources[i].allprotocolproxy = resource[i].allprotocolproxy
						updateresources[i].httpproxy = resource[i].httpproxy
						updateresources[i].ftpproxy = resource[i].ftpproxy
						updateresources[i].socksproxy = resource[i].socksproxy
						updateresources[i].gopherproxy = resource[i].gopherproxy
						updateresources[i].sslproxy = resource[i].sslproxy
						updateresources[i].proxyexception = resource[i].proxyexception
						updateresources[i].proxylocalbypass = resource[i].proxylocalbypass
						updateresources[i].clientcleanupprompt = resource[i].clientcleanupprompt
						updateresources[i].forcecleanup = resource[i].forcecleanup
						updateresources[i].clientoptions = resource[i].clientoptions
						updateresources[i].clientconfiguration = resource[i].clientconfiguration
						updateresources[i].sso = resource[i].sso
						updateresources[i].ssocredential = resource[i].ssocredential
						updateresources[i].windowsautologon = resource[i].windowsautologon
						updateresources[i].usemip = resource[i].usemip
						updateresources[i].useiip = resource[i].useiip
						updateresources[i].clientdebug = resource[i].clientdebug
						updateresources[i].loginscript = resource[i].loginscript
						updateresources[i].logoutscript = resource[i].logoutscript
						updateresources[i].homepage = resource[i].homepage
						updateresources[i].icaproxy = resource[i].icaproxy
						updateresources[i].wihome = resource[i].wihome
						updateresources[i].wihomeaddresstype = resource[i].wihomeaddresstype
						updateresources[i].citrixreceiverhome = resource[i].citrixreceiverhome
						updateresources[i].wiportalmode = resource[i].wiportalmode
						updateresources[i].clientchoices = resource[i].clientchoices
						updateresources[i].epaclienttype = resource[i].epaclienttype
						updateresources[i].iipdnssuffix = resource[i].iipdnssuffix
						updateresources[i].forcedtimeout = resource[i].forcedtimeout
						updateresources[i].forcedtimeoutwarning = resource[i].forcedtimeoutwarning
						updateresources[i].ntdomain = resource[i].ntdomain
						updateresources[i].clientlessvpnmode = resource[i].clientlessvpnmode
						updateresources[i].emailhome = resource[i].emailhome
						updateresources[i].clientlessmodeurlencoding = resource[i].clientlessmodeurlencoding
						updateresources[i].clientlesspersistentcookie = resource[i].clientlesspersistentcookie
						updateresources[i].allowedlogingroups = resource[i].allowedlogingroups
						updateresources[i].securebrowse = resource[i].securebrowse
						updateresources[i].storefronturl = resource[i].storefronturl
						updateresources[i].kcdaccount = resource[i].kcdaccount
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		""" Use this API to unset the properties of vpnsessionaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnsessionaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnsessionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		""" Use this API to fetch all the vpnsessionaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnsessionaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) != cls :
					if type(name) is not list :
						obj = vpnsessionaction()
						obj.name = name
						response = obj.get_resource(client, option_)
					else :
						if name and len(name) > 0 :
							response = [vpnsessionaction() for _ in range(len(name))]
							obj = [vpnsessionaction() for _ in range(len(name))]
							for i in range(len(name)) :
								obj[i] = vpnsessionaction()
								obj[i].name = name[i]
								response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		""" Use this API to fetch filtered set of vpnsessionaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnsessionaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		""" Use this API to count the vpnsessionaction resources configured on NetScaler.
		"""
		try :
			obj = vpnsessionaction()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		""" Use this API to count filtered the set of vpnsessionaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnsessionaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Spoofiip:
		ON = "ON"
		OFF = "OFF"

	class Transparentinterception:
		ON = "ON"
		OFF = "OFF"

	class Wihomeaddresstype:
		IPV4 = "IPV4"
		IPV6 = "IPV6"

	class Clientcleanupprompt:
		ON = "ON"
		OFF = "OFF"

	class Icaproxy:
		ON = "ON"
		OFF = "OFF"

	class Clientlessvpnmode:
		ON = "ON"
		OFF = "OFF"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Splitdns:
		LOCAL = "LOCAL"
		REMOTE = "REMOTE"
		BOTH = "BOTH"

	class Usemip:
		NS = "NS"
		OFF = "OFF"

	class Windowsclienttype:
		AGENT = "AGENT"
		PLUGIN = "PLUGIN"

	class Epaclienttype:
		AGENT = "AGENT"
		PLUGIN = "PLUGIN"

	class Clientlesspersistentcookie:
		ALLOW = "ALLOW"
		DENY = "DENY"
		PROMPT = "PROMPT"

	class Locallanaccess:
		ON = "ON"
		OFF = "OFF"

	class Proxy:
		BROWSER = "BROWSER"
		NS = "NS"
		OFF = "OFF"

	class Wiportalmode:
		NORMAL = "NORMAL"
		COMPACT = "COMPACT"

	class Clientlessmodeurlencoding:
		TRANSPARENT = "TRANSPARENT"
		OPAQUE = "OPAQUE"
		ENCRYPT = "ENCRYPT"

	class Forcecleanup:
		none = "none"
		all = "all"
		cookie = "cookie"
		addressbar = "addressbar"
		plugin = "plugin"
		filesystemapplication = "filesystemapplication"
		application = "application"
		applicationdata = "applicationdata"
		clientcertificate = "clientcertificate"
		autocomplete = "autocomplete"
		cache = "cache"

	class Clientsecuritylog:
		ON = "ON"
		OFF = "OFF"

	class Killconnections:
		ON = "ON"
		OFF = "OFF"

	class Useiip:
		NOSPILLOVER = "NOSPILLOVER"
		SPILLOVER = "SPILLOVER"
		OFF = "OFF"

	class Securebrowse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Defaultauthorizationaction:
		ALLOW = "ALLOW"
		DENY = "DENY"

	class Windowsautologon:
		ON = "ON"
		OFF = "OFF"

	class Clientoptions:
		none = "none"
		all = "all"
		services = "services"
		filetransfer = "filetransfer"
		configuration = "configuration"

	class Splittunnel:
		ON = "ON"
		OFF = "OFF"
		REVERSE = "REVERSE"

	class Clientchoices:
		ON = "ON"
		OFF = "OFF"

	class Proxylocalbypass:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rfc1918:
		ON = "ON"
		OFF = "OFF"

	class Ssocredential:
		PRIMARY = "PRIMARY"
		SECONDARY = "SECONDARY"

	class Clientconfiguration:
		none = "none"
		all = "all"
		general = "general"
		tunnel = "tunnel"
		trace = "trace"
		compression = "compression"

	class Clientdebug:
		debug = "debug"
		stats = "stats"
		events = "events"
		OFF = "OFF"

	class Sso:
		ON = "ON"
		OFF = "OFF"

class vpnsessionaction_response(base_response) :
	def __init__(self, length=1) :
		self.vpnsessionaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnsessionaction = [vpnsessionaction() for _ in range(length)]

