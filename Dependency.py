# 5_dependency.py

class Document:
    def __init__(self, content: str):
        self.content = content

class Printer:
    # Printer depends on Document to perform the print action
    def print_document(self, doc: Document):
        print(f"Printing document content: '{doc.content}'")

if __name__ == "__main__":
    doc = Document("Hello UML World!")
    printer = Printer()
    printer.print_document(doc)
    
