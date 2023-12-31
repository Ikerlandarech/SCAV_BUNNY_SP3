# SCAV VIDEO SP3
### EXERCISE 1: Changing bbb RESOLUTION and CODECS:
With the following command we can convert the bbb original resolution to 1280x720, 640x480, 320x240 & 160x120:
```ruby
python3 sp3.py --convert_video_resolution
```
With the following command we can change the original bbb h264 codec to VP8, VP9, h265 & AV1:
```ruby
python3 sp3.py --convert_video_codec
```

### EXERCISE 2: Exporting 2 video comparison:
Finally we can export 2 video comparisons with 2 different codecs with the following command:
```ruby
python3 sp3.py --compare_videos CODEC1 CODEC2
```
For instance:
```ruby
python3 sp3.py --compare_videos vp8 vp9
python3 sp3.py --compare_videos h265 av1 
```


### EXERCISE 3: 🐰💕🦋 - Bunny GUI! - 🐰💕🦋:
This exercise is pure magic, by running the script ***BunnyGUI.py*** we will be able to talk with our well known Bunny friend. I've been working with him during the whole course and he is super friendly and loves to help me with ffmpeg commands, I know he looks kind of silly but he is an expert on that topic since he has been part of all our *input_videos* of our scripts, so he knows by heart all the ffmpeg commands that exist on the world. Please remember to not ask him about rufians, he has been having some problems with them lately since sadly they've been killing butterflies. We all love butterflies but our Bunny friend here is obsessed and loves them like nothing in the world so you can talk with him about them too. Don't be shy ask him all the questions you have on the subject.

*A demo has been provided via AulaGlobal.*

**Keep in mind:** This program would need a little more development, both in terms of reinforcement techniques to handle the behaviour of our friend, as the processing part, I have been working very hard on creating workers and threads with *QRunneable* to perform the processes that use the API in parallel to the frontend processes but I ended up not using them since they gave tons of operation errors.

**Installation:** *In order to run BunnyGUI.py we will need to have installed the OpenAI GPT-3 Python Library, FFMPEG and PyQt5. Please keep in mind that the API used in the script has been disabled to avoid being leaked online so in order to run this script the user will need to generate a new API key from the OpenAI page.*

*The dependencies can be installed by running the following commands:*
```ruby
pip install PyQt5
pip install openai
```

### EXERCISE 4: Docker:
Finally on this exercise I have simply created my first Dockerfile a build a container that contains FFMPEG to run a simple CMD command.

