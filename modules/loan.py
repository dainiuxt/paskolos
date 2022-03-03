class Record:
  def __init__(self, id, amount, term, interest_rate):
    self.id = id
    self.amount = amount
    self. term = term
    self.interest = interest_rate

  def __str__(self):
      return f"Loan {self.id}. Amount: {self.amount}, {self.term} months for {self.interest}%"

class Loans:
  def __init__(self):
    self.book = []

  def append(self, rec):
    self.book.append(rec)

  def __repr__(self):
      return f"Loan {self.id}. Amount: {self.amount}, {self.term} months for {self.interest}%"