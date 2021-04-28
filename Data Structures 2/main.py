from sweepstakes import Sweepstake

#1a
months_of_the_year = (('January', 'February', 'March', 'April', 'May', 'June', 'July',
                       'August', 'September', 'October', 'November', 'December'))

month_with_pi_day = months_of_the_year[2]
print(month_with_pi_day)

#1b
birthday_locations = ['Croatia', 'Detroit', 'The Golf of Oman']

for locations in birthday_locations:
    print(locations)

#1c
contest = Sweepstake()
contest.add_contestants('Rick Sanchez')
contest.add_contestants('Morty Smith')
contest.add_contestants('Mr Me Seeks')
contest.add_contestants('Summer Smith')
contest.add_contestants('Jerry Smith')
contest.pick_contestant()
#2
family = [
    {
        'First name': 'Kailyn',
        'Last Name': 'Hubbard',
        'Relationship': 'Sister',
    },
    {
        'First name': 'Joslynn',
        'Last Name': 'Burrell',
        'Relationship': 'Mother',
    },
    {
        'First name': 'John',
        'Last Name': 'Alexander',
        'Relationship': 'Father',
    },
    {
        'First name': 'Leplesitt',
        'Last Name': 'Burrell',
        'Relationship': 'Step Father',
    }
]

print(family)
