from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from calculos import generar_reporte, guardar_consulta
import threading
import time
import logging

# === TU TOKEN ACTUAL (el último que te dio BotFather después de revoke) ===
TOKEN = "8446237819:AAFLQfBgVb5QjWZlrD9Fpi02VDTt_VQznWk"

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
        "Usa los comandos del menú.\n"
        "Pronto te pediré los datos paso a paso 🔮",
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    
    print("🤖 Numeria: El Oráculo iniciado - Online 24/7 en Railway")

    # Keep alive fuerte cada 10 segundos
    def keep_alive():
        while True:
            time.sleep(10)
            print(f"Keep alive - Bot activo - {time.strftime('%H:%M:%S')}")

    threading.Thread(target=keep_alive, daemon=True).start()
    
    app.run_polling(drop_pending_updates=True)