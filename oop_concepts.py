class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    # @staticmethod
    # def from_sum(value1, value2):
    #    return FixedFloat(value1 + value2)

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


static_number = FixedFloat.from_sum(19.575, 0.789)
print(static_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


euros = Euro(18.5963)
print(Euro.from_sum(16.7565, 90))  # <Euro €106.75>
