test_settings = {
    'brightness' : 'high'
}

def add_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings.keys():
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return f"No settings available."
    
    string = "Current User Settings:\n"
    for key, value in settings.items():
        string += f"{key.capitalize()}: {value}\n"

    return string


print(delete_setting({'theme': 'light'}, 'theme'))