import xplore
import json
import time
import os

#自分のAPI_KEYを入力pushするときはAPI_KEYに戻す
query = xplore.xploreapi.XPLORE('API_KEY')

# 取得したいtitleたち
public_titles = [
    'Journal on Selected Areas in Communications',
    'Transactions on Evolutionary Computation',
    'Wireless Communications'
]
# 仕様に無理やり当てはめてる
pubtitle = public_titles[2]

#ディレクトリの作成
os.makedirs(pubtitle,exist_ok=True)

# 年代を指定しながらその年代のjsonの作成
years = []
for num in range(1992, 1993):
    years.append(str(num))
    num += 1

print("\n---- getting {} ----\n".format(pubtitle))
for year in years:
    # 取得開始の表示
    print("year:{} > now loading......".format(year))
    # 取得する数
    query.maximumResults(200)
    # 雑誌のタイトル
    query.publicationTitle(pubtitle)
    # 取得する年数
    query.publicationYear(year)
    # 取得する場所の指定
    query.startingResult(1)
    JSON_FILE = query.callAPI()
    data = json.loads(JSON_FILE)

    record_unit = 200
    record_id = 0
    # 200超えていたら201番目から再取得，
    while(record_unit*record_id < data["total_records"]):
        # 取得しているidの表示
        print("\tid:{} loading ......".format(year, record_id))
        # 取得する場所の指定
        query.startingResult(record_unit * record_id + 1)
        # apiの呼び出し
        NEW_JSON_FILE = query.callAPI()
        # jsonとして読み込む
        new_data = json.loads(NEW_JSON_FILE)
        # jsonファイルに書き込む
        if(record_id == 0) :
            with open(pubtitle+'/' + year + '.json'.format(record_id+1), 'w') as f:
                json.dump(new_data, f, indent=1)
        else :
            with open(pubtitle+'/' + year + '-{}.json'.format(record_id+1), 'w') as f:
                json.dump(new_data, f, indent=1)
        # 書き込み終了の表示
        print("\t\t==> dumped.".format(year, record_id))
        # 更新処理
        record_id += 1

    # その年の取得終了の表示 
    print("year:{} > finish\n".format(year))
    # API取得したら時間を1秒待機
    time.sleep(1)

# 今現在は200を超えた場合にひとつのファイルにできていない。これは一つのファイルにするように変更する。
