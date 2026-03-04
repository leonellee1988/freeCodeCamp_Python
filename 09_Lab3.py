# Build an RPG Character

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    elif name == '':
        return 'The character should have a name'
    
    elif len(name) > 10:
        return 'The character name is too long'
    
    elif ' ' in name:
        return 'The character name should not contain spaces'
    
    elif not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers'
    
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    
    elif (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    
    else:
    
        dot_stregth = full_dot*strength + empty_dot*(10 - strength)
        dot_intelligence = full_dot*intelligence + empty_dot*(10 - intelligence)
        dot_charisma = full_dot*charisma + empty_dot*(10 - charisma)
    
    return (f'{name}\n'
            f'STR {dot_stregth}\n'
            f'INT {dot_intelligence}\n'
            f'CHA {dot_charisma}')
    
print(create_character('ren', 4, 2, 1))