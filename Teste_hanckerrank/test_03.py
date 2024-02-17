# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

# Example
# The result of the integer division .
# The result of the float division is .

if __name__ == '__main__':
    
    a = int(input('Digite o primeiro numero:' ))
    b = int(input('Digite o segundo numero: '))
    
    integer_division = a // b

    float_division = a / b
    print("O resultado da divisão inteira é", integer_division)
    print(f"O resultado da divisão de ponto flutuante é, {float_division :.1f}")
