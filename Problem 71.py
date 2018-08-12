# from fractions import Fraction
# for n in range(13,50):
#     answer = 0;
#     for x in range(3,n):
#         for y in range(1,x):
#             if Fraction(y,x) < Fraction(3,7):
#                 if Fraction(y,x) > answer:
#                     answer = Fraction(y,x);
#     print "n: " + str(n) + " Answer: " + str(answer);
answer = 2;
for n in range(7,1000001):
    if(n%7==6):
        answer+=3;
print "n: " + str(n) + " Answer: " + str(answer);

