import re

class HTMLMatcher:
    def __init__(self):
        self.stack = []

    def match_tags(self, html):
        tags = re.findall(r'<(/?[\w]+)[^>]*>', html)

        for tag in tags:
            if not tag.startswith('/'):
                self.stack.append(tag)
            else:
                if not self.stack or self.stack.pop() != tag[1:]:
                    print("Invalid HTML tags!")
                    return

        if not self.stack:
            print("Valid HTML tags!")
        else:
            print("Invalid HTML tags!")

html_code = """
<div>
    <p>Hello <b>World</b></p>
</div>
"""

matcher = HTMLMatcher()
matcher.match_tags(html_code)