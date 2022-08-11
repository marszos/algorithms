# Cracking the coding intervew | Bit manipulation | Debbuger: Exalpain what the follwoing code does? 
((n & (n-1)) == 0)


It returns 0 if n is a power of 2 (NB: only works for n > 0). So you can test for a power of 2 like this:


bool isPowerOfTwo(int n)
{
    return (n > 0) && ((n & (n - 1)) == 0);
}
