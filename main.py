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
    subscription_key = '674c2a16cc18418fb514d1df71071490'
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


#  def get_suggestions ():
#      subscriptionKey = 'b47216ed1fca42f1bc0af85a35acf7b9'

#      host = 'api.microsofttranslator.com'
#      path = '/V2/Http.svc/Translate'

#      target = 'th-th'
#      text = "input"
#      params = '?to=' + target + '&text=' + urllib.parse.quote (text)

#      headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
#      conn = httplib.HTTPSConnection('api.microsofttranslator.com')
#      conn.requests.get(path + params, None, headers)
#      response = conn.getresponse ()
#      return response.read ()

# do something with app...
@app.route('/index')
def p1():
    return render_template('index.html')

if __name__ =='__main__' :
    app.run(debug=True)



