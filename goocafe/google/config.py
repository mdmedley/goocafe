from cloudcafe.common.models.configuration import ConfigSectionInterface


class GoogleServerConfig(ConfigSectionInterface):
    SECTION_NAME = 'server'

    @property
    def endpoint(self):
        return self.get("endpoint")

class GoogleFormatConfig(ConfigSectionInterface):
    SECTION_NAME = 'format'

    @property
    def input(self):
        return self.get("input")

    @property
    def output(self):
        return self.get("output")
