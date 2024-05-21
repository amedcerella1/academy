class UserInterface:
    def __init__(self):
        self.content_list = []

    def update_content_list(self):
        """Update the UI content list."""
        # Code to update the UI content list
        pass

class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
        self.ui = UserInterface()

    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
        self.ui.update_content_list() 
