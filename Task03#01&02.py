import requests

from bs4 import BeautifulSoup

import pandas as pd

import sqlite3


url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html5lib')

# 貨幣

coins_divs = soup.find_all("div", class_="visible-phone print_hide")

coin = [div.get_text(strip=True) for div in coins_divs]

# 現金匯率本行買入

buying_td = soup.find_all("td", {"data-table":"本行現金買入", "class":"rate-content-cash text-right print_hide"})

buying = [td.get_text(strip=True) for td in buying_td]

# 現金匯率本行賣出

selling_td = soup.find_all("td", {"data-table":"本行現金賣出", "class":"rate-content-cash text-right print_hide"})

selling = [td.get_text(strip=True) for td in selling_td]

# 即期匯率本行買入

buying_spot_td = soup.find_all("td", {"data-table":"本行即期買入", "class":"rate-content-sight text-right print_hide"})

buying_spot = [td.get_text(strip=True) for td in buying_spot_td]

# 即期匯率本行賣出

selling_spot_td = soup.find_all("td", {"data-table":"本行即期賣出", "class":"rate-content-sight text-right print_hide"})

selling_spot = [td.get_text(strip=True) for td in selling_spot_td]


data = {'貨幣': coin, 
        '現金匯率本行買入' : buying,
        '現金匯率本行賣出' : selling,
        '即期匯率本行買入' : buying_spot,
        '即期匯率本行賣出' : selling_spot}
df = pd.DataFrame(data)

#hw02
#新增即時更新時間
Last_Update_date = soup.find('span', class_ = 'time').text.strip() # type: ignore

df['即時更新時間'] = Last_Update_date 
print(df)
# 建立 SQLite 資料庫連線

conn = sqlite3.connect('currency.db')

df.to_sql('currency', conn, if_exists='replace', index=False)

conn.close()
