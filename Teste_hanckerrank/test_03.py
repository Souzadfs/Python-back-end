# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

# Example
# The result of the integer division .
# The result of the float division is .

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    r = a / b

    if r % 2 == 0 and r % 2 != 0:
       print(r)    
print(f'{r:.1f}')
print(f'{r:.1f}')   