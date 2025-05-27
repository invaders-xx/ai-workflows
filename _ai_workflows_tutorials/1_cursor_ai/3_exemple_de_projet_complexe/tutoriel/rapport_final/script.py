import os
import re

def get_section_number(filename):
    # Extrait le numéro de section du nom de fichier
    match = re.search(r'6_section_(\d+)_', filename)
    return int(match.group(1)) if match else float('inf')

def aggregate_files():
    # Chemin des répertoires
    input_dir = '../contenu_généré'
    output_file = 'rapport.md'
    
    # Liste tous les fichiers markdown qui correspondent au pattern
    files = [f for f in os.listdir(input_dir) if f.startswith('6_section_') and f.endswith('.md')]
    
    # Trie les fichiers par numéro de section
    files.sort(key=get_section_number)
    
    # Agrège le contenu dans le fichier de sortie
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, filename in enumerate(files):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                # Ajoute une ligne vide entre les sections, sauf après la dernière
                if i < len(files) - 1:
                    outfile.write('\n\n')

if __name__ == '__main__':
    aggregate_files()