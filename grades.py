import random
random_num = random.randint(60,99)

print random_num


def grade(score):
    if score>89:
        print 'Score: ', random_num, 'Your grade is A'
    elif 79<score<90:
        print 'Score:', random_num, ' Your grade is B'
    elif 69<score<80:
        print 'Score:' , random_num, ' Your grade is C'
    elif 59<score<70:
        print 'Score: ', random_num, 'Your grade is D'


grade(random_num)
