from flask import Flask

from dotenv import load_dotenv
import os


app = Flask(__name__)

COINS = [
    "EUR - Euro",
    "ETH - Ethereum",
    "BNB - Binance",
    "XRP - Ripple",
    "ADA - Cardano",
    "SOL - Solana",
    "DOT - Polkadot",
    "DOGE - Dogecoin",
    "MATIC - Polygon",
    "ALGO - Algorand"
]



