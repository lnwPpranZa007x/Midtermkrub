def q02():
    my_list02 = ['There', 'is', 11.22, 'no', 'such', True, 'thing', 3.1, 'like', 'magic', 2.25]

    # put your code here
    # Print the sentence of text element(s) in the above list (Ignore non-text elements)
    # output --> There is no such thing like magic
    # 3 points
    print('q02')

    my_list03 = []
    for x in my_list02:
        if isinstance(x, str):
            my_list03.append(x)
    print(my_list03)
    #print in sentence format
    output = ''
    for x in my_list03:
        output = output + x + ' '
    print(output)

    print('"' + my_list03[0] + ' ' + my_list03[1] + ' ' + my_list03[2] + ' ' + my_list03[3] + ' ' +my_list03[4] + ' ' +my_list03[5] + ' '+my_list03[6] + '".')