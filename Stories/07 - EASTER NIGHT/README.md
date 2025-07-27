# Easter Night
The story takes place on Easter night, a time traditionally associated with joy, renewal, and resurrection in the Orthodox Christian tradition. However, the mood of the story is deeply somber.  
It follows two men—the sacristan (sexton) and a schoolmaster—as they walk through a village cemetery after the Easter church service. The church is full of life, songs, and light, but the graveyard is dark and quiet. As they pass by the graves, they come upon a fresh grave: it belongs to Maria, a young and gentle woman who had recently died.  
The sexton recounts how Maria was deeply loved and known for her kindness. Her death has left a void, yet even on Easter—a day meant to celebrate life and resurrection—no one visits her grave. The schoolmaster is struck by this emotional contradiction: inside the church, people rejoice, but out here, death remains forgotten.

## Merge Audio Files with Pedalboard Effects

This Python script [merge_audio_folder.py](./merge_audio_folder.py) merges (concatenates) all `.wav` audio files from a specified folder (`audios/`) into a single output file, optionally applying audio effects using [Spotify's Pedalboard](https://github.com/spotify/pedalboard).

## Steps
- Loads all `.wav` files in the `audios/` folder
- Concatenates them in order
- Converts mono files to stereo automatically
- Applies effects like Gain using Pedalboard
- Prints duration of each file and total playback time
- Saves final output as `merged_output.wav`


# 🧪 What’s Next?
Convert .wav + Image → .mp4 (Audio + Visual)