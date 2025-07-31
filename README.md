## Acoustic Sigils

This project is inspired by Kevin Max Krebs' concept of developing complex electroacoustic sigils. Acoustic sigils are audio representations of statements of intent, created by converting alphabet letters into tones and combining them to form a sound composition.

### How It Works

1. **Generate Statement of Intent**: Start by generating a statement of intent, similar to traditional sigilization methods.

2. **Reduce the Statement**: Reduce the statement by removing duplicate letters.

3. **Design a Scale**: Assign each letter of the alphabet a corresponding frequency in hertz (cycles per second). This can be done arbitrarily or through personal experimentation.

4. **Convert Statement to Frequencies**: Using the designed scale, convert each letter in the reduced statement to its corresponding frequency.

5. **Generate Tones**: Use tone generation software (such as Wavegen v2.1) to create sine waves for each frequency. Set the amplitude as a percentage of the maximum amplitude (usually 7-8%) and a duration of one second.

6. **Combine Tones**: Combine the generated tones to create a complex tone using additive synthesis.

7. **Utilization**: The resulting audio can be used in various ways:

   - Play it as looped background audio.
   - Incorporate it into musical compositions.
   - Broadcast it.
   - Listen to it while sleeping, etc.

### Implementation

The provided Python script `acoustic_sigils.py` implements the process of generating acoustic sigils. It takes a statement of intent entered by the user, converts it into a pentatonic scale, and generates a corresponding audio file.

### Usage

You can freely use the tool at the following link: [Acoustic sigils](https://huggingface.co/spaces/cha0smagick/Acoustic_sigils)

1. Enter your statement of intent and adjust the playback speed if desired.

2. Click "Generate Sigil" to create your acoustic sigil.

### References

- Original concept by Kevin Max Krebs.
- [Link to the original discussion](https://zeebazu.com/docs/Acoustic-Sigils.txt)

### Author

Cha0smagick

