# [Description](https://redd.it/5aemnn)

In [mathematics](https://en.wikipedia.org/wiki/Mathematics), a [Kaprekar
number](https://en.wikipedia.org/wiki/Kaprekar_number) for a given
[base](https://en.wikipedia.org/wiki/Base_(exponentiation)) is a [non-
negative](https://en.wikipedia.org/wiki/Non-negative)
[integer](https://en.wikipedia.org/wiki/Integer), the representation of whose
square in that base can be split into two parts that add up to the original
number again. For instance, `45` is a Kaprekar number, because `452 = 2025` and
`20 + 25 = 45`. The Kaprekar numbers are named after [D. R.
Kaprekar](https://en.wikipedia.org/wiki/D._R._Kaprekar).

I was introduced to this after the recent [Kaprekar constant
challenge](https://redd.it/56tbds).

For the main challenge we'll only focus on base 10 numbers. For a bonus, see if
you can make it work in arbitrary bases.

###Input Description

Your program will receive two integers per line telling you the start and end of 
the range to scan, inclusively. Example:

	1 50

### Output Description

Your program should emit the Kaprekar numbers in that range. From our example:

	45

### Challenge Input

	2 100
	101 9000

### Challenge Output

Updated the output as per [this comment](https://goo.gl/2D8tHo)

	9 45 55 99 297
	703 999 2223 2728 4879 5050 5292 7272 7777