from aiogram import types

links = ["https://t.me/testingsubs1",
         "https://t.me/testingsubs2", "https://t.me/testingsubs3"]

links_btns = []
count = 1
links_kb = types.InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

for link in links:
    links_btns.append(types.InlineKeyboardButton(f"link {1}", url=link))
    count += 1

links_kb.add(
    *links_btns).add(types.InlineKeyboardButton("ok", callback_data="ok"))
