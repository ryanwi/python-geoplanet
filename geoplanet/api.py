
import urllib2

from exceptions import Exception


def _py26OrGreater():
    import sys
    return sys.hexversion > 0x20600f0

if _py26OrGreater():
    import json
else:
    import simplejson as json

class GeoPlanetError(Exception):
    """
    Base Exception thrown by the GeoPlanet object when there is a
    general error interacting with the API.
    """
    pass

class GeoPlanetHTTPError(GeoPlanetError):
    """
    Exception thrown by the GeoPlanet object when there is an
    HTTP error interacting with http://developer.yahoo.com/geo/geoplanet/.
    """
    def __init__(self, e, uri, format, encoded_args):
      self.e = e
      self.uri = uri
      self.format = format
      self.encoded_args = encoded_args

    def __str__(self):
        return (
            "GeoPlanet sent status %i for URL: %s.%s using parameters: "
            "(%s)\ndetails: %s" %(
                self.e.code, self.uri, self.format, self.encoded_args, 
                self.e.fp.read()))

class GeoPlanetCall(object):
    def __init__(
        self, appid, format, domain, uri="", 
        encoded_args=None):
        self.appid = appid
        self.format = format
        self.domain = domain
        self.uri = uri
        self.encoded_args = encoded_args

    def __getattr__(self, k):
        try:
            return object.__getattr__(self, k)
        except AttributeError:
            return GeoPlanetCall(
                self.appid, self.format, self.domain,
                self.uri + "/" + k, self.encoded_args)

    def __call__(self, **kwargs):
        uri = self.uri.strip("/")
        method = "GET"

        uriBase = "http://%s/%s%s%s%s" %(
                    self.domain, api_version, uri)

        if (not self.encoded_args):
            if kwargs.has_key('id'):
                uri += "/%s" %(kwargs['id'])

            self.encoded_args = self.auth.encode_params(uriBase, method, kwargs)

        argStr = ""
        argData = None
        if (method == "GET"):
            if self.encoded_args:
                argStr = "?%s" %(self.encoded_args)
        else:
            argData = self.encoded_args

        headers = {}

        req = urllib2.Request(uriBase+argStr, argData, headers)
        
        try:
            handle = urllib2.urlopen(req)
            if "json" == self.format:
                return json.loads(handle.read())
            else:
                return handle.read()
        except urllib2.HTTPError, e:
            if (e.code == 304):
                return []
            else:
                raise GeoPlanetHTTPError(e, uri, self.format, self.encoded_args)

class GeoPlanet(GeoPlanetCall):
    """
    The minimalist yet fully featured GeoPlanet API class.

    Get RESTful data by accessing members of this class. The result
    is decoded python objects (lists and dicts).

    The GeoPlanet API is documented here:

      http://developer.yahoo.com/geo/geoplanet/guide/

    Examples::

      geoplanet = GeoPlanet(appid=[yourappidhere])

      # Get 
      geoplanet.


    Using the data returned
    -----------------------

    GeoPlanet API calls return decoded JSON. This is converted into
    a bunch of Python lists, dicts, ints, and strings. For example::

      x = geoplanet.


    Getting raw XML data
    --------------------

    If you prefer to get your GeoPlanet data in XML format, pass
    format="xml" to the GeoPlanet object when you instantiate it::

      geoplanet = GeoPlanet(appid=[yourappidhere], format="xml")

      The output will not be parsed in any way. It will be a raw string
      of XML.

    """
    def __init__(
        self, format="json",
        domain="http://where.yahooapis.com/", agent=None, secure=False, appid=None,
        api_version='v1'):
        """
        Create a new GeoPlanet API connector.

        `domain` lets you change the domain you are connecting. By
        default it's where.yahooapis.com.

        `api_version` is used to set the base uri. By default it's
        'v1'.
        """
        
        if (format not in ("json", "geojson", "xml", "")):
            raise ValueError("Unknown data format '%s'" %(format))

        uri = ""
        if api_version:
            uri = str(api_version)

        GeoPlanetCall.__init__(
            self, appid, format, domain, uri, secure=secure)

__all__ = ["GeoPlanet", "GeoPlanetError", "GeoPlanetHTTPError"]
