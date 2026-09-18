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
        self.last_url = self.last_url.next
        self.url_visited -= 1
        return poppedURL.value

    def isEmpty(self):
        return self.url_visited == 0

    def StackSize(self):
        return self.url_visited

riwayat_aby = BrowserHistory()

riwayat_aby.visit_page("google.com")
riwayat_aby.visit_page("roadmap.sh/python")
riwayat_aby.visit_page("stackoverflow.com/questions/linked-list")

print("Mundur ke:", riwayat_aby.go_back()) 
print("Mundur ke:", riwayat_aby.go_back())
print("Mundur ke:", riwayat_aby.go_back())
print("Mundur ke:", riwayat_aby.go_back())