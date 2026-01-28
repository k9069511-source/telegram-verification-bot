import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("8242611930:AAEKPM4c7wgsbjhRJmo9W9cybNGHo8tcI7I")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not set")

PUBLIC_CHANNEL = "@sauryasignal4564"
PRIVATE_CHANNEL_LINK = "https://t.me/+Sw01Nxdq1lo4NDFl"
ADMIN_ID = 8034017217

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Join Public Channel", url=f"https://t.me/{PUBLIC_CHANNEL[1:]}")],
                [InlineKeyboardButton("Verify ✅", callback_data="verify")]]
    await update.message.reply_text(
        "👋 Welcome!\n\n1️⃣ Join public channel\n2️⃣ Click Verify",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user

    try:
        member = await context.bot.get_chat_member(PUBLIC_CHANNEL, user.id)
        if member.status in ["member", "administrator", "creator"]:
            await query.message.reply_text(
                f"✅ Verified!\n\n👉 Join private channel:\n{PRIVATE_CHANNEL_LINK}"
            )
        else:
            await query.answer("❌ Join the public channel first!", show_alert=True)
    except:
        await query.answer("❌ Join the public channel first!", show_alert=True)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
