class DigitalSignageCMS:
    def __init__(self):
        self.content = {}
    
    def add_content(self, content_id, content):
        """Add new content to the CMS."""
        self.content[content_id] = content
    
    def fetch_content_for_display(self):
        """Fetch content for display in HTML format."""
        # Convert content dictionary to HTML-friendly format
        html_content = {}
        for content_id, content in self.content.items():
            html_content[content_id] = f"<div class='content-item'>{content}</div>"
        return html_content
