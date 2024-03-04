import moviepy.editor

video = moviepy.editor.VideoFileClip("//path to video ")

audio = video.audio
audio.write_audiofile("extractedsong.mp3")