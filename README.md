## PyUnio, A Python Implementation of Tezel's unio

__PyUnio is currently in alpha and should not be considered stable.__

### What

PyUnio is a rewrite of Tolga Tezel's [unio](https://github.com/ttezel/unio) (a Node.js solution) in Python.

_Keep in mind that PyUnio may not implement every feature of unio, but at the same time, it may implement more._

Any `specs` should be downloaded from Tezel's original repository and placed in the `specs` directory in the same file as `pyunio.py`.

### Implementations

Node.js:

* [unio](https://github.com/ttezel/unio) by Tolga Tezel (@ttezel)
	
Python:
	
* [PyUnio](https://github.com/citruspi/PyUnio) by Mihir Singh (@citruspi)

### Install

Either

    python setup.py
    
or

	pip install pyunio
	
followed by

	pip install -r requirements.txt
	
### Usage

#### Twitter - Get User Settings

The following code is an implementation of Twitter's API with PyUnio:

	from pyunio import pyunio
	
	params = {
				'consumer_secret'    : 'ITS A SECRET',
				'consumer_key'       : 'ITS A SECRET',
				'access_token'       : 'ITS A SECRET',
				'access_token_secret': 'ITS A SECRET'
			 }
	
	pyunio.use('twitter')
	
	result, error = pyunio.get('account/settings', params)
	
	print result.text


The output of `result.text` is

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

This can then be loaded and parsed via Python's `JSON` module.

### API

Coming Soon.

### License

	Copyright © 2012 Mihir Singh <me@mihirsingh.com>
    
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