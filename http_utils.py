#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import logging

info_logger = logging.getLogger(__name__)


class HttpClient(object):
    @staticmethod
    def http_request(url, method="GET", params=None, data=None, headers=None, auth=None):
        # update url if http is missing
        if not url.startswith("http"):
            url = "http://{}".format(url)

        return HttpClient.send_request(url=url,
                                 method=method,
                                 params=params,
                                 data=data,
                                 headers=headers,
                                 auth=auth)

    @staticmethod
    def https_request(url, method="GET", params=None, data=None, headers=None, auth=None):
        # update url if https is missing
        if not url.startswith("https"):
            url = "https://{}".format(url)

        return HttpClient.send_request(url=url,
                                 method=method,
                                 params=params,
                                 data=data,
                                 headers=headers,
                                 auth=auth)

    @staticmethod
    def send_request(url, method="GET", params=None, data=None, headers=None, auth=None):
        info_logger.debug("send_request: beginning to HttpRequest")
        r = None

        # if url is None:
        #     info_logger.warning("send_request: url is None")
        # if method == "":
        #     info_logger.warning("send_request: method is empty")
        # if params is None:
        #     info_logger.debug("send_request: params is None")
        # if headers is None:
        #     info_logger.debug("send_request: header is None")
        # if data is None:
        #     info_logger.debug("send_request: data is None")
        # if auth is None:
        #     info_logger.debug("send_request: auth is None")
        
        # info_logger.debug("send_request: url({})".format(url))
        # info_logger.debug("send_request: method({})".format(method))
        # info_logger.debug("send_request: params({})".format(params))
        # info_logger.debug("send_request: data({})".format(data))
        # info_logger.debug("send_request: headers({})".format(headers))
        # info_logger.debug("send_request: auth({})".format(auth))

        try:
            if method == "GET":
                r = requests.get(url=url,
                                 params=params,
                                 data=data,
                                 headers=headers,
                                 auth=auth,
                                 verify=False)
            elif method == "POST":
                r = requests.post(url=url,
                                  params=params,
                                  json=data,
                                  headers=headers,
                                  auth=auth,
                                  verify=False)
            elif method == "PUT":
                r = requests.put(url=url,
                                 params=params,
                                 json=data,
                                 headers=headers,
                                 auth=auth,
                                 verify=False)
            elif method == "OPTIONS":
                r = requests.options(url=url,
                                     params=params,
                                     data=data,
                                     headers=headers,
                                     auth=auth,
                                     verify=False)
            elif method == "DELETE":
                r = requests.delete(url=url,
                                    params=params,
                                    data=data,
                                    headers=headers,
                                    auth=auth)
            else:
                info_logger.warning(
                    "send_request: incorrect method(%s), please try later, quitting now..." % method)
                return None

            info_logger.debug("send_request: r.url({})".format(r.url))

        except requests.ConnectTimeout as e:
            info_logger.error("send_request: time out exception: e({0})".format(e))
        except requests.ConnectionError as e:
            info_logger.error("send_request: connection exception: e({0})".format(e))
        except requests.HTTPError as e:
            info_logger.error("send_request: http exception: e({0})".format(e))
        except requests.RequestException as e:
            info_logger.error("send_request: general exception: e({0})".format(e))
            import traceback
            traceback.print_exc()
        finally:
            info_logger.debug(
                "send_request: ending to send_request, response({0})".format(r))
            return r
