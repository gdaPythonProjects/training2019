# https://pyformat.info/

a, b = 2, 7
s = a + b
print(a, b, s)
print("Suma " + str(a) + " + " + str(b) + " = " + str(s))
print("Suma ", str(a), " + ", str(b), " = ", str(s))

# classic (from C language)
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
print("Suma %d + %d = %d" % (a, b, s))
print("Suma %(value_a)d + %(value_b)d = %(suma)d"
      % {"value_a": a, "value_b": b, "suma": s})

# new style / python style
print("Suma {} + {} = {}".format(a, b, s))
print("Suma {value_a} + {value_b} = {sum}".
      format(value_a=a, value_b=b, sum=s))

# f-strings
print(f"Suma {a} + {b} = {s}")
