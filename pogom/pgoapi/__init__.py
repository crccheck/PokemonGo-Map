"""
pgoapi - Pokemon Go API
Copyright (c) 2016 tjado <https://github.com/tejado>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.

Author: tjado <https://github.com/tejado>
"""

from __future__ import absolute_import

from .exceptions import PleaseInstallProtobufVersion3

import pkg_resources
import logging

__title__ = 'pgoapi'
__version__ = '1.1.7'
__author__ = 'tjado'
__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2016 tjado <https://github.com/tejado>'

from .pgoapi import PGoApi
from .rpc_api import RpcApi
from .auth import Auth

logging.getLogger("pgoapi").addHandler(logging.NullHandler())
logging.getLogger("rpc_api").addHandler(logging.NullHandler())
logging.getLogger("utilities").addHandler(logging.NullHandler())
logging.getLogger("auth").addHandler(logging.NullHandler())
logging.getLogger("auth_ptc").addHandler(logging.NullHandler())
logging.getLogger("auth_google").addHandler(logging.NullHandler())

try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass