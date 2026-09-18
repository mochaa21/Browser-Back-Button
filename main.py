class Web:
    def __init__(self, value):
        self.value = value
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.last_url = None
        self.url_visited = 0

    def visit_page(self, element):
        new_url_node = Web(element)
        if self.last_url:
            new_url_node.next = self.last_url
        self.last_url = new_url_node
        self.url_visited += 1

    def go_back(self):
        if self.isEmpty():
            return "History is empty. Opening New Tab."
        poppedURL = self.last_url
        self.url_visited -= 1
        return poppedURL

    def isEmpty(self):
        return self.url_visited == 0

    def StackSize(self):
        return self.url_visited