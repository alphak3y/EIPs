import json

def validate_eip_sections():
    eip_file = open('EIPS/eip-1559.md', 'r')
    eip_file_lines = eip_file.readlines()

    sections = [
                {'name':'Abstract', 'alternate_names': [], 'required': True},
                {'name':'Motivation', 'alternate_names': [], 'required': False},
                {'name':'Specification', 'alternate_names': [], 'required': True},
                {'name':'Rationale', 'alternate_names': [], 'required': False},
                {'name':'Backwards Compatibility', 'alternate_names': [], 'required': True},
                {'name':'Test Cases', 'alternate_names': [], 'required': True},
                {'name':'Reference Implementation', 'alternate_names': [], 'required': False},
                {'name':'Security Considerations', 'alternate_names': [], 'required': True},
                {'name':'Copyright Waiver', 'alternate_names': ['Copyright'], 'required': True}
               ]
            
    required_sections = 0
    for section in sections:
        if section['required']:
            required_sections +=1
    sections_found = []
    required_sections_found = 0
    section_ctr = 0

    for line in eip_file_lines:
        if line.startswith('## '):
            print(line[3:])
            print(section_ctr)
            print(line[3:])
            print(line[3:] in sections[section_ctr]['alternate_names'])
            print(sections[section_ctr]['alternate_names'])
            if line[3:].startswith(sections[section_ctr]['name']) or line[3:] in sections[section_ctr]['alternate_names']:
                sections_found.append(sections[section_ctr])
                section_ctr += 1
                if sections[section_ctr]['required']:
                    required_sections_found += 1
            elif sections[section_ctr]['required'] == False:
                if line[3:].startswith(sections[section_ctr+1]['name']):
                    sections_found.append(sections[section_ctr+1])
                    section_ctr += 2
            else:
                if sections[section_ctr]['required']:
                    for section in sections:
                        if line[3:] == section['name']:
                            print('invalid section order!')
    print('sections found: ')
    print(json.dumps(sections_found, indent=2))
    if required_sections_found < required_sections:
        print('missing required sections')
    else:
        print('eip passed section validation')
        

if __name__ == "__main__":
    validate_eip_sections()
    
