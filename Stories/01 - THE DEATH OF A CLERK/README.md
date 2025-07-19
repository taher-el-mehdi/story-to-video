# 🎥 THE DEATH OF A CLERK

This folder contains the assets and documentation with Breakdown for turning *Anton Chekhov’s* short story *“The Death of a Government Clerk”* into a narrated and illustrated video.

## 📜 Story Summary
A minor government clerk sneezes on a general and spirals into shame and over-apology, ultimately leading to his death. A tragicomic tale of status, anxiety, and invisibility.

📖 Original story: https://sites.google.com/view/short-stories-of-anton-chekhov/the-death-of-a-government-clerk

## 🛠️ Steps Followed
### 🎙️ Narration
- **Tool**: [OpenAI Text-to-Speech](https://www.openai.fm)
- **Voice**: *Sage* (Tone: Friendly – ideal for Chekhov’s calm and ironic style)
- **Output**: multiple audio files – [[`1.wav`](./audios/1.wav), [`2.wav`](./audios/2.wav),[...](./audios/)]

### 🖼️ Visuals
- **Tool**: [Microsoft Copilot – Create](https://m365.cloud.microsoft)
- **Method**:  
  - Described key scenes: the sneeze, the apologies, the despair at home.
  - Generated unique AI visuals for each scene.
- **Output**: multiple visuals files –[[`1.png`](./visuals/1.png), [`2.png`](./visuals/2.png),[...](./visuals/)]

### 🎞️ Video Editing
- **Tool**: [Microsoft Clipchamp](https://clipchamp.com)
- **Method**:
  - Imported narration and visuals.
  - Used Clipchamp’s AI for:
    - Auto subtitles
    - Scene transitions
    - Timing alignment with voice

### 🔗 Output
📺 Watch the video on [Youtube](https://www.youtube.com/watch?v=nH1JMmy4wKI&t=4s)

---


## 🧪 What’s Next?
- Automate narration with a CLI tool
→ [openai](https://www.openai.fm) only allows 999 characters per request, so I plan to build a script that splits the text and generates all `.wav` files automatically — saving time and avoiding manual steps.