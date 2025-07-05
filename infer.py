from dp.phonemizer import Phonemizer

phonemizer = Phonemizer.from_checkpoint('models/en_us_cmudict_forward.pt')
input_string = 'Phonemizing an English text is imposimpable!'
phonemes = phonemizer(input_string, lang='en_us')
print(input_string)
print(phonemes)
