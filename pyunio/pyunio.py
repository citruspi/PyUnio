##############################################
# Name        : pyunio
# Author      : Mihir Singh (@citruspi)
# Version     : 0.1.1
# License     : MIT
# Description : Basic Python implementation
#			    of @ttezel's Node.js unio.
##############################################

try:

	import os
	import json
	import requests
	from inspect import stack
	from pprint import pprint
	from requests_oauthlib import OAuth1
	
except ImportError as e:
	
	print e	

class PyUnio(object):
	
	def __init__(self):
		
		self.specs = dict	
				
	def use(self, service):
				
		try:
	
			with open(os.getcwd()+'/specs/'+service+'.json') as service_definition: self.specs = json.load(service_definition)
													
		except Exception as e:
			
			return (None, "Exception: %s" % (e))	
			
	def get(self, route, params):

		try:		
	
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('consumer_key' or 'consumer_secret' or 'access_token' or 'access_token_secret') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth), None)																
					
				else:
					
					return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params), None)
	
			else:
	
				return (None, "The '%s' method is not defined for the '%s' resource." % (stack()[0][3], route))		
	
		except KeyError as e:
	
			return (None, "Exception: %s" % (e))													
				
	def post(self, route, params):
		
		try:		
		
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('consumer_key' or 'consumer_secret' or 'access_token' or 'access_token_secret') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth), None)																
					
				else:
					
					return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params), None)
		
			else:
		
				return (None, "The '%s' method is not defined for the '%s' resource." % (stack()[0][3], route))		
		
		except KeyError as e:
		
			return (None, "Exception: %s" % (e))		
		
	def put(self, route, params):
		
		try:		
		
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('consumer_key' or 'consumer_secret' or 'access_token' or 'access_token_secret') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth), None)																
					
				else:
					
					return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params), None)
		
			else:
		
				return (None, "The '%s' method is not defined for the '%s' resource." % (stack()[0][3], route))		
		
		except KeyError as e:
		
			return (None, "Exception: %s" % (e))		
		
	def delete(self, route, params):
		
		try:		
		
			if stack()[0][3] in self.specs['resources'][route]['methods']:
				
				if ('consumer_key' or 'consumer_secret' or 'access_token' or 'access_token_secret') in params:
					
						oauth, params = self.oauth_handle(params)
															   
						return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
																 params=params,
												 				 auth=oauth), None)																
					
				else:
					
					return (getattr(requests, stack()[0][3])(self.specs['api_root']+'/'+self.specs['resources'][route]['path'],
														 params=params), None)
		
			else:
		
				return (None, "The '%s' method is not defined for the '%s' resource." % (stack()[0][3], route))		
		
		except KeyError as e:
		
			return (None, "Exception: %s" % (e))	
			
	def oauth_handle(self, params):
		
		try:
	
			oauth = OAuth1(params['consumer_key'], 
								   params['consumer_secret'],
								   params['access_token'], 
								   params['access_token_secret'],
								   signature_type='auth_header')
								   
			del params['consumer_key']
			del params['consumer_secret']
			del params['access_token']
			del params['access_token_secret']	
					
			return (oauth, params)
			
		except Exception as e:
			
			print "Exception %s " % (e) 
			quit()
												
pyunio = PyUnio()