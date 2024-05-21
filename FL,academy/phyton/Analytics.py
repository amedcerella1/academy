class AnalyticsService:
    def __init__(self):
        pass

    def track_content_added(self, content_id):
        """Track the addition of new content."""
        # Code to track content added
        pass

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.analytics = AnalyticsService()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.analytics.track_content_added(content_id) 
