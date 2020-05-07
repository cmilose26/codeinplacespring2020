"""
See the Animal Association section handout
"""


def main():
    print_intro()
    # Your solution goes here


def print_intro(is_phase_1):
    if is_phase_1:
        print('Association test, standard')
    else:
        print('Association test, flipped')
    print('You will be asked to answer three questions.')
    print('You should associate animals as follows:')
    print('puppy', get_association('puppy', is_phase_1))
    print('panda', get_association('panda', is_phase_1))
    print('spider', get_association('spider', is_phase_1))
    print('bat', get_association('bat', is_phase_1))
    input('Press enter to start... ')

def random_animal():
    return random.choice(['puppy', 'panda', 'spider', 'bat'])

def get_association(animal, is_phase_1):
    if animal == 'puppy' or animal == 'panda':
        return 'cute'
    if animal == 'bat' or animal == 'spider':
        return 'scary'