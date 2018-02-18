from flask import Flask
import requests
from flask import Response
from flask import request
import json
import httplib , urllib
from ocp import *
from flask import Flask ,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)



@app.route('/result' ,methods=['GET'])
def hello_world():
    imageURL = request.args.get('imageURL')

    imageURL = str(imageURL)
    ocr_url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/ocr'
    #image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"
    subscription_key = 'Your_subscription_key'
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
    params   = {'language': 'unk', 'detectOrientation ': 'true'}
    data     = {'url': imageURL}
    response = requests.post(ocr_url, headers=headers, params=params, json=data)
    response.raise_for_status()

    analysis = response.json()
    #print analysis
    json_words = []
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)
    #print word_infos
    #word_info[0]['text']
    for x in word_infos :
        json_words.append(x[u'text'])
        

    
    js = json.dumps(json_words)

    return js



@app.route('/index')
def p1():
    return render_template('index.html')

if __name__ =='__main__' :
    app.run(debug=True)



