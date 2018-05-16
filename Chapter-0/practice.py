from functools import partial 

def write_letter(to, msg, by):
    print('To {}, by {}, my message: {}'.format(to, by, msg))

# write_letter('mom', 'me', 'hi mom')

write_letter_mom = partial(write_letter, 'mom', by='me')

write_letter_mom('hey mom, live a great life!')
write_letter_mom('be cool')