from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters
)
from calculos import generar_reporte, guardar_consulta
import threading
import time
import logging

TOKEN = "8446237819:AAGnhQ1iD2ESgJLcHtOfOPT08QAenENYAmM"


# ───────────── COMANDOS ─────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 *Bienvenido a Numeria: El Oráculo*\n\n"
        "Soy tu guía numerológico.\n\n"
        "• /individual - Estudio personal\n"
        "• Próximamente: /pareja - Compatibilidad amorosa 💞\n"
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
    context.user_data.clear()

    keyboard = [
    [InlineKeyboardButton("🧑 Ingresar nombre y apellido", callback_data="set_nombre")],
    [InlineKeyboardButton("📅 Ingresar fecha de nacimiento", callback_data="set_fecha")],
    [InlineKeyboardButton("🔮 Obtener lectura", callback_data="generar")]
]

    await update.message.reply_text(
        "🔮 *Estudio Numerológico Individual*\n\n"
        "Usá los botones para ingresar tus datos:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )


# ───────────── BOTONES ─────────────

async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "set_nombre":
        context.user_data["esperando"] = "nombre"
        await query.message.reply_text("🧑 Escribí tu nombre completo:")

    elif data == "set_fecha":
        context.user_data["esperando"] = "fecha"
        await query.message.reply_text("📅 Escribí tu fecha (DD/MM/AAAA):")

    elif data == "generar":
        nombre = context.user_data.get("nombre")
        fecha = context.user_data.get("fecha")

        if not nombre or not fecha:
            await query.message.reply_text("❌ Falta nombre o fecha.")
            return

        reporte = generar_reporte(nombre, fecha)
        await query.message.reply_text(reporte, parse_mode="Markdown")
        guardar_consulta(nombre, fecha, reporte=reporte)

        context.user_data.clear()
        await query.message.reply_text("✅ Reporte enviado. Usa /individual para otro.")


# ───────────── TEXTO ─────────────

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    esperando = context.user_data.get("esperando")
    texto = update.message.text.strip()

    if esperando == "nombre":
        context.user_data["nombre"] = texto
        context.user_data["esperando"] = None
        await update.message.reply_text("✅ Nombre guardado.")

    elif esperando == "fecha":
        context.user_data["fecha"] = texto
        context.user_data["esperando"] = None
        await update.message.reply_text("✅ Fecha guardada.")


# ───────────── MAIN ─────────────

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("individual", individual))
    app.add_handler(CallbackQueryHandler(botones))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    print("🤖 Numeria: El Oráculo iniciado - Online 24/7 en Railway")

    def keep_alive():
        while True:
            time.sleep(10)
            print(f"Keep alive - Bot activo - {time.strftime('%H:%M:%S')}")

    threading.Thread(target=keep_alive, daemon=True).start()

    app.run_polling(drop_pending_updates=True)
