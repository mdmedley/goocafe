from cafe.engine.clients.rest import AutoMarshallingRestClient


class GoogleClient(AutoMarshallingRestClient):

    def __init__(self, serialize_format, deserialize_format, url):
        super(GoogleClient, self).__init__(serialize_format,
                                           deserialize_format)

        self.url = url

    def search(self, criteria, requestslib_kwargs=None):
        path = "{url}/#q={criteria}".format(url=self.url, criteria=criteria)
        response = self.request("GET", path,
                                requestslib_kwargs=requestslib_kwargs)

        return response
