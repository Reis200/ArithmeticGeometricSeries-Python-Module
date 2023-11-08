
class ArithmeticSeries:
    def find_nth_term_value(self,a_value,d_value,nth_term):
        value = a_value + (nth_term - 1)*d_value
        return value
    
    def find_a_from_nth_term(self,d_value,term_value,nth_term):
        a = int(term_value) + d_value*(1-nth_term)
        return a

    def find_d_from_nth_term(self,a_value,term_value,nth_term):
        d = (term_value - a_value) / (nth_term-1)
        return d

    def find_sum_of_series_up_to(self,a_value,d_value,nth_term):
        sum_of_series = (nth_term / 2) * (2*a_value + (nth_term - 1)*d_value)
        return sum_of_series

    def identify_items_of_sequence(self,arithmetic_sequence):
        d = int(arithmetic_sequence[1]) - int(arithmetic_sequence[0])
        a = arithmetic_sequence[0]
        number_of_terms = len(arithmetic_sequence)
        return f"initial term: {a}; common difference: {d}; number_of_terms: {number_of_terms}"

class GeometricSeries:    
     def find_nth_term_value(self,a_value,r_value,nth_term):
         value = a_value * r_value**(nth_term-1)
         return value
     def find_a_from_nth_term(self,r_value,term_value,nth_term):
         a = term_value / r_value**(nth_term-1)
         return a
     def find_r_from_nth_term(self,term_value,next_term_value):
         r = next_term_value / term_value
         return r
     def find_sum_of_series_up_to1(self,a_value,r_value,nth_term):
         sum_of_series = (a_value*(1-r_value**nth_term)) / (1 - r_value)
         return sum_of_series
     def find_sum_of_series_up_to2(self,a_value,r_value,nth_term):
         sum_of_series = (a_value*(r_value**nth_term-1)) / (r_value - 1)
         return sum_of_series
     def identify_items_of_sequence(self,arithmetic_sequence):
         r = int(arithmetic_sequence[1]) / int(arithmetic_sequence[0])
         a = arithmetic_sequence[0]
         number_of_terms = len(arithmetic_sequence)
         return f"initial term: {a}; common ratio: {r}; number_of_terms: {number_of_terms}"


a1 = ArithmeticSeries()
g1 = GeometricSeries()
