#"The array you entered is of mixed type"
#"String: magical unicorns hello world"
#"Sum: 117.98"

l = ['magical unicorns',19,'hello',98.98,'world']

curr_type = type(l)
if curr_type is int:
    if curr_type is str:
        print "The array you entered if of mixed type."

        intList = [i for i in l if isinstance(i, int)]
        print intList

        strList = [i for i in l if isinstance(i, str)]
        print strList

    elif curr_type is int:
        print 'THe array you entered is of int type.'
        sum = 0
        for i in l:
            print sum+i

    elif curr_type is str:
        print 'The array you entered if of string type.'
        for i in l:
            print i
