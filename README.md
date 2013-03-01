## PyUnio, API Consumption in a Snap

__PyUnio is currently in alpha and should not be considered stable.__

### Introducion

`PyUnio` is an implementation of Tolga Tezel's Node.js project [unio](https://github.com/ttezel/unio). 
 
It allows developers to consume REST API's in as little as three lines of code by predefining aspects of an API in a `JSON` file. These API definitions are called `specs` and should be placed in a directory titled `specs`.

Any `specs` should be downloaded from [here](https://github.com/ttezel/unio/tree/master/specs) or you can write your own.

### Warning

`PyUnio`'s development may not always run parallel to that of `unio`. 

`PyUnio` may implement features not available in `unio`, or it may not implement features available in `unio`.

For this reason, you should __read this entire page__ for any important changes in future versions.

### Install

Either

	$ git clone git://github.com/citruspi/PyUnio.git
	$ cd PyUnio && python setup.py
	$ pip install -r requirements.txt
    
or

	$ pip install pyunio
	
### Directory Structure

	project/
		script.py
		specs/
			service.json
			service.json
			service.json
			service.json
			etc
	
### Usage

#### OAuth

`PyUnio` supports `OAuth` via the `requests_oauthlib` module.

To use `OAuth` in a call, just include

* `consumer_secret`
* `consumer_key`
* `access_token`
* `access_token_secret`

in the `params` `dict`.

#### Example: Twitter - Get User Settings

The following code is an implementation of Twitter's API with PyUnio:

	import os
	from pyunio import pyunio
	
	pyunio = pyunio.PyUnio(os.getcwd())
	
	params = {
				'consumer_secret'    : 'ITS A SECRET',
				'consumer_key'       : 'ITS A SECRET',
				'access_token'       : 'ITS A SECRET',
				'access_token_secret': 'ITS A SECRET'
			 }
	
	pyunio.use('twitter')
	
	try:
	
		result = pyunio.get('account/settings', params)
	
		print result.text
		
	except Exception as e:
	
		raise Exception(e)

The output of `result.text` (with my Twitter account) is:

	{
		"protected":false,
		"geo_enabled":false,
		"screen_name":"citrus",
		"language":"en",
		"time_zone":{
			"tzinfo_name":"America\/Halifax",
			"name":"Atlantic Time (Canada)",
			"utc_offset":-14400
		},
		"discoverable_by_email":false,
		"sleep_time":{
			"enabled":false,
			"start_time":null,
			"end_time":null
		},
		"use_cookie_personalization":false,
		"always_use_https":true
	}

This can then be loaded and parsed via Python's `JSON` module:

	parsed = json.loads(result.text)

### API

Coming Soon.

### License

	Copyright © 2013 Mihir Singh <me@mihirsingh.com>
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of 
    this software and associated documentation files (the “Software”), to deal in 
    the Software without restriction, including without limitation the rights to 
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
    the Software, and to permit persons to whom the Software is furnished to do 
    so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all 
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY 
    KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
    IN THE SOFTWARE.
    
### Contributing

Just fork and submit a pull request ;)