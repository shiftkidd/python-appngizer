class Error(Exception):
    '''  '''
class ElementError(Error):
    '''  '''
class ClientError(Error):
    '''  '''
class HttpClientBadRequest(Error):
    '''  '''
class HttpElementConflict(Error):
    '''  '''
class HttpElementNotFound(Error):
    '''  '''
class HttpElementForbidden(Error):
    '''  '''
class HttpServerError(Error):
    '''  '''
class NotAllowedOp(Error):
    '''  '''
class XMLValidationError(Error):
    '''  '''