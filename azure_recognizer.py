import os
import json
import requests
import sys

API_KEY = '68f60404ffe0414aad2f9abbf980f641'
ENDPOINT = 'https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/ocr'
DIR = sys.argv[1]

def handler():
    text = ''
    for filename in os.listdir(DIR):
        index_of_ = filename.find('_')
        index_of_dot = filename.find(".")
        new_filename = ""
        version = 1
        if index_of_ > -1:
            new_filename = filename[0:index_of_]
            version = filename[index_of_ + 1: index_of_dot]
        else:
            new_filename = filename[0:index_of_dot]
        pathToImage = '{0}\{1}'.format(DIR, filename)
        results = get_text(pathToImage)
        text += "Version:" + str(version) +";Original:" + new_filename + ";Recognized:" + parse_text(results) + "\n"
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)

def parse_text(results):
    text = ''
    for region in results['regions']:
        for line in region['lines']:
            for word in line['words']:
                text += word['text'] + ' '
    return text  

def get_text(pathToImage):
    print('Processing: ' + pathToImage)
    headers  = {
        'Ocp-Apim-Subscription-Key': API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    
    payload = open(pathToImage, 'rb').read()
    response = requests.post(ENDPOINT, headers=headers, data=payload)
    results = json.loads(response.content)
    return results

if __name__ == '__main__':
    handler()