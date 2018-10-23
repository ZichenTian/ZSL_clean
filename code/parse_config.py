def parse_config(config_file):
    with open(config_file, 'rb') as f:
        lines = f.readlines()
    config_dict = {}
    for line in lines:
        if '#' in line:
            line = line.split('#')[0]
        if ':' in line:
            key, value = line.split(':')
            key, value = key.strip(), value.strip()
            config_dict[key] = value
    return config_dict

if __name__ == '__main__':
    pass
    #print parse_config('./config.proto')