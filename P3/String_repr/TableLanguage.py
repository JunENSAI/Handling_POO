class TableLanguage:

    def __init__(self,language:str, spec:str):
        self.language = language
        self.spec = spec
    
    def __str__(self):
        return f"This language {self.language} served on {self.spec}"

    def __repr__(self):
        return f"TableLanguage(language = '{self.language}', spec = '{self.spec}')"
    
tl = TableLanguage("SQL","relational database")
print(tl)

tl_repr = [tl]
print(tl_repr)