"""
[2015-05-11] Challenge #214 [Easy] Calculating the standard deviation
http://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/

Description

Standard deviation is one of the most basic measurments in statistics. For some collection of values (known as a "population" in statistics), it measures how dispersed those values are. If the standard deviation is high, it means that the values in the population are very spread out; if it's low, it means that the values are tightly clustered around the mean value.
For today's challenge, you will get a list of numbers as input which will serve as your statistical population, and you are then going to calculate the standard deviation of that population. There are statistical packages for many programming languages that can do this for you, but you are highly encouraged not to use them: the spirit of today's challenge is to implement the standard deviation function yourself.
The following steps describe how to calculate standard deviation for a collection of numbers. For this example, we will use the following values:
5 6 11 13 19 20 25 26 28 37
First, calculate the average (or mean) of all your values, which is defined as the sum of all the values divided by the total number of values in the population. For our example, the sum of the values is 190 and since there are 10 different values, the mean value is 190/10 = 19
Next, for each value in the population, calculate the difference between it and the mean value, and square that difference. So, in our example, the first value is 5 and the mean 19, so you calculate (5 - 19)2 which is equal to 196. For the second value (which is 6), you calculate (6 - 19)2 which is equal to 169, and so on.
Calculate the sum of all the values from the previous step. For our example, it will be equal to 196 + 169 + 64 + ... = 956.
Divide that sum by the number of values in your population. The result is known as the variance of the population, and is equal to the square of the standard deviation. For our example, the number of values in the population is 10, so the variance is equal to 956/10 = 95.6.
Finally, to get standard deviation, take the square root of the variance. For our example, sqrt(95.6) ≈ 9.7775.
Formal inputs & outputs

Input

The input will consist of a single line of numbers separated by spaces. The numbers will all be positive integers.
Output

Your output should consist of a single line with the standard deviation rounded off to at most 4 digits after the decimal point.
Sample inputs & outputs

Input 1

5 6 11 13 19 20 25 26 28 37
Output 1

9.7775
Input 2

37 81 86 91 97 108 109 112 112 114 115 117 121 123 141
Output 2

23.2908
Challenge inputs

Challenge input 1

266 344 375 399 409 433 436 440 449 476 502 504 530 584 587
Challenge input 2

809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373
Notes

For you statistics nerds out there, note that this is the population standard deviation, not the sample standard deviation. We are, after all, given the entire population and not just a sample.
If you have a suggestion for a future problem, head on over to /r/dailyprogrammer_ideas and let us know about it!
"""

# 1st implementation: clear, short, matches the problem definition
def standard_deviation_1(input_str):
    list = [int(s) for s in input_str.split()]
    count = len(list)
    avg = sum(list) / count
    variance = sum((n - avg)**2 for n in list) / count
    return variance**0.5

# 2nd implementation: 1 pass, O(1) memory usage
def standard_deviation(input_str):
    n_sum, n2_sum, count = 0, 0, 0
    for s in input_str.split():
        n = int(s)
        n_sum += n
        n2_sum += n*n
        count += 1
    if count == 0:
        return None
    avg = n_sum / count
    return (n2_sum/count - n_sum*n_sum/(count*count))**0.5

    
def tests():
    assert math.trunc(standard_deviation('5 6 11 13 19 20 25 26 28 37') * 10000.0) == 97775, 'Test 1'
    assert math.trunc(standard_deviation('37 81 86 91 97 108 109 112 112 114 115 117 121 123 141') * 10000.0) == 232908, 'Test 2'
    assert math.trunc(standard_deviation('266 344 375 399 409 433 436 440 449 476 502 504 530 584 587') * 10000.0) == 836615, 'Test 3'
    assert math.trunc(standard_deviation('809 816 833 849 851 961 976 1009 1069 1125 1161 1172 1178 1187 1208 1215 1229 1241 1260 1373') * 10000.0) == 1701272, 'Test 4'
    print('All tests passed')

if __name__ == '__main__':
    tests()

# Python 3.4 => import statistics; statistics.pstdev(list)
# Others => import numpy; numpy.std()

