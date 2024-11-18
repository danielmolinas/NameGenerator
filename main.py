import random
from collections import defaultdict, Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example Names
male_names = """
Liam
Noah
Oliver
James
Elijah
Mateo
Theodore
Henry
Lucas
William
Benjamin
Levi
Josiah
Charles
Christopher
Isaiah
Nolan
Cameron
Nathan
Joshua
Kai
Waylon
Angel
Lincoln
Andrew
Roman
Adrian
Aaron
Wesley
Ian
Thiago
Axel
Brooks
Bennett
Weston
Rowan
Christian
Sebastian
Jack
Ezra
Michael
Daniel
Leo
Owen
Samuel
Hudson
Alexander
Asher
Luca
Ethan
John
David
Jackson
Joseph
Mason
Luke
Matthew
Julian
Dylan
Elias
Jacob
Maverick
Gabriel
Logan
Aiden
Thomas
Isaac
Miles
Grayson
Santiago
Anthony
Wyatt
Carter
Jayden
Ezekiel
Caleb
Cooper
"""

female_names = """
Olivia
Emma
Charlotte
Amelia
Sophia
Mia
Isabella
Ava
Evelyn
Luna
Harper
Sofia
Camila
Eleanor
Elizabeth
Violet
Scarlett
Emily
Hazel
Lily
Elena
Hannah
Valentina
Maya
Zoey
Delilah
Leah
Lainey
Lillian
Paisley
Genesis
Madelyn
Sadie
Sophie
Leilani
Addison
Natalie
Josephine
Alice
Ruby
Claire
Kinsley
Everly
Emery
Adeline
Kennedy
Maeve
Audrey
Autumn
Athena
Eden
Gianna
Aurora
Penelope
Aria
Nora
Chloe
Ellie
Mila
Avery
Layla
Abigail
Ella
Isla
Eliana
Nova
Madison
Zoe
Ivy
Grace
Lucy
Willow
Emilia
Riley
Naomi
Victoria
Stella
"""

unisex_names = """
Lowen
Arbor
Everest
Onyx
Ridley
Tatum
Wren
Ellis
Zephyr
Royal
Azriel
Ira
Sage
Blake
Ash
Jett
Robin
Spencer
Marlowe
Phoenix
Sutton
Shiloh
Koda
Amari
Artemis
Scout
Basil
Rory
Vesper
Lux
River
"""

# Combine all names into a single dataset
all_names = male_names + "\n" + female_names + "\n" + unisex_names

# Convert names into a list
all_names_list = all_names.strip().split("\n")

# Create a Markov chain transition matrix
transition_matrix = defaultdict(Counter)

for name in all_names_list:
    for i in range(len(name) - 1):
        transition_matrix[name[i]][name[i + 1]] += 1

# Generate a name based on the transition matrix
def generate_name(prompt='', num_names=1, max_length=6):
    random.seed(prompt + str(random.random())) 
    names = []
    for _ in range(num_names):
        name = [random.choice(list(transition_matrix.keys()))]
        while len(name) < max_length:
            next_char_options = list(transition_matrix[name[-1]].elements())
            if not next_char_options:
                break
            next_char = random.choice(next_char_options)
            name.append(next_char)
        full_name = "".join(name)
        # Capitalize only the first letter and convert the rest to lowercase
        formatted_name = full_name.capitalize()
        names.append(formatted_name)
    return names

@app.route('/generate_names', methods=['POST'])
def generate_names():
    data = request.get_json()

    prompt = data.get('prompt', '')
    number_of_options = data.get('number_of_options', 1)
    name_type = data.get('name_type', 'random')

    if name_type == 'male':
        name_data = male_names
    elif name_type == 'female':
        name_data = female_names
    elif name_type == 'unisex':
        name_data = unisex_names
    else:
        name_data = all_names

    # Generate names using the Markov Chain model
    name_options = generate_name(prompt=prompt, num_names=number_of_options, max_length=6)

    response = {
        'prompt': prompt,
        'number_of_options': number_of_options,
        'name_type': name_type,
        'names': name_options
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
