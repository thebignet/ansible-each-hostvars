#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'each_hostvars': self.each_hostvars,
            'keep_attribute': self.keep_attribute,
            'each_format': self.each_format
        }

    def each_hostvars(self, hostnames, hostvars):
        return [
            hostvars[hostname]
            for hostname in hostnames
        ]

    def keep_attribute(self, server_hostvars, key):
        return [
            hostvars[key]
            for hostvars in server_hostvars
        ]

    def each_format(self, server_hostvars, f):
        return [
            f.format_map(hostvars)
            for hostvars in server_hostvars
        ]

        