class APIError(Exception):
    def __init__(self, http_status, error_code, rsp=None, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.http_status = http_status
        self.error_code = error_code
        self.rsp = rsp

    def __str__(self):
        code_str = "HTTP %d" % self.http_status

        if self.error_code:
            code_str += ', API Error %d' % self.error_code

        if self.rsp and 'err' in self.rsp:
            return '%s (%s)' % (self.rsp['err']['msg'], code_str)
        else:
            return code_str


class ResourceError(Exception):
    def __init__(self, msg, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.msg = msg

    def __str__(self):
        return self.msg


class ServerInterfaceError(Exception):
    def __init__(self, msg, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.msg = msg

    def __str__(self):
        return self.msg


class ChildResourceUncreatableError(ResourceError):
    pass


class InvalidChildResourceUrlError(ResourceError):
    pass


class InvalidResourceTypeError(ResourceError):
    pass


class InvalidKeyError(ResourceError):
    pass


class RequestFailedError(ResourceError):
    pass


class UnloadedResourceError(ResourceError):
    pass


class UnknownResourceTypeError(ResourceError):
    pass


class InvalidRequestMethodError(ServerInterfaceError):
    pass


class AuthenticationFailedError(ServerInterfaceError):
    pass