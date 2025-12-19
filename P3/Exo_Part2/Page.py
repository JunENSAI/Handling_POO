class Page:

    def __init__(self, item_list:list[str],page_size:int):
        self.item_list = item_list
        self.page_size = page_size
    
    def __iter__(self):
        first_page = self.item_list[:self.page_size]
        return iter(first_page)
    
    @classmethod
    def from_text(cls, item_str, page_size):
        item_cln = item_str.split(",")
        return cls(item_cln, page_size)
    
    @staticmethod
    def helper_message():
        return "Pagination helps manage large datasets"

p = Page.from_text("a,b,c,d", 2)

for item in p:
    print(item)

print(f"Info: {Page.helper_message()}")