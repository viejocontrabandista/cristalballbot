from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Importamos las funciones de calculos.py
from calculos import generar_reporte, consulta_existe, guardar_consulta

# === TU TOKEN VA AQUÍ ENTRE COMILLAS ===
TOKEN = "8446237819:AAFV_zPY7sX91uWptCqt3K4-WhD_ctoW6NU"

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
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    
    print("Bot iniciado - Esperando mensajes...")
    app.run_polling(drop_pending_updates=True)