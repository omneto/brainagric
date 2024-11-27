
def validate_cpf(cpf):

    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    digit_count = firstValidation = secondValidation = False

    if len(numbers) == 11:
        digit_count = True
    
        sum_digits_one = sum(a*b for a, b in zip (numbers[0:9], range (10, 1, -1)))
        expected_digit_one = (sum_digits_one * 10 % 11) % 10
        if numbers[9] == expected_digit_one:
            firstValidation = True

        sum_digits_two = sum(a*b for a, b in zip(numbers [0:10], range (11, 1, -1)))
        expected_digit_two = (sum_digits_two *10 % 11) % 10
        if numbers[10] == expected_digit_two:
            secondValidation = True

        if digit_count == True and firstValidation == True and secondValidation == True:
            return True
        else:
            return False

    else:
        return False
    

def validate_cnpj(cnpj):

    numbers = [int(digit) for digit in cnpj if digit.isdigit()]

    digit_count = firstValidation = secondValidation = False

    if len(numbers) == 14:
        digit_count = True

        sum_digits_one = sum( a*b for a, b in zip (numbers[0:12], list(range(6,10)) + list(range(2, 10))) )
        expected_digit_one = (sum_digits_one % 11)
        if expected_digit_one > 9:
            expected_digit_one = 0

        if numbers[12] == expected_digit_one:
            firstValidation = True

        sum_digits_two = sum(a*b for a, b in zip(numbers[0:13], list(range(5,10)) + list(range(2, 10))) )
        expected_digit_two = (sum_digits_two % 11)
        if expected_digit_two > 9:
            expected_digit_two = 0

        if numbers[13] == expected_digit_two:
            secondValidation = True

        if digit_count == True and firstValidation == True and secondValidation == True:
            return True
        else:
            return False

    else:
        return False

