print "I will now count my chickens:"

print "Hens", 25+30/6
print "Roosters", 100-25*3%4

print "Now I will count the eggs:"

print 3+2+1-5+4%2-1/4+6
# Note, the above treats everyting as integers, so the total in the end is off
# Try this to force the use of floats:
print 3+2+1-5+4%2-1.0/4+6 # worked
# This?
print 3+2+1-5+4%2-1/4+6.0 # failed
# forced the whole result to a float, but incorrect because the fraction was not made a float
# This?
print 3.0+2+1-5+4%2-1/4+6 # same

print "Is it true that 3+2<5-7?"

print 3+2<5-7

print "What is 3+2?", 3+2
print "What is 5-7?", 5-7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5>-2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5<=-2
