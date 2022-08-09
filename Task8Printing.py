
formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "foour"))
print(formatter.format("true", "false", "false", "true"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"  
))