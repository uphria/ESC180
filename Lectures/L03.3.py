12323423423
12323424.0

123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457123234354643456363394857394857394857349857398457

# you can have really large ints! ... until it is so large it exceeds the memory of the computer

# unlike integers, floats are stored with a fixed number of digits
# a * 2^b
# a: mantissa
# b: exponent
# each has a limited number of digits available
10.0**400 # this is too large
10.0**308 # this is the limit (and -308)
# mantissa is also limited in number of digits with decimals
10**-100
10**-500 # returns 0