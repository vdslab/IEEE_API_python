import xplore
import json

query = xplore.xploreapi.XPLORE('API_KEY')
#query.abstractText() #abstractのテキストデータ
#query.affiliationText()　#所属している機関の情報
#query.articleNumber()　#IEEEの管理番号
#query.articleTitle()　#論文タイトル
#doiコード
query.doi('10.1109/LPT.2019.2954012')

JSON_FILE = query.callAPI()
data = json.loads(JSON_FILE)
with open('test.json', 'w') as f:
  json.dump(data, f,indent=1)