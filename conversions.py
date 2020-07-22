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
    

def text_to_piglatin(text):
    '''Converts string of text to piglatin and ignores punctuation.'''
    punctuation = {',', '.', '?', '!'}
    piglatin = []
    
    for word in text.split():
        if word in punctuation:
            piglatin.append(word)
        elif word[-1] in punctuation:
            piglatin.append(word[1:-1] + word[0] + 'ay' + word[-1])
        else:
            piglatin.append(word[1:] + word[0] + 'ay')
            
    return ' '.join(piglatin)


def to_camel_case(text):
    '''Converts dash and underscore delimited words into camel case. 
    The capitalization of the first word will remain the same.'''
    words = text.replace('-', ' ').replace('_', ' ').split()
    return ''.join([word.title() if words.index(word) > 0 else word for word in words])


def format_duration(seconds):
    '''Given seconds, the fuction returns a human readable string such as 
    "5 hours, 1 minute and 42 seconds". An input of 0 will return "now", and 
    any non-natural nuumber will return False.'''
    
    if type(seconds) != int:
        return False
    elif seconds < 0:
        return False
    elif seconds == 0:
        return 'now'
    
    counts = dict()
    readable = ''
    
    conversions = {'year' : 365*24*60*60,
                   'day' : 24*60*60,
                   'hour' : 60*60,
                   'minute' : 60,
                   'second' : 1}
    
    for unit, value in conversions.items():
        count = 0
        
        while True:
            seconds -= value
            count += 1
                
            if seconds < 0:
                seconds += value
                count -= 1
                break
            
        if count == 1:
            counts[unit] = count
        elif count > 1:
            counts[unit + 's'] = count
    
        if not seconds: break
          
    counts_list = list(counts.items())
    
    for i, ele in enumerate(counts_list):
        if len(counts_list) - i >= 3:
            readable += '%s %s, ' % (counts_list[i][1], counts_list[i][0])
        elif len(counts_list) - i == 2:
            readable += '%s %s and ' % (counts_list[i][1], counts_list[i][0])
        else:
            readable += '%s %s' % (counts_list[i][1], counts_list[i][0])
            
    return readable
