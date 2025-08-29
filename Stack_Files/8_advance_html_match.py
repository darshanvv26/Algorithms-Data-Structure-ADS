import re

class HTMLMatcherWithAttributes:
    def __init__(self):
        self.stack = []

    def match_tags(self, html):
        tags = re.findall(r'<[^>]+>', html)

        for full_tag in tags:
            if full_tag.endswith('/>'):
                continue

            if full_tag.startswith('</'):
                tag_name = full_tag[2:-1].strip()
                if not self.stack or self.stack.pop() != tag_name:
                    print("Invalid HTML tags!")
                    return
                
            else:           
                tag_content = full_tag[1:-1].strip()
                tag_name = tag_content.split()[0]
                self.stack.append(tag_name)

        if not self.stack:
            print("Valid HTML tags!")
        else:
            print("Invalid HTML tags!")

html_code = """
<div class="container" id="main">
    <p style="color:red">Hello <b>World</b></p>
    <img src="image.jpg" /> <p>
</div>
"""

matcher = HTMLMatcherWithAttributes()
matcher.match_tags(html_code)
