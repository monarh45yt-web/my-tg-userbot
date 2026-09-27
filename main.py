from pyrogram import Client, filters

API_ID = 36087554                # Ваш API_ID
API_HASH = "0684924f16cd135ea37a0160f20e08a8"    # Ваш API_HASH
SESSION_STRING = "AgImpwIABSmnKbyDfouzqlnO8NcWoTXkg_72wcv70F31rBqlXyq1NxWAzRIPBsCpBzG1sodYYi5kveJ8CU-CrUGRI79PuN_w6z178K2Dv7R0JEkjknLcpCUWmn0yvRnfAr2c9xkDGh8hWpC9OFHBpHgbyAsiZSKfNI3w5Y4sIeo_FUnQkBo3_-tFJLX9QSywib0uJWjNYEgHGRwzbpLplSm8br82BshAdEqaDQLDYi6foPUwiTUaN6Ffe68-BzaAmpGmw0Fe2YqT4LL_NoXEcxcFf2cEvGMJl3KohGohdAGDN8ldVNwAaKulF9hRv1yJ-LBpqMCewySCEy_JF9PNTNG2qNHDngAAAAHBrxFhAA"

# ==================== 1. ГДЕ ОТВЕЧАТЬ ====================
# Укажите юзернеймы групп (начинаются с @) или их цифровые ID.
# Пример: ["@my_group_1", "@my_group_2"] или [-1001234567890]
TARGET_CHATS = [-1003603462795]

# ==================== 2. КОГДА ОТВЕЧАТЬ ====================
# Список фраз, на которые бот будет реагировать (в нижнем регистре):
TRIGGER_WORDS = ["인천광역시 제물포구 항동7가 29-3"]

# Текст вашего ответа:
REPLY_TEXT = "Monarh 010-7267-0199"

# =========================================================

# Флаг включения/выключения (по умолчанию ВКЛЮЧЕН)
IS_ACTIVE = True

app = Client(
    "my_userbot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)


# КОМАНДА УПРАВЛЕНИЯ: Напишите в любом чате от своего имени:
# `.авто вкл`  — чтобы включить
# `.авто выкл` — чтобы выключить
@app.on_message(filters.me & filters.command(["авто"], prefixes="."))
async def toggle_auto_responder(client, message):
    global IS_ACTIVE
    if len(message.command) > 1:
        status = message.command[1].lower()
        if status in ["вкл", "on", "1"]:
            IS_ACTIVE = True
            await message.edit_text("✅ **Автоответчик ВКЛЮЧЕН**")
        elif status in ["выкл", "off", "0"]:
            IS_ACTIVE = False
            await message.edit_text("❌ **Автоответчик ВЫКЛЮЧЕН**")
        else:
            await message.edit_text("Использование: `.авто вкл` или `.авто выкл`")


# ОСНОВНОЙ АВТООТВЕТЧИК
@app.on_message(filters.chat(TARGET_CHATS) & filters.group & ~filters.me)
async def auto_reply(client, message):
    global IS_ACTIVE
    
    # Если автоответчик выключен командой — ничего не делаем
    if not IS_ACTIVE:
        return
        
    if message.text:
        text = message.text.lower()
        # Проверяем, есть ли хотя бы одно ключевое слово из списка
        if any(word in text for word in TRIGGER_WORDS):
            await message.reply(REPLY_TEXT)


print("Юзербот запущен с выбором групп и управлением!")
app.run()
