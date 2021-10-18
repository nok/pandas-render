class Template:

    def __init__(self, template: str):
        self.template = template

    def render(self) -> str:
        return self.template
