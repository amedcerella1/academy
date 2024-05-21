class CloudStorage:
    def __init__(self):
        self.storage = {}

    def upload_content(self, content_id, content):
        """Upload content to cloud storage."""
        self.storage[content_id] = content

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.storage = CloudStorage()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.storage.upload_content(content_id, content) 
