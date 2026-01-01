from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Importamos las funciones de calculos.py
from calculos import generar_reporte, consulta_existe, guardar_consulta

# === TU TOKEN VA AQUÍ ENTRE COMILLAS ===
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
        "Pronto te pediré los datos paso a paso y generaré tu reporte completo 🔮",
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    import threading
    import time
    import logging

    logging.basicConfig(level=logging.INFO)

    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    
    print("🤖 Numeria: El Oráculo iniciado - Online 24/7 en Railway")

    # Función keep alive en hilo separado
    def keep_alive():
        while True:
            time.sleep(30)
            print("Keep alive - Bot activo en Railway")

    threading.Thread(target=keep_alive, daemon=True).start()
    
    # Inicia el polling (bloquea, pero el keep alive sigue vivo)
    app.run_polling(drop_pending_updates=True)