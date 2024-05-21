class AutomationService:
    def __init__(self):
        pass

    def schedule_content(self, content_id):
        """Schedule content for display."""
        # Code to schedule content
        pass

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.automation = AutomationService()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.automation.schedule_content(content_id) 
