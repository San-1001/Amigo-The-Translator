# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:17:58 2022

@author: Lenovo
"""

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import googletrans
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS



st.set_page_config(page_title="AMIGO - Your personal translator", page_icon="👨", layout="wide")

img_logo=Image.open("images/logo.png")
with st.container():
    st.image(img_logo)
    
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        



local_css("style/style.css")

lang=googletrans.LANGUAGES


# Creating Recogniser() class object
recog1 = spr.Recognizer()
 
# Creating microphone instance
mc = spr.Microphone()

pglang=st.sidebar.selectbox("Use AMIGO in your language", ['<select>', *lang.values()])
if pglang=='<select>':
    pglang='english'
mainlang=list(lang.keys())[list(lang.values()).index(pglang)]

def bonda(a):
    translator=Translator()
    fromtxt=translator.translate(a,src='en',dest=mainlang)
    prtxt=fromtxt.text
    st.write(prtxt)

def hdr(a):
    translator=Translator()
    fromtxt=translator.translate(a,src='en',dest=mainlang)
    prtxt=fromtxt.text
    st.header(prtxt)
    
    

with st.container():
    hdr("Translate from Audio")
    bonda("From:")
    from_lang_val=st.selectbox("From :",lang.values())
    from_lang=list(lang.keys())[list(lang.values()).index(from_lang_val)]
    bonda("To:")
    to_lang_val=st.selectbox("To :",lang.values())
    to_lang=list(lang.keys())[list(lang.values()).index(to_lang_val)]
    if st.button("Translate to audio"):
        with mc as source:
            translator=Translator()
            fromtxt=translator.translate("Speak 'AMIGO' to initiate the Translation !",src='en',dest=mainlang)
            prtxt=fromtxt.text
            st.write(prtxt)
            st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            recog1.adjust_for_ambient_noise(source, duration=0.2)
            audio = recog1.listen(source)
            MyText = recog1.recognize_google(audio)
            MyText = MyText.lower()
# Here initialising the recorder with
# hello, whatever after that hello it
# will recognise it.
        
        if 'amigo' in MyText:
            # Translator method for translation
            translator = Translator()
            
            try:
                with mc as source:
                    fromtxt=translator.translate("Speak a stentence...",src='en',dest=mainlang)
                    prtxt=fromtxt.text
                    st.write(prtxt)
                    recog1.adjust_for_ambient_noise(source, duration=0.2)
               # Storing the speech into audio variable
                    audio = recog1.listen(source)
                # Using recognize.google() method to
                # convert audio into text
                    get_sentence = recog1.recognize_google(audio)
                    
             
            # Printing Speech which need to
            # be translated.
                    bonda("Phase to be Translated :") 
                    st.write(get_sentence)
         
                    # Using translate() method which requires
                    # three arguments, 1st the sentence which
                    # needs to be translated 2nd source language
                    # and 3rd to which we need to translate in
                    text_to_translate = translator.translate(get_sentence,
                                                             src= from_lang,
                                                             dest= to_lang)
                     
                    # Storing the translated text in text
                    # variable
                    text = text_to_translate.text
                    st.write(text)
         
                    # Using Google-Text-to-Speech ie, gTTS() method
                    # to speak the translated text into the
                    # destination language which is stored in to_lang.
                    # Also, we have given 3rd argument as False because
                    # by default it speaks very slowly
                    speak = gTTS(text=text, lang=to_lang, slow= False)
         
                    # Using save() method to save the translated
                    # speech in capture_voice.mp3
                    speak.save("captured_voice.mp3")    
                    audio_file=open('captured_voice.mp3','rb')
                    audio_bytes=audio_file.read()
                    
                    st.audio(audio_bytes, format='audio/mp3')
                
            except spr.UnknownValueError:
                    bonda("Unable to Understand the Input")

            except spr.RequestError as e:
                    bonda("Unable to provide Required Output")+e
            
        else:
            st.empty()



with st.container():
    hdr("Translate from Text")
    from_lang_v=st.selectbox("From:",lang.values())
    from_langu=list(lang.keys())[list(lang.values()).index(from_lang_v)]
    to_lang_v=st.selectbox(
    "To:",
    lang.values())
    to_langu=list(lang.keys())[list(lang.values()).index(to_lang_v)]
    bonda("Enter text to be translated")
    fst_txt=st.text_input(" ")
    if st.button("Translate to text"):
            translator=Translator()
            fromtxt=translator.translate(fst_txt,src=from_langu,dest=to_langu)
            trans_txt=fromtxt.text
            st.write(trans_txt)
            speak = gTTS(text=trans_txt, lang=to_langu, slow= False)
            speak.save("captured_voice.mp3")    
            audio_file=open('captured_voice.mp3','rb')
            audio_bytes=audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            
            




lottie_coding=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_HjK9Ol.json")


    
with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        translator=Translator()
        hdr("Our Vision")
        st.write("##")
        bonda("We have created a personal translator for you!")
        bonda("- AMIGO- your personal translator")
        bonda("- AMIGO helps you to translate any language to any other language")
        bonda("- AMIGO has the best UI - Easily accessible - Could be used by a layman")
        bonda("- Both audio and text form of translation is provided by AMIGO")
        bonda("- Use AMIGO in your language")
        
        
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

img_allow=Image.open("images/allow.png")
img_to=Image.open("images/to.png")
img_from=Image.open("images/from.png")
img_translate=Image.open("images/translate.png")
img_final=Image.open("images/final.png")

with st.container():
    hdr("How to use AMIGO?")
    st.write("##")
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_allow)
    with text_column:
        bonda("Step 1: Make sure that you have allowed microphone access")

with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_from)
    with text_column:
        bonda("Step 2: Choose the language you need to translate")

with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_to)
    with text_column:
        bonda("Step 3: Choose the final language you need to translate into")

with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_translate)
    with text_column:
        bonda("Step 4: Click the 'Translate' button below")

with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_final)
    with text_column:
        bonda("Step 5: Say AMIGO! and move on! TADA!!🤩🤩")
        


with st.container():
    st.write("---")
    hdr("Get in touch with us")
    st.write("##")
    
    contact_form= """
    <form action="https://formsubmit.co/adhithyarengamani@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="mail" name="gmail" placeholder="Your email ID" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>"""

    
    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()