from configparser import ConfigParser

config = ConfigParser()

config['settings'] = {
    'hotkey': 'alt+c',
    'bgcolor': '#3764ab'
}

with open('./config.ini', 'w') as f:
      config.write(f)