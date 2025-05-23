import logging
from session import Session
from exercise import Exercise
from exercise_group import Exercise_Group

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s|%(name)s|%(levelname)s|%(message)s",
    handlers=[logging.FileHandler("data/piano.log")],
)


# warm-ups
warm_ups = Exercise_Group("Warm Ups", [Exercise("Stretch"), Exercise("Rock")])

# exercises
default_keys = [
    "C",
    "G",
    "D",
    "A",
    "E",
    "F",
    "Bb",
    "Am",
    "Dm",
    "Em",
    "Gm",
]
scales_and_chords = {
    "Expanded Scale": ["C", "G", "Am", "Dm"],
    "Four Octave Scale": default_keys,
    "Arpeggio": default_keys,
    "Chromatic Scale": ["D", "Ab"],
    "Triads": default_keys,
    "Broken Chords": default_keys,
    "Broken Triads": default_keys,
    "Running": ["C", "G", "D", "A", "F", "Bb", "E"],
}

scale_exercises = []
for ex, keys in scales_and_chords.items():
    scale_exercises.append(Exercise(f"{ex} ({', '.join(keys)})"))
scales_group = Exercise_Group("Scales and Chords", scale_exercises)

# dozen
book = "Book 2"
# dozen_ex = ["2-12", "3-1", "3-2", "3-3", "3-4"]
# dozen_ex = ["3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-10", "3-11", "3-12"]
# dozen_ex = ["4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7", "4-8", "4-9", "4-10", "4-11", "4-12"]
dozen_ex = ["5-1"]
dozen_exercises = []
for ex in dozen_ex:
    dozen_exercises.append(Exercise(f"{book} {ex}"))
dozen_group = Exercise_Group("Daily Dozen", dozen_exercises)

# songs
songs = [
    "Easy Piano Classics - Sonatina (Op 36, No 1), Clementi (p60)",
]
song_ex = [Exercise(song) for song in songs]
song_group = Exercise_Group("Songs", song_ex)

# repetoire
repetoire = [
    "Easy Piano Classics - Gavotte, Telemann (p13)",
    "Easy Piano Classics - Minuet in G Major, Bach (p24)",
    "Easy Piano Classics - Minuet in F Major, Haydn (p42)",
    "Easy Piano Classics - Ecossaise in G, Beethoven (p53)",
    "Easy Piano Classics - Soldier's March, Schumann (p72)",
    "Easy Piano Classics - Ballade, Burgmuller (p88)",
    "Easy Piano Classics - Nocturne (Op 9, No 2), Chopin (p148)",
    "Jazzin Americana - Super Stomp Rag (p2)",
    "Jazzin Americana - In the Hall of the Jazz Kings (p4)",
    "Jazzin Americana - Practice the Piano Blues (p6)",
    "Jazzin Americana - Bird in the Bebop (p12)",
    "Jazzin Americana - California Cool (p14)",
    "Jazzin Americana - Battle in Carnegie Hall (p18)",
    "Joy of Piano - Clair De Lune, Debussy (p20)",
]
repetoire_ex = [Exercise(rep) for rep in repetoire]
repetoire_group = Exercise_Group("Repetoire Review", repetoire_ex)

my_session = Session([warm_ups, scales_group, dozen_group, song_group, repetoire_group])
my_session.run_session()

