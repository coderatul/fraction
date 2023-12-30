import math

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        # checkig for ZerodivisionError 
        if self.denominator == 0:
            raise ZeroDivisionError("can't devide by zero(0)")
        # if numerator of fraction objetc = 0, then changing it's denominator to 1
        elif self.numerator == 0:
            self.denominator = 1
        # checking if agrs are int or float only
        self.values = [self.numerator, self.denominator]
        for value in self.values:
            if not isinstance(value,(int,float)):
                raise TypeError("invalid operand(s): expected Frcation(int or float , int or float)")
            
    def __str__(self):
        # if numerator of fraction is zero, returning 0
        if self.numerator == 0:
            return '0'
        else:
            return f"{self.numerator}/{self.denominator}"
    
    def reduce(self):
        # farction to decimal or float 
        if (self.numerator % self.denominator) == 0:
            return self.numerator // self.denominator
        else:
            return self.numerator / self.denominator
        
    
    def add_different_denominator_fracs(self, *other):
        # calculating sum of fractions with uncommon denominators
        numerator = 0
        denominators = [self.denominator] # list of denominators, arg for math.lcm()
        # as first fraction is not iterable, adding i'ts denominator seperately
        for fraction in other:
            denominators.append(fraction.denominator)
        # calculating lcm 
        lcm = math.lcm(*denominators) #direferencing list object and calculating lcm
        # as first fraction is not iterable, performing it's calculation seperately
        numerator += self.numerator * (lcm // self.denominator)
        for fraction in other:
            numerator += fraction.numerator * (lcm // fraction.denominator)
        return Fraction(numerator, lcm)

    def __add__(self, *other):
        # flag for common denominators
        common_denominator = 1
        for fraction in other:
            # checking for common denominators
            if fraction.denominator == self.denominator:
                pass
            else:
                # if denominators are'nt common then changing the flag to 0
                common_denominator = 0 
        if common_denominator == 1:
            # calculating sum of fractions with common denominators 
            for fraction in other:
                self.numerator += fraction.numerator
            return Fraction(self.numerator,self.denominator)
        else:
            # if denominators are'nt common, calling add_different_denominator_fracs
            return self.add_different_denominator_fracs(*other)
        
    def subtract_different_denominator_fracs(self, *other):
                # calculating sum of fractions with uncommon denominators
        numerator = 0
        denominators = [self.denominator] # list of denominators, arg for math.lcm()
        # as first fraction is not iterable, adding i'ts denominator seperately
        for fraction in other:
            denominators.append(fraction.denominator)
        # calculating lcm 
        lcm = math.lcm(*denominators) #direferencing list object and calculating lcm
        # as first fraction is not iterable, performing it's calculation seperately
        numerator = self.numerator * (lcm // self.denominator)
        for fraction in other:
            numerator -= fraction.numerator * (lcm // fraction.denominator)
        return Fraction(numerator, lcm)
        
            
    def __sub__(self, *other):
                # flag for common denominators
        common_denominator = 1
        for fraction in other:
            # checking for common denominators
            if fraction.denominator == self.denominator:
                pass
            else:
                # if denominators are'nt common then changing the flag to 0
                common_denominator = 0 
        if common_denominator == 1:
            # calculating sum of fractions with common denominators 
            for fraction in other:
                self.numerator -= fraction.numerator
            return Fraction(self.numerator,self.denominator)
        else:
            # if denominators are'nt common, calling add_different_denominator_fracs
            return self.subtract_different_denominator_fracs(*other)
        
        
    def __mul__(self, *other):
        for fraction in other:
            self.numerator *= fraction.numerator
            self.denominator *= fraction.denominator
        return Fraction(self.numerator, self.denominator)
        
    def __truediv__(self, *other):
        for fraction in other:
            self.numerator = self.numerator * fraction.denominator
            self.denominator = self.denominator * fraction.numerator
        return Fraction(self.numerator, self.denominator)
    
    def __floordiv__(self, *other):
        return self.__truediv__(*other)
    
    def __mod__(self, *other):
        remainder = 0
        fractions = [self] + list(other)
        for i in range(len(fractions)-1):
            remainder = fractions[i].reduce() % fractions[i+1].reduce()
        return remainder
        
    
    def __pow__(self, other):
        if isinstance(self,(int,float)) or isinstance(other,(int,float)):
            raise TypeError("expecting fraction objects only")
        else:
            return math.pow(self.reduce(), other.reduce())
        
    def __lt__(self, *other):
        result = True
        fractions = [self] + list(other)
        for i in range(len(fractions)-1):
            if fractions[i].reduce() < fractions[i+1].reduce():
                pass
            else: 
                result = False
        return result
                
        
    def __le__(self, *other):
        result = True
        fractions = [self] + list(other)
        for i in range(len(fractions)-1):
            if fractions[i].reduce() <= fractions[i+1].reduce():
                pass
            else: 
                result = False
        return result

  
    def __eq__(self, *other):
        flag = 0
        for fraction in other:
            if fraction.reduce() == self.reduce():
                flag = 1
        if flag == 1:
            return True
        else:
            return False
                
        
    def __ne__(self, *other):
        flag = 0
        for fraction in other:
            if fraction.reduce() != self.reduce():
                flag = 1
        if flag == 1:
            return True
        else:
            return False
 
    def __gt__(self, *other):
        result = True
        fractions = [self] + list(other)
        for i in range(len(fractions)-1):
            if fractions[i].reduce() > fractions[i+1].reduce():
                pass
            else: 
                result = False
        return result
   
    def __ge__(self, *other):
        result = True
        fractions = [self] + list(other)
        for i in range(len(fractions)-1):
            if fractions[i].reduce() >= fractions[i+1].reduce():
                pass
            else: 
                result = False
        return result 
    
    def __ge__(self, *other: "Fraction") -> bool:
        """Compares fractions for greater than or equal to.

        Args:
            *other: One or more Fraction objects to compare to.

        Returns:
            True if self is greater than or equal to all other fractions,
            False otherwise.
        """

        result = True
        fractions = [self] + list(other)  # Combine fractions into a list
        for i in range(len(fractions) - 1):
            # If current fraction is less than the next, return False
            if fractions[i].reduce() < fractions[i + 1].reduce():
                result = False
                break
        return result  # True if self is greater than or equal to all other fractions
