class SecurityService:
    def __init__(self):
        pass

    def encrypt_content(self, content_id):
        """Encrypt content for security."""
        # Code to encrypt content
        pass

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.security = SecurityService()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.security.encrypt_content(content_id) 
