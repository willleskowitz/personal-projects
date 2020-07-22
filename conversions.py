"""
# Name:         Will Leskowitz
# Project:      Personal Projects
# Script:       Conversions
# Date:         Wed Jul 22 00:26:46 2020
#
"""

def roman_to_decimal(roman):
    '''Converts string of roman numerals to decimal integer.'''
    conversions = {'I' : 1,
                   'V' : 5,
                   'X' : 10,
                   'L' : 50,
                   'C' : 100,
                   'D' : 500,
                   'M' : 1000}
    
    order = ('M', 'D', 'C', 'L', 'X', 'V', 'I')
    
    first = True
    decimal_num = 0
    
    for digit in roman:
        if first:
            decimal_num += conversions[digit]
            prior_digit = digit
            first = False
            
        else:
            if order.index(digit) >= order.index(prior_digit):
                decimal_num += conversions[digit]
                
            else:
                decimal_num -= conversions[prior_digit]
                decimal_num += conversions[digit] - conversions[prior_digit]
                
            prior_digit = digit
                
    return decimal_num


def decimal_to_roman(decimal):
    '''Converts decimal integer to string of roman numerals.'''
    conversions = {1 : 'I',
                   4 : 'IV',
                   5 : 'V',
                   9 : 'IX',
                   10 : 'X',
                   40 : 'XL',
                   50 : 'L',
                   90 : 'XC',
                   100 : 'C',
                   400 : 'CD',
                   500 : 'D',
                   900 : 'CM',
                   1000 : 'M'}
    
    order = sorted(conversions.keys(), reverse=True)
    
    roman_val = ''
    
    for value in order:
        while True:
            temp_val = decimal - value
            
            if temp_val < 0:
                break
            
            else:
                roman_val += conversions[value]
                decimal -= value
    
        if not decimal:
            break
    
    return roman_val


class VigenereCipher(object):
    '''Class that uses a key and an alphabet to encode and decode from the 
    Vigenère cipher. Characters that are not within the alphabet will remain
    the same.'''
    def __init__(self, key, alphabet):
        self.key = key * 10
        self.alphabet = alphabet * 10
    
    def encode(self, text):
        encrypted = ''
        for i, char in enumerate(text):
            if char not in self.alphabet:
                encrypted += char
            else:
                shift = self.alphabet.index(self.key[i])
                encrypted += self.alphabet[self.alphabet.index(char) + shift]
            
        return encrypted
    
    def decode(self, text):
        decrypted = ''
        for i, char in enumerate(text):
            if char not in self.alphabet:
                decrypted += char
            else:
                shift = self.alphabet.index(self.key[i])
                decrypted += self.alphabet[self.alphabet.index(char) - shift]
            
        return decrypted
    
