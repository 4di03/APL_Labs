from uncertainties import ufloat


def least_significant_digit_power(num_string : str):
    print(num_string)

    if 'e' in num_string:
        # There's an exponent. Figure out what it is and negate it.

        dec,pow= num_string.split('e')

        pow = int(pow)
        if pow < 0:

            num_dec = abs(int(pow))+ len(dec.split('.')[1])
            return -1* num_dec

        else:
            return pow +1


    if '.' in num_string:
        # There's a decimal point. Figure out how many digits are to the right
        # of the decimal point and negate that.
        return -len(num_string.partition('.')[2])
    else:
        # No decimal point. Count trailing zeros.
        return len(num_string) - len(num_string.rstrip('0'))
    



def get_pct_error_ufloat(n, pct_error = 0.03):
    '''
    Given a measuremnet n, returns a ufloat where error is 0.03 * n, per Hari's instructions
    
    '''

    f = ufloat(n, pct_error * n)

    return f
def get_apl_ufloat(n):
    '''
    Given a measuremnet n, returns a ufloat where error is 1 * 10^(-least_significant_digit_power(n)), per Hari's instructions
    
    '''

    str_n = str(n)
    #print(str_n)

    pow = least_significant_digit_power(str_n)
    #print(pow)

    f = ufloat(n, 10**pow)

    return f

