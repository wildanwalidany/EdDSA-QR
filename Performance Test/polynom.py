def polynomial_modulo(dividend, divisor):
    dividend_deg = len(dividend) - 1
    divisor_deg = len(divisor) - 1

    while dividend_deg >= divisor_deg:
        if divisor[0] == 0:
            break

        div = [0] * (dividend_deg - divisor_deg) + divisor
        quotient = dividend[dividend_deg] // div[0]
        div = [coeff * quotient for coeff in div]
        dividend = [dividend[i] ^ div[i] for i in range(len(dividend))]
        dividend_deg = len(dividend) - 1

    return dividend

# Example usage
m_prime = [1, 0, 1, 1, 0]  # Dividend polynomial
g = [1, 1, 0, 1]          # Divisor polynomial

r = polynomial_modulo(m_prime, g)
print("r(x) =", r)
