import pt_math

class simple_fraction:
    def __init__(self, numerator, denominator):
        
        numerator_dividers = pt_math.get_dividers(numerator)
        numerator_denominator = pt_math.get_dividers(denominator)

        common_dividers = []
        for divider_n in numerator_dividers:
            for divider_d in numerator_denominator:
                if divider_n == divider_d:
                    common_dividers.append(divider_n)
                    numerator_denominator.remove(divider_n)
                    break
        
        max_common_divider = 1
        for divider in common_dividers:
            max_common_divider = max_common_divider * divider

        
        self.numerator = int(numerator/max_common_divider)
        self.denominator = int(denominator/max_common_divider)

    def to_string(self):
        return str(self.numerator) + '/' + str(self.denominator)

def sum_fraction(a, b):
    
    numerator_dividers = pt_math.get_dividers(a.numerator*b.denominator + b.numerator*a.denominator)
    numerator_denominator = pt_math.get_dividers(a.denominator*b.denominator)
    
    common_dividers = []
    for divider_n in numerator_dividers:
        for divider_d in numerator_denominator:
            if divider_n == divider_d:
                common_dividers.append(divider_n)
                numerator_denominator.remove(divider_n)
                break
        
    max_common_divider = 1
    for divider in common_dividers:
        max_common_divider = max_common_divider * divider

    numerator =  int((a.numerator*b.denominator + b.numerator*a.denominator)/max_common_divider)
    denominator = int((a.denominator*b.denominator)/max_common_divider)

    return simple_fraction(numerator, denominator)

def sum(a, b):
    if type(a) is int:
        if type(b) is int:
            result = a + b
        else:
            a = simple_fraction(a, 1)
            result = sum_fraction(a, b)
    else:
        if type(b) is int:
            b = simple_fraction(b, 1)
            result = sum_fraction(a, b)
        else:
            result = sum_fraction(a, b)
    
    return result

def diff(a, b):

    if type(b) is int:
        b = b * (-1)
    else:
        b.numerator = b.numerator * (-1)

    return sum(a, b)