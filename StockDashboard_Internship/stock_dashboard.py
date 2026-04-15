#!/usr/bin/env python3
"""
STOCK DASHBOARD v2.2 - IDLE Color Fixed
✅ ▲ UP / ▼ DOWN symbols (IDLE visible)
✅ All other features same
✅ Professional + Clear
"""

import requests
import json
import csv
import os
from datetime import datetime
import time

API_KEY = "demo"
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_data(symbol):
    """Get live stock data"""
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
        
        if 'Global Quote' in data and '05. price' in data['Global Quote']:
            quote = data['Global Quote']
            return {
                'symbol': symbol,
                'price': float(quote['05. price']),
                'change': float(quote['09. change']),
                'change_percent': float(quote['10. change percent'].replace('%', '')),
                'volume': int(quote['06. volume'].replace(',', '')),
                'timestamp': quote['07. latest trading day'],
                'fetched_at': datetime.now().isoformat()
            }
        return None
    except:
        return None

def display_dashboard(stocks_data):
    """Professional table with ▲▼ symbols"""
    valid_data = [stock for stock in stocks_data if stock]
    if not valid_data:
        print("❌ No data")
        return
    
    print("\n" + "="*80)
    print("📈 STOCK DASHBOARD - Live Market Data")
    print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    print(f"{'Symbol':<8} {'Price':<10} {'Chg':<8} {'%Chg':<6} {'Volume'}")
    print("-"*80)
    
    for stock in valid_data:
        # ▲ UP PROFIT | ▼ DOWN LOSS
        trend = "▲" if stock['change'] >= 0 else "▼"
        change_abs = abs(stock['change'])
        
        print(f"{stock['symbol']:<8} "
              f"${stock['price']:<9.2f} "
              f"{trend} {change_abs:<6.2f} "
              f"{stock['change_percent']:+5.1f}% "
              f"{stock['volume']:,}")
    
    print("="*80)
    print(f"✅ {len(valid_data)}/{len(stocks_data)} successful")

def save_to_csv(stocks_data, filename=None):
    """CSV export - Excel ready"""
    if not filename:
        filename = f"stocks_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    
    valid_data = [stock for stock in stocks_data if stock]
    if valid_data:
        fieldnames = ['symbol', 'price', 'change', 'change_percent', 'volume', 'timestamp', 'fetched_at']
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_data)
        print(f"💾 CSV: '{filename}'")

def save_to_json(stocks_data, filename=None):
    """JSON export"""
    if not filename:
        filename = f"stocks_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    
    valid_data = [stock for stock in stocks_data if stock]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(valid_data, f, indent=2, default=str)
    print(f"💾 JSON: '{filename}'")

def main():
    """Main dashboard"""
    print("🚀 STOCK DASHBOARD v2.2 - ▲UP ▼DOWN Indicators")
    print("Codec Technologies Financial Analytics\n")
    
    default_stocks = ['IBM', 'AAPL', 'MSFT', 'GOOGL', 'TSLA']
    print("📊 Stocks: " + ", ".join(default_stocks))
    
    custom = input("Custom stocks? (y/N): ").strip().lower()
    stocks = default_stocks.copy()
    
    if custom == 'y':
        extra = input("Enter (comma sep): ").strip().upper()
        if extra:
            extra_stocks = [s.strip() for s in extra.split(',') if s.strip()]
            stocks.extend(extra_stocks)
    
    print(f"\n🔍 Fetching {len(stocks)} stocks...\n")
    
    stocks_data = []
    for i, symbol in enumerate(stocks, 1):
        print(f"📡 [{i}/{len(stocks)}] {symbol}...", end=" ")
        data = get_stock_data(symbol)
        stocks_data.append(data)
        if i < len(stocks):
            time.sleep(0.6)
    
    display_dashboard(stocks_data)
    save_to_csv(stocks_data)
    save_to_json(stocks_data)
    
    print("\n🎯 COMPLETE! Files exported!")
    print("🔄 Enter = Refresh")

if __name__ == "__main__":
    try:
        while True:
            main()
            input()
            print("\n" + "="*80 + "\n")
    except KeyboardInterrupt:
        print("\n👋 Dashboard closed!")
