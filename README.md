# **Bitcoin Keys**

#### Key generation from scratch with no external dependencies.

Bitcoin uses the ECDSA algorithm with [**Secp256k1**](http://www.secg.org/sec2-v2.pdf) which specifies the elliptic curve E domain parameters T over finite field F<sub>p</sub>


![alt text](img/eqn1.svg)

![alt text](img/eqn2.svg)

Visualising the curve over the real numbers and using coordinate geometry, we can derive expressions for point addition and point doubling:

![alt text](img/eqn3.svg)

where for point addition:

![alt text](img/eqn21.svg)

and for point doubling by differenting E at point (x<sub>p</sub>, y<sub>p</sub>):

![alt text](img/eqn22.svg)

Using the extended Euclidean algorithm to compute modular inverses:
```
   t := 0;     newt := 1
   r := n;     newr := a

   while newr ≠ 0 do
       quotient := r div newr
       (t, newt) := (newt, t − quotient × newt)
       (r, newr) := (newr, r − quotient × newr)

   if r > 1 then
       return "a is not invertible"
   if t < 0 then
       t := t + n

   return t
```
We can now calculate the resulting public key K from a randomly generated private key k (where K = k*G), using the double-and-add method to efficiently traverse the curve:
```
let bits = bit_representation(s) # the vector of bits (from MSB to LSB) representing s
let res = O # point at infinity
for bit in bits:
    res = res + res # double
    if bit == 1:
        res = res + P # add
    i = i - 1
return res
```

Running the program with test private key k:\
**k = 1E99423A4ED27608A15A2616A2B0E9E52CED330AC530EDCC32C8FFC6A526AEDD**

we get uncompressed public key K:\
**K = 04f028892bad7ed57d2fb57bf33081d5cfcf6f9ed3d3d7f159c2e2fff579dc341a7cf33da18bd734c600b96a72bbc4749d5141c90ec8ac328ae52ddfe2e505bdb**
