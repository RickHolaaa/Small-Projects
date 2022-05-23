# Work only when the youtube video have a subtitle option

# Option : try with different API (like LyricsGenius, ...)

from youtube_transcript_api import YouTubeTranscriptApi
video = input("Enter your youtube video url")
lg = input("Enter your language (en for english, fr for french, ...)")
lang = [str(lg),'cn']
print(video[32:43])
srt = YouTubeTranscriptApi().get_transcript(str(video[32:43]),languages=lang)
for i in range(len(srt)):
    print(srt[i]['text'])

