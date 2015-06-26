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

class sslcrl_binding(base_resource):
	""" Binding class showing the resources that can be bound to sslcrl_binding. 
	"""
	def __init__(self) :
		self._crlname = ""
		self.sslcrl_serialnumber_binding = []

	@property
	def crlname(self) :
		"""Name of the CRL for which to show detailed information.<br/>Minimum length =  1.
		"""
		try :
			return self._crlname
		except Exception as e:
			raise e

	@crlname.setter
	def crlname(self, crlname) :
		"""Name of the CRL for which to show detailed information.<br/>Minimum length =  1
		"""
		try :
			self._crlname = crlname
		except Exception as e:
			raise e

	@property
	def sslcrl_serialnumber_bindings(self) :
		"""serialnumber that can be bound to sslcrl.
		"""
		try :
			return self._sslcrl_serialnumber_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcrl_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcrl_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		""" Returns the value of object identifier argument
		"""
		try :
			if (self.crlname) :
				return str(self.crlname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, crlname) :
		""" Use this API to fetch sslcrl_binding resource.
		"""
		try :
			if type(crlname) is not list :
				obj = sslcrl_binding()
				obj.crlname = crlname
				response = obj.get_resource(service)
			else :
				if crlname and len(crlname) > 0 :
					obj = [sslcrl_binding() for _ in range(len(crlname))]
					for i in range(len(crlname)) :
						obj[i].crlname = crlname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class sslcrl_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcrl_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcrl_binding = [sslcrl_binding() for _ in range(length)]

