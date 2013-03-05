##############################################
# Name        : PyUnio
# Author      : Mihir Singh (@citruspi)
# Version     : 0.1.3
# License     : MIT
# Description : Basic Python implementation
#			    of @ttezel's Node.js unio.
##############################################

try:

	import os
	import json
	import requests
	from inspect import stack
	from requests_oauthlib import OAuth1
	
except ImportError as e:
	
	raise Exception(e)

class PyUnio(object):
	
	def __init__(self, cwd):
		
		self.specs = dict	
		self.cwd   = cwd 
				
	def use(self, service):
				
		try:
	
			with open(self.cwd+'/specs/'+service+'.json') as service_definition: self.specs = json.load(service_definition)
													
		except Exception as e:
			
			raise Exception(e)
			
	def get(self, route, params):

		try:		
	
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('oauth') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth)														
					
				else:
					
					return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params)
	
			else:
	
				raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (stack()[0][3], route)	
	
		except KeyError as e:
	
			raise Exception(e)												
				
	def post(self, route, params):
		
		try:		
		
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('oauth') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth)															
					
				else:
					
					return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params)
		
			else:
		
				raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (stack()[0][3], route)	
		
		except KeyError as e:
		
			raise Exception(e)	
		
	def put(self, route, params):
		
		try:		
		
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('oauth') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth)														
					
				else:
					
					return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params)
		
			else:
		
				raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (stack()[0][3], route)	
		
		except KeyError as e:
		
			raise Exception(e)		
		
	def delete(self, route, params):
		
		try:		
		
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('oauth') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth)															
					
				else:
					
					return getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params)
		
			else:
		
				raise Exception("The HTTP verb '%s' is not defined for '%s'.") % (stack()[0][3], route)	
		
		except KeyError as e:
		
			raise Exception(e)			
			
	def oauth_handle(self, params):
		
		try:
	
			oauth = OAuth1(params['ouath']['consumer_key'],       		
    					   params['ouath']['consumer_secret'],
                           params['ouath']['access_token'], 
                           params['ouath']['access_token_secret'],
                           signature_type='auth_header')
								   
			del params['ouath']
					
			return (oauth, params)
			
		except Exception as e:
			
			raise Exception(e)											