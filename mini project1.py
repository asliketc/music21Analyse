from music21 import *
import matplotlib.pyplot as plt 

def pitch_toMidi(pitchName):
    p=pitch.Pitch(pitchName)
    return p.midi
def sortPitches(pitches):
    return sorted(pitches, key=lambda x:pitch_toMidi(x))

try:
    score= converter.parse('/Users/macbook/Desktop/furelise_new.xml')
except Exception as e:
    print("Could not Load")
    raise e

composer=score.metadata.composer
title=score.metadata.title
print(f"Title: {title}")
print(f"Composer: {composer}")

#to access notes
flat_score=score.flatten()
offset=[]
pitches=[]
for n in flat_score.notes:
    if isinstance(n, note.Note):
        pitches.append(n.pitch.nameWithOctave)
        offset.append(n.offset)

#
pitches=sortPitches(pitches)
print(pitches)
pitches_midi=[]
plt.figure(figsize=(10,6))
plt.plot(offset,pitches,marker='o',linestyle='-',color='yellow')
plt.xlabel('Note Index')
plt.ylabel('MIDI PITCH')
plt.title('Melodic Contour')
for measure, pitch_mid in zip(offset, pitches):
    pitchname=note.Note(pitch_mid).nameWithOctave
    pitches_midi.append(note.Note(pitch_mid).pitch.midi)
    plt.text(measure, pitch_mid,pitchname, fontsize=9, ha="right")



y_ticks=pitches
y_labels=[note.Note(midi).nameWithOctave for midi in y_ticks]
plt.yticks(y_ticks,y_labels)
plt.show()