
from google.appengine.ext import ndb

class URLMap(ndb.Model):
    """
    URLMap model for mapping shortcodes to URLS
    """
    # URLMap Properties
    counter = ndb.IntegerProperty(required = False)
    url = ndb.StringProperty(required = True)
    shortcode = ndb.StringProperty(required = True)

    @classmethod
    def is_shortcode_available(self, shortcode):
        """Check if a shortcode is available to use"""
        return self.query(self.shortcode == shortcode).count() is 0

    @classmethod
    def get_url_by_shortcode(self, shortcode):
        """Return the first URL matching a shortcode query"""
        urlmap_list = self.query(self.shortcode == shortcode)/fetch(1)
        if len(urlmap_list) == 0:
            return None
        else:
            return urlmap_list[0]

    def is_still_valid(self):
        """Return if this URLMap is still valid"""
        return self.counter > 0

# Debug
if __name__ == '__main__':
    pass
