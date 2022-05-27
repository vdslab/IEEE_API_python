import xplore
import json
import time

query = xplore.xploreapi.XPLORE('API_KEY')
#年代を指定しながらその年代のjsonの作成
years = []
for num in range(1990,1991):
    years.append(str(num))
    num += 1


for year in years :
  #取得する数
  query.maximumResults(200)
  #雑誌のタイトル
  query.publicationTitle('')
  #取得する年数
  query.publicationYear(year)
  #取得する場所の指定
  query.startingResult(1)
  JSON_FILE = query.callAPI()
  data = json.loads(JSON_FILE)
  dir = 'Pattern Analysis and Machine Intelligence/'
  #保存する場所と名前を変更（年代がjsonの名前になるようにしている。変更してもらってよろしい）
  with open(dir + year +'.json', 'w') as f:
    json.dump(data, f,indent=1)

  #1回200までしかできないので200超えていたら201番目から再取得。400超えていたらまた作成。
  if(data['total_records'] > 200) :
    #取得する場所の指定
    query.startingResult(201)
    JSON_FILE2 = query.callAPI()
    data2 = json.loads(JSON_FILE2)
    with open(dir + year +'-2.json', 'w') as f:
      json.dump(data2, f,indent=1)
  #API取得したら時間を1秒待機
  time.sleep(1)

#今現在は200を超えた場合にひとつのファイルにできていない。これは一つのファイルにするように変更する。
