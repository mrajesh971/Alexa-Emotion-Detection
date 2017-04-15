import logging,time

from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement, context, audio, current_stream

app = Flask(__name__)
ask = Ask(app, "/")
logger = logging.getLogger()
logging.getLogger('flask_ask').setLevel(logging.INFO)


@ask.launch
def launch():
    card_title = 'Audio Example'
    time.sleep(1)
    text = 'Welcome to an Emotion automation ,Tell Your mood,I will play action based on your mood'
    prompt = ''
    time.sleep(1)
    return question(text).reprompt(prompt).simple_card(card_title, text)


@ask.intent('DemoIntent')
def demo():
    speech = "Playing a melody song to make your mood active"
    stream_url = 'https://archive.org/download/piano_by_maxmsp/beats107.mp3'
    return audio(speech).play(stream_url, offset=93000)


# 'ask audio_skil Play the sax
@ask.intent('SaxIntent')
def george_michael():
    speech = 'yeah i got it,Making you still more happier!'
    stream_url = 'https://ia800203.us.archive.org/27/items/CarelessWhisper_435/CarelessWhisper.ogg'
    return audio(speech).play(stream_url)

@ask.intent('AngIntent')
def Ang_me():
    speech = 'I will make you cool my pal here is the Joke,Team work is important; it helps to put the blame on someone else hahaha.'
    #speech = "rajesh,she is your heart"
    #stream_url = 'https://ia600300.us.archive.org/2/items/plpl011/plpl011_05-johnny_ripper-rain.mp3'
    return question(speech)

@ask.intent('TiredIntent')
def Tired_me():
    speech = 'I will make you Fantastic my dear'
    stream_url = 'https://ia600300.us.archive.org/2/items/plpl011/plpl011_05-johnny_ripper-rain.mp3'
    return audio(speech).play(stream_url)


@ask.intent('AMAZON.PauseIntent')
def pause():
    return audio('Paused the stream.').stop()


@ask.intent('AMAZON.ResumeIntent')
def resume():
    return audio('Resuming.').resume()

@ask.intent('AMAZON.StopIntent')
def stop():
    return audio('stopping').clear_queue(stop=True)



# optional callbacks
@ask.on_playback_started()
def started(offset, token):
    _infodump('STARTED Audio Stream at {} ms'.format(offset))
    _infodump('Stream holds the token {}'.format(token))
    _infodump('STARTED Audio stream from {}'.format(current_stream.url))


@ask.on_playback_stopped()
def stopped(offset, token):
    _infodump('STOPPED Audio Stream at {} ms'.format(offset))
    _infodump('Stream holds the token {}'.format(token))
    _infodump('Stream stopped playing from {}'.format(current_stream.url))


@ask.on_playback_nearly_finished()
def nearly_finished():
    _infodump('Stream nearly finished from {}'.format(current_stream.url))

@ask.on_playback_finished()
def stream_finished(token):
    _infodump('Playback has finished for stream with token {}'.format(token))

@ask.session_ended
def session_ended():
    return "{}", 200

def _infodump(obj, indent=2):
    msg = json.dumps(obj, indent=indent)
    logger.info(msg)


if __name__ == '__main__':
    app.run(debug=True)
