from telegram import Bot
import pandas as pd
import asyncio

API_TOKEN = '1968085479:AAEck4QaWFrY9Bl7tNKRaqF3lNe0dIrr3Kg'
bot = Bot(token=API_TOKEN)
df = pd.read_excel("test.xlsx")
# df = df[['Rank','Close','Ch_R','Name','Thema']]
df = df[['Rank','Ch_R','Name','Thema']]
df_string = df.head(15).to_string(index=False)
print(df_string)
async def send_telegram_message(message_text="test"):
    chat_id = '1956916092'
    # 메시지를 보내고 응답을 기다리기 위해 await 키워드를 사용합니다.
    await bot.send_message(chat_id=chat_id, text=message_text)

# 비동기 함수를 실행합니다.

asyncio.run(send_telegram_message(df_string))