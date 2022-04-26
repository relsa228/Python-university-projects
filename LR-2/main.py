from work_modules.yaml_serialize_module import YamlSerializer
from work_modules.toml_serialize_module import TomlSerializer


trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_toml = {'trunk': trunk_template, 'access': access_template}

ts = TomlSerializer()
print(ts.dumps(to_toml))
print(ts.loads(ts.dumps(to_toml)))

ts.dump(to_toml, "jcd.toml")
print(ts.load("jcd.toml"))
