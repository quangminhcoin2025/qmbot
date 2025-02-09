import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# 🔹 Sử dụng API Token mới của bạn
TOKEN = "7523225425:AAGAW-lYyt3gYCDdFEcsl6PMSaI4rJHUxwQ"

# 🔹 URL để lấy giá XRP từ Binance
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"

# 🔹 Cấu hình logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def get_xrp_price():
    """Lấy giá XRP từ Binance API"""
    response = requests.get(BINANCE_API_URL)
    data = response.json()
    return float(data["price"])

async def start(update: Update, context: CallbackContext):
    """Lệnh /start"""
    await update.message.reply_text("Xin chào! Tôi là bot giao dịch. Nhập /xrp để xem giá XRP.")

async def xrp(update: Update, context: CallbackContext):
    """Lệnh /xrp để lấy giá XRP"""
    price = await get_xrp_price()
    await update.message.reply_text(f"Giá XRP hiện tại: {price:.4f} USDT")

def main():
    """Chạy bot Telegram"""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("xrp", xrp))

    application.run_polling()

if __name__ == "__main__":
    main()
