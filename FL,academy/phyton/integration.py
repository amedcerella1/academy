class IntegrationService:
    def __init__(self):
        pass

    def notify_external_system(self, content_id):
        """Notify external system about new content."""
        # Code to notify external system
        pass

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.integration = IntegrationService()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.integration.notify_external_system(content_id) 
