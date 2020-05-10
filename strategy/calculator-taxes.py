# Designer patterns
# Strategy

from budget import Budget
from taxes import ISS, ICMS


class Calculator_taxes:

    def calc_taxes(self, budget, tax):
        calculated_tax = tax.calc(budget)
        print(calculated_tax)


if __name__ == '__main__':

    calc = Calculator_taxes()

    budget = Budget(100)

    calc.calc_taxes(budget, ISS())
    calc.calc_taxes(budget, ICMS())
