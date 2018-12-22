def digit_cancel(nominator, denominator):
    
    if nominator >= denominator:
        raise ValueError('numerator must be less than denominator')
    
    nominator_tens, nominator_units = str(nominator)
    denominator_tens, denominator_units = str(denominator)
    
    if not int(denominator_units) and not int(nominator_units):
        return False
    
    if nominator_tens == denominator_tens:
        digit_canceled_nominator = int(nominator_units)
        digit_canceled_denominator = int(denominator_units)

    elif nominator_tens == denominator_units:
        digit_canceled_nominator = int(nominator_units)
        digit_canceled_denominator = int(denominator_tens)
    
    elif nominator_units == denominator_tens:
        digit_canceled_nominator = int(nominator_tens)
        digit_canceled_denominator = int(denominator_units)

    elif nominator_units == denominator_units:
        digit_canceled_nominator = int(nominator_tens)
        digit_canceled_denominator = int(denominator_tens)

    else:
        return False
    
    if not digit_canceled_denominator:
        return False
    
    value = digit_canceled_nominator / digit_canceled_denominator
    result = {
        'digit_canceled_denominator' : digit_canceled_denominator,
        'digit_canceled_nominator' : digit_canceled_nominator,
        'digit_canceled_value' : value
    }
    
    return result

def find_digit_canceling_fractions():
    
    for nominator in range(10, 100):

        # initiate 'nominator'
        denominator = nominator+1

        while denominator < 100:
            # check whether value remains the same
            original_value = nominator / denominator
            digit_cancel_value = digit_cancel(nominator, denominator)
            if digit_cancel_value:
                if original_value == digit_cancel_value['digit_canceled_value']:
                    result = {
                        'digit_canceled_nominator' : digit_cancel_value['digit_canceled_nominator'],
                        'digit_canceled_denominator' : digit_cancel_value['digit_canceled_denominator'],
                    }
                    yield result

            denominator += 1

def simplify_fraction(nominator, denominator):
    for n in range(2, min(nominator, denominator)+1):
        # find a common factor
        if (nominator%n or denominator%n):
            continue
        else:
            # continue until they're divisible
            while (not nominator%n and not denominator%n):
                nominator /= n
                denominator /= n

            result = {
                'nominator' : nominator,
                'denominator' : denominator
            }
            return result

def main():
    
    product_of_nominator = 1
    product_of_denominator = 1

    for fraction in find_digit_canceling_fractions():
        product_of_nominator *= fraction['digit_canceled_nominator']
        product_of_denominator *= fraction['digit_canceled_denominator']
        
    answer = simplify_fraction(product_of_nominator, product_of_denominator)
    print(answer['denominator'])
    return answer['denominator']

if __name__ == "__main__":
    main()
