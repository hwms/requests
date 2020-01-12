# -*- coding: utf-8 -*-

r"""
The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.

Example::

    >>> import requests
    >>> requests.codes['temporary_redirect']
    307
    >>> requests.codes.teapot
    418
    >>> requests.codes['\o/']
    200

Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.
"""


class Codes():

    def __init__(self):
        self.continue_ = 100
        self.__dict__['continue'] = 100
        self.CONTINUE = 100
        self.switching_protocols = 101
        self.SWITCHING_PROTOCOLS = 101
        self.processing = 102
        self.PROCESSING = 102
        self.checkpoint = 103
        self.CHECKPOINT = 103
        self.uri_too_long = 122
        self.URI_TOO_LONG = 122
        self.request_uri_too_long = 122
        self.REQUEST_URI_TOO_LONG = 122
        self.ok = 200
        self.OK = 200
        self.okay = 200
        self.OKAY = 200
        self.all_ok = 200
        self.ALL_OK = 200
        self.all_okay = 200
        self.ALL_OKAY = 200
        self.all_good = 200
        self.ALL_GOOD = 200
        self.__dict__['\\o/'] = 200
        self.__dict__['✓'] = 200
        self.created = 201
        self.CREATED = 201
        self.accepted = 202
        self.ACCEPTED = 202
        self.non_authoritative_info = 203
        self.NON_AUTHORITATIVE_INFO = 203
        self.non_authoritative_information = 203
        self.NON_AUTHORITATIVE_INFORMATION = 203
        self.no_content = 204
        self.NO_CONTENT = 204
        self.reset_content = 205
        self.RESET_CONTENT = 205
        self.reset = 205
        self.RESET = 205
        self.partial_content = 206
        self.PARTIAL_CONTENT = 206
        self.partial = 206
        self.PARTIAL = 206
        self.multi_status = 207
        self.MULTI_STATUS = 207
        self.multiple_status = 207
        self.MULTIPLE_STATUS = 207
        self.multi_stati = 207
        self.MULTI_STATI = 207
        self.multiple_stati = 207
        self.MULTIPLE_STATI = 207
        self.already_reported = 208
        self.ALREADY_REPORTED = 208
        self.im_used = 226
        self.IM_USED = 226
        self.multiple_choices = 300
        self.MULTIPLE_CHOICES = 300
        self.moved_permanently = 301
        self.MOVED_PERMANENTLY = 301
        self.moved = 301
        self.MOVED = 301
        self.__dict__['\\o-'] = 301
        self.found = 302
        self.FOUND = 302
        self.see_other = 303
        self.SEE_OTHER = 303
        self.other = 303
        self.OTHER = 303
        self.not_modified = 304
        self.NOT_MODIFIED = 304
        self.use_proxy = 305
        self.USE_PROXY = 305
        self.switch_proxy = 306
        self.SWITCH_PROXY = 306
        self.temporary_redirect = 307
        self.TEMPORARY_REDIRECT = 307
        self.temporary_moved = 307
        self.TEMPORARY_MOVED = 307
        self.temporary = 307
        self.TEMPORARY = 307
        self.permanent_redirect = 308
        self.PERMANENT_REDIRECT = 308
        self.resume_incomplete = 308
        self.RESUME_INCOMPLETE = 308
        self.resume = 308
        self.RESUME = 308
        self.bad_request = 400
        self.BAD_REQUEST = 400
        self.bad = 400
        self.BAD = 400
        self.unauthorized = 401
        self.UNAUTHORIZED = 401
        self.payment_required = 402
        self.PAYMENT_REQUIRED = 402
        self.payment = 402
        self.PAYMENT = 402
        self.forbidden = 403
        self.FORBIDDEN = 403
        self.not_found = 404
        self.NOT_FOUND = 404
        self.__dict__['-o-'] = 404
        self.method_not_allowed = 405
        self.METHOD_NOT_ALLOWED = 405
        self.not_allowed = 405
        self.NOT_ALLOWED = 405
        self.not_acceptable = 406
        self.NOT_ACCEPTABLE = 406
        self.proxy_authentication_required = 407
        self.PROXY_AUTHENTICATION_REQUIRED = 407
        self.proxy_auth = 407
        self.PROXY_AUTH = 407
        self.proxy_authentication = 407
        self.PROXY_AUTHENTICATION = 407
        self.request_timeout = 408
        self.REQUEST_TIMEOUT = 408
        self.timeout = 408
        self.TIMEOUT = 408
        self.conflict = 409
        self.CONFLICT = 409
        self.gone = 410
        self.GONE = 410
        self.length_required = 411
        self.LENGTH_REQUIRED = 411
        self.precondition_failed = 412
        self.PRECONDITION_FAILED = 412
        self.precondition = 412
        self.PRECONDITION = 412
        self.request_entity_too_large = 413
        self.REQUEST_ENTITY_TOO_LARGE = 413
        self.request_uri_too_large = 414
        self.REQUEST_URI_TOO_LARGE = 414
        self.unsupported_media_type = 415
        self.UNSUPPORTED_MEDIA_TYPE = 415
        self.unsupported_media = 415
        self.UNSUPPORTED_MEDIA = 415
        self.media_type = 415
        self.MEDIA_TYPE = 415
        self.requested_range_not_satisfiable = 416
        self.REQUESTED_RANGE_NOT_SATISFIABLE = 416
        self.requested_range = 416
        self.REQUESTED_RANGE = 416
        self.range_not_satisfiable = 416
        self.RANGE_NOT_SATISFIABLE = 416
        self.expectation_failed = 417
        self.EXPECTATION_FAILED = 417
        self.im_a_teapot = 418
        self.IM_A_TEAPOT = 418
        self.teapot = 418
        self.TEAPOT = 418
        self.i_am_a_teapot = 418
        self.I_AM_A_TEAPOT = 418
        self.misdirected_request = 421
        self.MISDIRECTED_REQUEST = 421
        self.unprocessable_entity = 422
        self.UNPROCESSABLE_ENTITY = 422
        self.unprocessable = 422
        self.UNPROCESSABLE = 422
        self.locked = 423
        self.LOCKED = 423
        self.failed_dependency = 424
        self.FAILED_DEPENDENCY = 424
        self.dependency = 424
        self.DEPENDENCY = 424
        self.unordered_collection = 425
        self.UNORDERED_COLLECTION = 425
        self.unordered = 425
        self.UNORDERED = 425
        self.upgrade_required = 426
        self.UPGRADE_REQUIRED = 426
        self.upgrade = 426
        self.UPGRADE = 426
        self.precondition_required = 428
        self.PRECONDITION_REQUIRED = 428
        self.precondition = 428
        self.PRECONDITION = 428
        self.too_many_requests = 429
        self.TOO_MANY_REQUESTS = 429
        self.too_many = 429
        self.TOO_MANY = 429
        self.header_fields_too_large = 431
        self.HEADER_FIELDS_TOO_LARGE = 431
        self.fields_too_large = 431
        self.FIELDS_TOO_LARGE = 431
        self.no_response = 444
        self.NO_RESPONSE = 444
        self.none = 444
        self.NONE = 444
        self.retry_with = 449
        self.RETRY_WITH = 449
        self.retry = 449
        self.RETRY = 449
        self.blocked_by_windows_parental_controls = 450
        self.BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS = 450
        self.parental_controls = 450
        self.PARENTAL_CONTROLS = 450
        self.unavailable_for_legal_reasons = 451
        self.UNAVAILABLE_FOR_LEGAL_REASONS = 451
        self.legal_reasons = 451
        self.LEGAL_REASONS = 451
        self.client_closed_request = 499
        self.CLIENT_CLOSED_REQUEST = 499
        self.internal_server_error = 500
        self.INTERNAL_SERVER_ERROR = 500
        self.server_error = 500
        self.SERVER_ERROR = 500
        self.__dict__['/o\\'] = 500
        self.__dict__['✗'] = 500
        self.not_implemented = 501
        self.NOT_IMPLEMENTED = 501
        self.bad_gateway = 502
        self.BAD_GATEWAY = 502
        self.service_unavailable = 503
        self.SERVICE_UNAVAILABLE = 503
        self.unavailable = 503
        self.UNAVAILABLE = 503
        self.gateway_timeout = 504
        self.GATEWAY_TIMEOUT = 504
        self.http_version_not_supported = 505
        self.HTTP_VERSION_NOT_SUPPORTED = 505
        self.http_version = 505
        self.HTTP_VERSION = 505
        self.variant_also_negotiates = 506
        self.VARIANT_ALSO_NEGOTIATES = 506
        self.insufficient_storage = 507
        self.INSUFFICIENT_STORAGE = 507
        self.bandwidth_limit_exceeded = 509
        self.BANDWIDTH_LIMIT_EXCEEDED = 509
        self.bandwidth = 509
        self.BANDWIDTH = 509
        self.not_extended = 510
        self.NOT_EXTENDED = 510
        self.network_authentication_required = 511
        self.NETWORK_AUTHENTICATION_REQUIRED = 511
        self.network_auth = 511
        self.NETWORK_AUTH = 511
        self.network_authentication = 511
        self.NETWORK_AUTHENTICATION = 511

    def __repr__(self):
        return "<lookup 'status_codes'>"

    def __getitem__(self, key):
        # We allow fall-through here, so values default to None
        return self.__dict__.get(key, None)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


codes = Codes()


def _init():

    def doc(code):
        names = ', '.join('``%s``' % n for n in _codes[code])
        return '* %d: %s' % (code, names)

    _codes = {}
    for title, code in codes.__dict__.items():
        if title[0] == title[0].lower() and title[-1] != '_':
            _codes.setdefault(code, []).append(title)

    global __doc__  #@ReservedAssignment
    __doc__ = (__doc__ + '\n' +  #@ReservedAssignment
               '\n'.join(doc(code) for code in sorted(_codes))
               if __doc__ is not None else None)


_init()
