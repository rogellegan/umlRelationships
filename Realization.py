# 6_realization.py

from abc import ABC, abstractmethod

# Interface / Abstract Class
class Printable(ABC):
    @abstractmethod
    def print_details(self):
        pass

# Realization / Implementation
class Invoice(Printable):
    def __init__(self, amount: float):
        self.amount = amount

    def print_details(self):
        print(f"Invoice Total Amount: ${self.amount:.2f}")

if __name__ == "__main__":
    invoice = Invoice(150.75)
    invoice.print_details()
