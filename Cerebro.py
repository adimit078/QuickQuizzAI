#Imports
import cv2 as cv
import numpy as np
import pytesseract
import requests
import gradio as gr
import openai
import random
import re

'''
This file preprocces an image using various OpenCV techniques and runs it through an Optical Character Recognition tool called Python-tesseract to convert the image to text.
'''

#Main Function
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

#Convert to Grayscale
def get_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def resize(image):
    return  cv.resize(img, (560, 900))

openai.api_key = "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"

#text = ocr_core(gray)

def openai_chat(input_prompt):
    
    template = """
    Sentence: India won the 1983 Cricket World Cup which was the 3rd edition of the Cricket World Cup tournament.
    Question: Who won the 1983 Cricket World Cup ______ ? Answer: India
    Sentence: Google was founded on September 4, 1998, by Larry Page and Sergey Brin.
    Question: In which year was Google founded ______? Answer: 1998
    """

    input_prompt = "Sentence: " + input_prompt
    prompt = template + input_prompt

    completion = openai.Completion.create(engine="davinci", 
                                      prompt=prompt, 
                                      max_tokens=64, 
                                      temperature=0.7)

    message = completion.choices[0].text
    output_list = message.split("\n")
    out_index = []
    for idx, sentence in enumerate(output_list):
        if "Question" in sentence:
            out_index.append(idx)
    
    if out_index:
        return output_list[min(out_index)]
    
def select_random_full_sentence(text):
    # Use regular expressions to split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Remove empty sentences and fragments (if any)
    full_sentences = [sentence.strip() for sentence in sentences if sentence.strip() and re.search(r'[.!?]$', sentence)]

    # Randomly select a full sentence
    if full_sentences:
        selected_sentence = random.choice(full_sentences)
        return selected_sentence
    else:
        return None
    
def main(img):
    text = ocr_core(get_grayscale(img))
    selected_sentence = select_random_full_sentence(text)
    finalOutput = openai_chat(selected_sentence)
    print(finalOutput)
    return(finalOutput)


iface = gr.Interface(
    fn=main,  # Use the OCR function
    inputs="image",
    outputs="text",
    live=True,
    title="Effortlessly reinforce your reading with AI-driven quizzes.",
    description="Upload a picture of your textbook page, or a screenshot of your online reading.",
    allow_flagging = "never"
)

# Run the Gradio interface
iface.launch()