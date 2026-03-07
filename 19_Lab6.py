# Build a User Configuration Manager

def add_setting(setting_dict, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()

    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting_dict, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()

    if key in setting_dict:
        setting_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting_dic, key):
    key = key.lower()

    if key in setting_dic:
        setting_dic.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
    
def view_settings(setting_dic):
    if len(setting_dic) == 0:
        return f"No settings available."
    else:
        result = "Current User Settings:\n"
        for key, value in setting_dic.items():
            result += f"{key.capitalize()}: {value}\n"
        return result

test_settings = {}

# Adding settings 1:
add_setting(test_settings, ('Kernel', 'Linux'))
add_setting(test_settings, ('Distribution', 'Mint'))
add_setting(test_settings, ('Distribution', 'Fedora'))
add_setting(test_settings, ('Computer', 'Dell'))

# Updating settings 1:
update_setting(test_settings, ('Computer', 'Toshiba'))
update_setting(test_settings, ('Computer', 'Fedora'))
update_setting(test_settings, ('RAM memory', '16GB'))

# Adding settings 2:
add_setting(test_settings, ('RAM Memory', '16GB'))
add_setting(test_settings, ('Hard Disk', '500GB'))
add_setting(test_settings, ('Computer Color', 'Gray'))
add_setting(test_settings, ('Computer Size', '50x30cm'))

# Deliting settings 1:
delete_setting(test_settings, 'Items')
delete_setting(test_settings, 'Computer Size')
delete_setting(test_settings, 'Computer Color')

print(view_settings(test_settings))