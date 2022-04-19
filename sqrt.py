def sqrt(x):
    # Babylonian method 
    if x <= 1:
        return x 
    else:
        x_n = 0.5 * x
        change = 1 
        
        while change > 0.01:
            next_n = 0.5 * (x_n + x/x_n)
            change = abs(x_n - next_n)
            x_n = next_n
    
    return (int(x_n))
