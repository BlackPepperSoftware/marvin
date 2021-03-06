import time
import random
import pickle
import os
from datetime import date

RANDOM_CHANNEL_ID = os.environ.get("MARVIN_SLACK_CHANNEL_ID")
FILE="plugins/animal.data"
ANIMALS = ['Adelie Penguin',
           'African Bush Elephant',
           'African Civet',
           'African Clawed Frog',
           'African Forest Elephant',
           'African Palm Civet',
           'African Penguin',
           'African Tree Toad',
           'African Wild Dog',
           'Albatross',
           'Aldabra Giant Tortoise',
           'Alligator',
           'Angelfish',
           'Ant',
           'Anteater',
           'Antelope',
           'Arctic Fox',
           'Arctic Hare',
           'Arctic Wolf',
           'Armadillo',
           'Asian Elephant',
           'Asian Giant Hornet',
           'Asian Palm Civet',
           'Asiatic Black Bear',
           'Avocet',
           'Axolotl',
           'Aye Aye',
           'Baboon',
           'Bactrian Camel',
           'Badger',
           'Banded Palm Civet',
           'Bandicoot',
           'Barn Owl',
           'Barnacle',
           'Barracuda',
           'Basking Shark',
           'Bat',
           'Bear',
           'Bearded Dragon',
           'Beaver',
           'Beetle',
           'Bengal Tiger',
           'Binturong',
           'Birds Of Paradise',
           'Bison',
           'Black Bear',
           'Black Rhinoceros',
           'Black Widow Spider',
           'Blue Whale',
           'Bobcat',
           'Bonobo',
           'Booby',
           'Bornean Orang-utan',
           'Borneo Elephant',
           'Bottle Nosed Dolphin',
           'Brown Bear',
           'Budgerigar',
           'Buffalo',
           'Bull Shark',
           'Bullfrog',
           'Bumble Bee',
           'Burrowing Frog',
           'Butterfly',
           'Butterfly Fish',
           'Caiman',
           'Caiman Lizard',
           'Camel',
           'Capybara',
           'Caracal',
           'Cassowary',
           'Caterpillar',
           'Catfish',
           'Centipede',
           'Chameleon',
           'Chamois',
           'Cheetah',
           'Chicken',
           'Chimpanzee',
           'Chinchilla',
           'Chinstrap Penguin',
           'Chipmunk',
           'Cichlid',
           'Clouded Leopard',
           'Clown Fish',
           'Coati',
           'Cockroach',
           'Collared Peccary',
           'Common Buzzard',
           'Common Frog',
           'Common Loon',
           'Common Toad',
           'Cottontop Tamarin',
           'Cougar',
           'Cow',
           'Coyote',
           'Crab',
           'Crab-Eating Macaque',
           'Crane',
           'Crested Penguin',
           'Crocodile',
           'Cross River Gorilla',
           'Cuscus',
           'Cuttlefish',
           'Darwin\'s Frog',
           'Deer',
           'Desert Tortoise',
           'Dhole',
           'Dingo',
           'Discus',
           'Dodo',
           'Dolphin',
           'Donkey',
           'Dormouse',
           'Dragonfly',
           'Drever',
           'Duck',
           'Dugong',
           'Dunker',
           'Dusky Dolphin',
           'Dwarf Crocodile',
           'Eagle',
           'Earwig',
           'Eastern Gorilla',
           'Eastern Lowland Gorilla',
           'Echidna',
           'Egyptian Mau',
           'Electric Eel',
           'Elephant',
           'Elephant Seal',
           'Elephant Shrew',
           'Emperor Penguin',
           'Emperor Tamarin',
           'Emu',
           'Falcon',
           'Fennec Fox',
           'Ferret',
           'Fin Whale',
           'Fire-Bellied Toad',
           'Fishing Cat',
           'Flamingo',
           'Flounder',
           'Flying Squirrel',
           'Fossa',
           'Fox',
           'Frigatebird',
           'Frilled Lizard',
           'Frog',
           'Fur Seal',
           'Galapagos Penguin',
           'Galapagos Tortoise',
           'Gar',
           'Gecko',
           'Gentoo Penguin',
           'Geoffroys Tamarin',
           'Gerbil',
           'Gharial',
           'Giant African Land Snail',
           'Giant Clam',
           'Giant Panda Bear',
           'Gibbon',
           'Gila Monster',
           'Giraffe',
           'Glass Lizard',
           'Glow Worm',
           'Goat',
           'Golden Lion Tamarin',
           'Golden Oriole',
           'Goose',
           'Gopher',
           'Gorilla',
           'Grasshopper',
           'Great White Shark',
           'Green Bee-Eater',
           'Grey Mouse Lemur',
           'Grey Reef Shark',
           'Grey Seal',
           'Grizzly Bear',
           'Grouse',
           'Guinea Fowl',
           'Guinea Pig',
           'Guppy',
           'Hammerhead Shark',
           'Hamster',
           'Hare',
           'Harrier',
           'Hedgehog',
           'Hercules Beetle',
           'Hermit Crab',
           'Heron',
           'Highland Cattle',
           'Hippopotamus',
           'Honey Bee',
           'Horn Shark',
           'Horned Frog',
           'Horse',
           'Horseshoe Crab',
           'Howler Monkey',
           'Human',
           'Humboldt Penguin',
           'Hummingbird',
           'Humpback Whale',
           'Hyena',
           'Ibis',
           'Iguana',
           'Impala',
           'Indian Elephant',
           'Indian Palm Squirrel',
           'Indian Rhinoceros',
           'Indian Star Tortoise',
           'Indochinese Tiger',
           'Indri',
           'Jackal',
           'Jaguar',
           'Japanese Chin',
           'Japanese Macaque',
           'Javan Rhinoceros',
           'Jellyfish',
           'Kakapo',
           'Kangaroo',
           'Keel Billed Toucan',
           'Killer Whale',
           'King Crab',
           'King Penguin',
           'Kingfisher',
           'Kiwi',
           'Koala',
           'Komodo Dragon',
           'Kudu',
           'Ladybird',
           'Leaf-Tailed Gecko',
           'Lemming',
           'Lemur',
           'Leopard',
           'Leopard Cat',
           'Leopard Seal',
           'Leopard Tortoise',
           'Liger',
           'Lion',
           'Lionfish',
           'Little Penguin',
           'Lizard',
           'Llama',
           'Lobster',
           'Long-Eared Owl',
           'Lynx',
           'Macaroni Penguin',
           'Macaw',
           'Magellanic Penguin',
           'Magpie',
           'Maine Coon',
           'Malayan Civet',
           'Malayan Tiger',
           'Manatee',
           'Mandrill',
           'Manta Ray',
           'Marine Toad',
           'Markhor',
           'Marsh Frog',
           'Masked Palm Civet',
           'Mayfly',
           'Meerkat',
           'Millipede',
           'Minke Whale',
           'Mole',
           'Mongoose',
           'Monitor Lizard',
           'Monkey',
           'Monte Iberia Eleuth',
           'Moorhen',
           'Moose',
           'Moray Eel',
           'Moth',
           'Mountain Gorilla',
           'Mountain Lion',
           'Mouse',
           'Mule',
           'Newt',
           'Nightingale',
           'Numbat',
           'Nurse Shark',
           'Ocelot',
           'Octopus',
           'Okapi',
           'Olm',
           'Opossum',
           'Orang-utan',
           'Ostrich',
           'Otter',
           'Oyster',
           'Pademelon',
           'Panther',
           'Parrot',
           'Patas Monkey',
           'Peacock',
           'Pelican',
           'Penguin',
           'Pheasant',
           'Pied Tamarin',
           'Pig',
           'Pika',
           'Pike',
           'Pink Fairy Armadillo',
           'Piranha',
           'Platypus',
           'Poison Dart Frog',
           'Polar Bear',
           'Pond Skater',
           'Poodle',
           'Pool Frog',
           'Porcupine',
           'Possum',
           'Prawn',
           'Proboscis Monkey',
           'Puffer Fish',
           'Puffin',
           'Puma',
           'Purple Emperor',
           'Puss Moth',
           'Pygmy Hippopotamus',
           'Pygmy Marmoset',
           'Quail',
           'Quetzal',
           'Quokka',
           'Quoll',
           'Rabbit',
           'Raccoon',
           'Radiated Tortoise',
           'Rat',
           'Rattlesnake',
           'Red Knee Tarantula',
           'Red Panda',
           'Red Wolf',
           'Red-handed Tamarin',
           'Reindeer',
           'Rhinoceros',
           'River Dolphin',
           'River Turtle',
           'Robin',
           'Rock Hyrax',
           'Rockhopper Penguin',
           'Roseate Spoonbill',
           'Royal Penguin',
           'Sabre-Toothed Tiger',
           'Salamander',
           'Sand Lizard',
           'Saola',
           'Scorpion',
           'Scorpion Fish',
           'Sea Dragon',
           'Sea Lion',
           'Sea Otter',
           'Sea Slug',
           'Sea Squirt',
           'Sea Turtle',
           'Sea Urchin',
           'Seahorse',
           'Seal',
           'Serval',
           'Sheep',
           'Shrimp',
           'Siamese Fighting Fish',
           'Siberian Tiger',
           'Skunk',
           'Sloth',
           'Slow Worm',
           'Snail',
           'Snake',
           'Snapping Turtle',
           'Snowshoe',
           'Snowy Owl',
           'South China Tiger',
           'Spadefoot Toad',
           'Sparrow',
           'Spectacled Bear',
           'Sperm Whale',
           'Spider Monkey',
           'Spiny Dogfish',
           'Sponge',
           'Squid',
           'Squirrel',
           'Squirrel Monkey',
           'Sri Lankan Elephant',
           'Stag Beetle',
           'Starfish',
           'Stellers Sea Cow',
           'Stick Insect',
           'Stingray',
           'Stoat',
           'Striped Rocket Frog',
           'Sumatran Elephant',
           'Sumatran Orang-utan',
           'Sumatran Rhinoceros',
           'Sumatran Tiger',
           'Sun Bear',
           'Swan',
           'Tang',
           'Tapir',
           'Tarsier',
           'Tasmanian Devil',
           'Tawny Owl',
           'Termite',
           'Tetra',
           'Thorny Devil',
           'Tiger',
           'Tiger Salamander',
           'Tiger Shark',
           'Tortoise',
           'Toucan',
           'Tree Frog',
           'Tropicbird',
           'Tuatara',
           'Turkey',
           'Uakari',
           'Uguisu',
           'Umbrellabird',
           'Vampire Bat',
           'Vervet Monkey',
           'Vulture',
           'Wallaby',
           'Walrus',
           'Warthog',
           'Wasp',
           'Water Buffalo',
           'Water Dragon',
           'Water Vole',
           'Weasel',
           'Western Gorilla',
           'Western Lowland Gorilla',
           'Whale Shark',
           'White Faced Capuchin',
           'White Rhinoceros',
           'White Tiger',
           'Wild Boar',
           'Wildebeest',
           'Wolf',
           'Wolverine',
           'Wombat',
           'Woodlouse',
           'Woodpecker',
           'Woolly Monkey',
           'Wrasse',
           'X-Ray Tetra',
           'Yak',
           'Yellow-Eyed Penguin',
           'Yorkshire Terrier',
           'Zebra',
           'Zebra Shark',
           'Zebu',
           'Zonkey',
           'Zorse']

crontable = []
outputs = []

def process_message(data):
    if "text" in data:
        text = data["text"]
        channel = data["channel"]
        if channel.startswith(RANDOM_CHANNEL_ID) or channel.startswith("D"):
            if "animal" in text:
                _,weekNumber,_ = date.today().isocalendar()

                if os.path.isfile(FILE):
                    aow = pickle.load(open(FILE, 'rb'))
                else:
                    aow = update_aow(weekNumber, '')

                if aow[0] != weekNumber:
                    aow = update_aow(weekNumber, aow[1])

                response_text = 'The animal of the week is \"{0}\"'.format(aow[1])
                outputs.append([channel, response_text])


def update_aow(weekNumber, old_animal):
    aow = (weekNumber, random_animal(old_animal))
    pickle.dump(aow, open(FILE, 'wb'))
    return aow

def random_animal(old_animal) :
    new_animal = old_animal
    while old_animal == new_animal:
        new_animal = random.choice(ANIMALS)
    return new_animal
