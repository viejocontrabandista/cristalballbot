from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from calculos import generar_reporte, guardar_consulta
import threading
import time
import logging

TOKEN = "8446237819:AAGJVPOvIrJd4xqQk120Jk7uzpiIdbdiwDY"  # Pega aquí el token nuevo que te dio BotFather

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
        "Pronto más funciones 🔮",
        parse_mode='Markdown'
    )

async def individual(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 *Estudio Numerológico Individual*\n\n"
        "Envía tu información en este formato:\n\n"
        "*Nombre:* Juan Pérez\n"
        "*Fecha:* 31/12/1990",
        parse_mode='Markdown'
    )
    context.user_data['esperando'] = 'individual'

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('esperando') == 'individual':
        texto = update.message.text.strip()
        nombre = None
        fecha = None
        for linea in texto.split('\n'):
            if linea.lower().startswith('nombre:'):
                nombre = linea[7:].strip()
            elif linea.lower().startswith('fecha:'):
                fecha = linea[6:].strip()
        
        if nombre and fecha:
            reporte = generar_reporte(nombre, fecha)
            await update.message.reply_text(reporte, parse_mode='Markdown')
            guardar_consulta(nombre, fecha, reporte=reporte)
            context.user_data.clear()
        else:
            await update.message.reply_text(
                "❌ Formato incorrecto.\n\n"
                "Envía:\n"
                "*Nombre:* tu nombre completo\n"
                "*Fecha:* DD/MM/AAAA",
                parse_mode='Markdown'
            )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("individual", individual))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
    
    print("🤖 Numeria: El Oráculo iniciado - Online 24/7 en Railway")

    def keep_alive():
        while True:
            time.sleep(10)
            print(f"Keep alive - Bot activo - {time.strftime('%H:%M:%S')}")

    threading.Thread(target=keep_alive, daemon=True).start()
    
    app.run_polling(drop_pending_updates=True)