from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from calculos import generar_reporte, consulta_existe, guardar_consulta
import os

TOKEN = os.environ['TOKEN']  # Token desde variables de Railway

app = FastAPI()

application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 *Bienvenido a Numeria: El Oráculo*\n\n"
        "Soy tu guía numerológico.\n\n"
        "• /individual - Estudio personal\n"
        "• /pareja - Compatibilidad amorosa\n"
        "• /ayuda - Instrucciones",
        parse_mode='Markdown'
    )

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Usa los comandos. Pronto más funciones 🔮",
        parse_mode='Markdown'
    )

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("ayuda", ayuda))

@app.on_event("startup")
async def startup():
    await application.initialize()
    await application.start()
    print("Bot iniciado con webhook")

@app.on_event("shutdown")
async def shutdown():
    await application.stop()
    await application.shutdown()

@app.post("/")
async def webhook(request: Request):
    update = Update.de_json(await request.json(), application.bot)
    await application.process_update(update)
    return "ok"