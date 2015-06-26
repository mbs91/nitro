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

class snmp_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._snmptotrxpkts = 0
		self._snmprxpktsrate = 0
		self._snmptottxpkts = 0
		self._snmptxpktsrate = 0
		self._snmptotgetreqs = 0
		self._snmpgetreqsrate = 0
		self._snmptotgetnextreqs = 0
		self._snmpgetnextreqsrate = 0
		self._snmptotgetbulkreqs = 0
		self._snmpgetbulkreqsrate = 0
		self._snmptotresponses = 0
		self._snmpresponsesrate = 0
		self._snmptottraps = 0
		self._snmptoterrreqdropped = 0
		self._snmptotparseerrs = 0
		self._snmptotbadversions = 0
		self._snmptotbadcommname = 0
		self._snmptotbadcommuse = 0
		self._snmpunsupportedsecuritylevel = 0
		self._snmpnotintimewindow = 0
		self._snmpunknownusername = 0
		self._snmpunknownengineids = 0
		self._snmpwrongdigests = 0
		self._snmpdecryptionerrors = 0

	@property
	def clearstats(self) :
		"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def snmpdecryptionerrors(self) :
		"""SNMP packets that were dropped because they could not be decrypted.
		"""
		try :
			return self._snmpdecryptionerrors
		except Exception as e:
			raise e

	@property
	def snmptotresponses(self) :
		"""SNMP Get-Response PDUs that have been generated by the NetScaler.
		"""
		try :
			return self._snmptotresponses
		except Exception as e:
			raise e

	@property
	def snmptotbadcommuse(self) :
		"""The total number of SNMP Messages received that represented an SNMP operation which was not allowed by the SNMP community named in the Message.
		"""
		try :
			return self._snmptotbadcommuse
		except Exception as e:
			raise e

	@property
	def snmptoterrreqdropped(self) :
		"""SNMP requests dropped.
		"""
		try :
			return self._snmptoterrreqdropped
		except Exception as e:
			raise e

	@property
	def snmpgetnextreqsrate(self) :
		"""Rate (/s) counter for snmptotgetnextreqs.
		"""
		try :
			return self._snmpgetnextreqsrate
		except Exception as e:
			raise e

	@property
	def snmptotbadversions(self) :
		"""Number of SNMP messages received, which were for an unsupported SNMP version.
		"""
		try :
			return self._snmptotbadversions
		except Exception as e:
			raise e

	@property
	def snmptotrxpkts(self) :
		"""SNMP packets received.
		"""
		try :
			return self._snmptotrxpkts
		except Exception as e:
			raise e

	@property
	def snmptxpktsrate(self) :
		"""Rate (/s) counter for snmptottxpkts.
		"""
		try :
			return self._snmptxpktsrate
		except Exception as e:
			raise e

	@property
	def snmpresponsesrate(self) :
		"""Rate (/s) counter for snmptotresponses.
		"""
		try :
			return self._snmpresponsesrate
		except Exception as e:
			raise e

	@property
	def snmpgetreqsrate(self) :
		"""Rate (/s) counter for snmptotgetreqs.
		"""
		try :
			return self._snmpgetreqsrate
		except Exception as e:
			raise e

	@property
	def snmptotbadcommname(self) :
		"""SNMP messages received, which used an SNMP community name not known to the NetScaler.
		"""
		try :
			return self._snmptotbadcommname
		except Exception as e:
			raise e

	@property
	def snmptotgetnextreqs(self) :
		"""SNMP Get-Next PDUs that have been accepted and processed.
		"""
		try :
			return self._snmptotgetnextreqs
		except Exception as e:
			raise e

	@property
	def snmptottxpkts(self) :
		"""SNMP packets transmitted.
		"""
		try :
			return self._snmptottxpkts
		except Exception as e:
			raise e

	@property
	def snmpunknownengineids(self) :
		"""SNMP packets that were dropped because they referenced an SNMP engine ID that was not known to the NetScaler.
		"""
		try :
			return self._snmpunknownengineids
		except Exception as e:
			raise e

	@property
	def snmpwrongdigests(self) :
		"""SNMP packets that were dropped because they did not contain the expected digest value.
		"""
		try :
			return self._snmpwrongdigests
		except Exception as e:
			raise e

	@property
	def snmpgetbulkreqsrate(self) :
		"""Rate (/s) counter for snmptotgetbulkreqs.
		"""
		try :
			return self._snmpgetbulkreqsrate
		except Exception as e:
			raise e

	@property
	def snmpnotintimewindow(self) :
		"""SNMP packets that were dropped because they appeared outside of the authoritative SNMP engine's window.
		"""
		try :
			return self._snmpnotintimewindow
		except Exception as e:
			raise e

	@property
	def snmptotgetbulkreqs(self) :
		"""SNMP Get-Bulk PDUs that have been accepted and proZcessed.
		"""
		try :
			return self._snmptotgetbulkreqs
		except Exception as e:
			raise e

	@property
	def snmptotparseerrs(self) :
		"""Number of ASN.1 or BER errors encountered when decoding received SNMP Messages.
		"""
		try :
			return self._snmptotparseerrs
		except Exception as e:
			raise e

	@property
	def snmpunknownusername(self) :
		"""SNMP packets that were dropped because they referenced a user that was  not  known to the SNMP engine.
		"""
		try :
			return self._snmpunknownusername
		except Exception as e:
			raise e

	@property
	def snmpunsupportedsecuritylevel(self) :
		"""SNMP packets that were dropped because they requested a security level that was
		unknown to the NetScaler or otherwise unavailable.
		"""
		try :
			return self._snmpunsupportedsecuritylevel
		except Exception as e:
			raise e

	@property
	def snmptotgetreqs(self) :
		"""SNMP Get-Request PDUs that have been accepted and processed.
		"""
		try :
			return self._snmptotgetreqs
		except Exception as e:
			raise e

	@property
	def snmprxpktsrate(self) :
		"""Rate (/s) counter for snmptotrxpkts.
		"""
		try :
			return self._snmprxpktsrate
		except Exception as e:
			raise e

	@property
	def snmptottraps(self) :
		"""SNMP Trap PDUs that have been generated by the NetScaler.
		"""
		try :
			return self._snmptottraps
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmp
		except Exception as e :
			raise e

	def _get_object_name(self) :
		""" Returns the value of object identifier argument
		"""
		try :
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		""" Use this API to fetch the statistics of all snmp_stats resources that are configured on netscaler.
		"""
		try :
			obj = snmp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class snmp_response(base_response) :
	def __init__(self, length=1) :
		self.snmp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmp = [snmp_stats() for _ in range(length)]

