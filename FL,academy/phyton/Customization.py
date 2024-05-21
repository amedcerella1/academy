class CustomizationService:
    def __init__(self):
        pass

    def customize_content(self, content_id):
        """Customize content based on user preferences."""
        # Code to customize content
        pass

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.customization = CustomizationService()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.customization.customize_content(content_id) 
