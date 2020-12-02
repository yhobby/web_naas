from jinja2 import Environment, FileSystemLoader


def generator(template_name, data):
    env = Environment(loader=FileSystemLoader('dashboard/jinja2_templates/'))
    template = env.get_template(template_name)

    return template.render(data)


if __name__ == '__main__':
    test_data = {
        'bts': 'AL0000',
        'interface': 'GigabitEthernet0/0/0',
        'vlan_abis': '1703',
        'vlan_iub': '2703',
        'vlan_om': '3703',
        'vlan_s1c': '1303',
        'vlan_s1u': '2303',
        'vlan_x2': '3303',
        'ip_abis': '1.1.1.1',
        'ip_iub': '1.1.1.2',
        'ip_om': '1.1.1.3',
        'ip_s1c': '1.1.1.4',
        'ip_s1u': '1.1.1.5',
        'ip_x2': '1.1.1.6'
    }
    print(generator('bts_config.txt', test_data))