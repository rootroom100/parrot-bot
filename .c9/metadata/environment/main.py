{"filter":false,"title":"main.py","tooltip":"/main.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":3,"column":0},"end":{"row":63,"column":0},"action":"insert","lines":["","","# インポートするライブラリ","from flask import Flask, request, abort","","from linebot import (","    LineBotApi, WebhookHandler",")","from linebot.exceptions import (","    InvalidSignatureError",")","from linebot.models import (","    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction",")","import os","","# 軽量なウェブアプリケーションフレームワーク:Flask","app = Flask(__name__)","","","#環境変数からLINE Access Tokenを設定","LINE_CHANNEL_ACCESS_TOKEN = os.environ[\"LINE_CHANNEL_ACCESS_TOKEN\"]","#環境変数からLINE Channel Secretを設定","LINE_CHANNEL_SECRET = os.environ[\"LINE_CHANNEL_SECRET\"]","","line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)","handler = WebhookHandler(LINE_CHANNEL_SECRET)","","@app.route(\"/callback\", methods=['POST'])","def callback():","    # get X-Line-Signature header value","    signature = request.headers['X-Line-Signature']","","    # get request body as text","    body = request.get_data(as_text=True)","    app.logger.info(\"Request body: \" + body)","","    # handle webhook body","    try:","        handler.handle(body, signature)","    except InvalidSignatureError:","        abort(400)","","    return 'OK'","","# MessageEvent","@handler.add(MessageEvent, message=TextMessage)","def handle_message(event):","\tline_bot_api.reply_message(","        event.reply_token,","        TextSendMessage(text='「' + event.message.text + '」って何？')","     )","","if __name__ == \"__main__\":","    port = int(os.getenv(\"PORT\"))","    app.run(host=\"0.0.0.0\", port=port)","","","","",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":14,"column":28},"end":{"row":14,"column":28},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567610158639,"hash":"eedb51da4e625cf566e32cb2035c7b12ece49cfa"}