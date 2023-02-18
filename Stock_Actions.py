import yfinance as yf
import matplotlib.pyplot as plt
import random
from datetime import date
from yahoo_fin import stock_info as si
import os
import time
mode = input("Press 0 for information\nPress 1 to play the GAMMA investing simulator\nPress 2 to play the crypto investing simulator\nPress 3 to view stock data\nPress 4 to play the fake GAMMA and crypto trader\nPress 5 to practice shorting a stock\nPress 6 to enter the stock price predictor\nPress 7 to find the best stocks to invest in (WARNING: EXTREMELY SLOW)\nPress 8 to find the best S&P 500 stocks to buy\nPress 9 to find the best DOW companies to buy\nPress 10 to find the best NASDAQ companies to buy\nPress 11 to find all the other best companies to buy\n")
mode0 = "0"
if mode == "0":
  while True:
    os.system('clear')
    subject = input("Enter the corresponding number for what you want to know:\n\n1. Stocks\n2. Cryptocurrency\n3. Stock shorting\n4. I am ready to play a game\n")
    if subject == "1":
      wait = input("\nA stock, also known as equity, is a security that represents the ownership of a fraction of the issuing corporation. Units of stock are called \"shares\" which entitles the owner to a proportion of the corporation's assets and profits equal to how much stock they own.\n\nStocks are bought and sold predominantly on stock exchanges and are the foundation of many individual investors' portfolios. Stock trades have to conform to government regulations meant to protect investors from fraudulent practices.")
    if subject == "2":
      wait = input("Cryptocurrency is a digital payment system that doesn't rely on banks to verify transactions. It’s a peer-to-peer system that can enable anyone anywhere to send and receive payments. Instead of being physical money carried around and exchanged in the real world, cryptocurrency payments exist purely as digital entries to an online database describing specific transactions. When you transfer cryptocurrency funds, the transactions are recorded in a public ledger. Cryptocurrency is stored in digital wallets.\n\nCryptocurrency received its name because it uses encryption to verify transactions. This means advanced coding is involved in storing and transmitting cryptocurrency data between wallets and to public ledgers. The aim of encryption is to provide security and safety.\n\nThe first cryptocurrency was Bitcoin, which was founded in 2009 and remains the best known today. Much of the interest in cryptocurrencies is to trade for profit, with speculators at times driving prices skyward.")
    if subject == "3":
      wait = input("Short selling is when a trader borrows shares from a broker and immediately sells them with the expectation that the share price will fall shortly after. If it does, the trader can buy the shares back at the lower price, return them to the broker, and keep the difference, minus any loan interest, as profit.\n\nHere’s an example: You borrow 10 shares of a company (or an ETF or REIT), then immediately sell them on the stock market for $10 each, generating $100. If the price drops to $5 per share, you could use your $100 to buy back all 10 shares for only $50, then return the shares to the broker. In the end, you netted $50 on the short (minus any commissions, fees and interest).")
    if subject == "4":
      game = input("Press 1 to play the GAMMA investing simulator\nPress 2 to play the crypto investing simulator\nPress 3 to view stock data\nPress 4 to play the fake GAMMA and crypto trader\nPress 5 to practice shorting a stock\n")
      mode0 = game
      break
revx3 = "Arnav"
def credc(str):
  print(str)
def bar(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    tags = "=" * round(left)
    spaces = " " * round(right)
    percents = f"{percent:.0f}%"
    print("\r[", tags, spaces, "]", sep="", end="\n", flush=True)
if mode == "1" or mode0 == "1":
  os.system('clear')
  game = input("Press enter to join a game or press 0 for a new game\n")
  if game == "0":
    money = 10000
    print("Money: ", money)
    aapli = 0
    msfti = 0
    googi = 0
    metai = 0
    amzni = 0
    while True:
      os.system('clear')
      aapl = round(yf.Ticker("AAPL").fast_info["last_price"], 2)
      msft = round(yf.Ticker("MSFT").fast_info["last_price"], 2)
      goog = round(yf.Ticker("GOOG").fast_info["last_price"], 2)
      meta = round(yf.Ticker("META").fast_info["last_price"], 2)
      amzn = round(yf.Ticker("AMZN").fast_info["last_price"], 2)
      print("Apple: ", aapl)
      print()
      print("Microsoft: ", msft)
      print()
      print("Google: ", goog)
      print()
      print("Meta: ", meta)
      print()
      print("Amazon: ", amzn)
      option = int(input("Press 1 to invest\nPress 2 to sell\nPress 3 to view your stocks\nPress 4 to exit the game\n"))
      if option == 1:
        comp = input("What company?\n")
        num = int(input("How many stocks?\n"))
        if comp == "apple":
          aapli += num
          money -= aapl*num
          print("Money: ", money)
        if comp == "microsoft":
          msfti += num
          money -= msft*num
          print("Money: ", money)
        if comp == "google":
          googi += num
          money -= goog*num
          print("Money: ", money)
        if comp == "meta":
          metai += num
          money -= meta*num
          print("Money: ", money)
        if comp == "amazon":
          amzni += num
          money -= amzn*num
          print("Money: ", money)
      if option == 2:
        comp = input("What company?\n").lower
        num = int(input("How many stocks?\n"))
        if comp == "apple":
          if num > aapli:
            num = aapli
          aapli -= num
          money += aapl*num
          print("Money: ", money)
        if comp == "microsoft":
          if num > msfti:
            num = msfti
          msfti -= num
          money += msft*num
          print("Money: ", money)
        if comp == "google":
          if num > googi:
            num = googi
          googi -= num
          money += goog*num
          print("Money: ", money)
        if comp == "meta":
          if num > metai:
            num = metai
          metai -= num
          money += meta*num
          print("Money: ", money)
        if comp == "amazon":
          if num > amzni:
            num = amzni
          amzni -= num
          money += amzn*num
          print("Money: ", money)
      if option == 3:
        print("Apple: ", aapli)
        print("Microsoft: ", msfti)
        print("Google: ", googi)
        print("Meta: ", metai)
        print("Amazon: ", amzni)
      if option == 4:
        break
    codetup = (str(money), str(aapli), str(msfti), str(googi), str(metai), str(amzni))
    code = "-".join(codetup)
    print("Use this code to return to this game:  ", code)
  else:
    print("Please enter the numbers in your save code")
    money = 0
    aapli = 0
    msfti = 0
    googi = 0
    metai = 0
    amzni = 0
    count = 0
    for i in range(6):
      j = float(input())
      if count == 0:
        money = j
      if count == 1:
        aapli = j
      if count == 2:
        msfti = j
      if count == 3:
        googi = j
      if count == 4:
        metai = j
      if count == 5:
        amzni = j
      count += 1
    print("Money: ", money)
    while True:
      os.system('clear')
      aapl = round(yf.Ticker("AAPL").fast_info["last_price"], 2)
      msft = round(yf.Ticker("MSFT").fast_info["last_price"], 2)
      goog = round(yf.Ticker("GOOG").fast_info["last_price"], 2)
      meta = round(yf.Ticker("META").fast_info["last_price"], 2)
      amzn = round(yf.Ticker("AMZN").fast_info["last_price"], 2)
      print("Apple: ", aapl)
      print()
      print("Microsoft: ", msft)
      print()
      print("Google: ", goog)
      print()
      print("Meta: ", meta)
      print()
      print("Amazon: ", amzn)
      option = int(input("Press 1 to invest\nPress 2 to sell\nPress 3 to view your stocks\nPress 4 to exit the game\n"))
      if option == 1:
        comp = input("What company?\n")
        num = int(input("How many stocks?\n"))
        if comp == "apple":
          aapli += num
          money -= aapl*num
          print("Money: ", money)
        if comp == "microsoft":
          msfti += num
          money -= msft*num
          print("Money: ", money)
        if comp == "google":
          googi += num
          money -= goog*num
          print("Money: ", money)
        if comp == "meta":
          metai += num
          money -= meta*num
          print("Money: ", money)
        if comp == "amazon":
          amzni += num
          money -= amzn*num
          print("Money: ", money)
      if option == 2:
        comp = input("What company?\n").lower
        num = int(input("How many stocks?\n"))
        if comp == "apple":
          if num > aapli:
            num = aapli
          aapli -= num
          money += aapl*num
          print("Money: ", money)
        if comp == "microsoft":
          if num > msfti:
            num = msfti
          msfti -= num
          money += msft*num
          print("Money: ", money)
        if comp == "google":
          if num > googi:
            num = googi
          googi -= num
          money += goog*num
          print("Money: ", money)
        if comp == "meta":
          if num > metai:
            num = metai
          metai -= num
          money += meta*num
          print("Money: ", money)
        if comp == "amazon":
          if num > amzni:
            num = amzni
          amzni -= num
          money += amzn*num
          print("Money: ", money)
      if option == 3:
        print("Apple: ", aapli)
        print("Microsoft: ", msfti)
        print("Google: ", googi)
        print("Meta: ", metai)
        print("Amazon: ", amzni)
        wait = input()
      if option == 4:
        break
    codetup = (str(money), str(aapli), str(msfti), str(googi), str(metai), str(amzni))
    code = "-".join(codetup)
    print("Use this code to return to this game:  ", code)
revx4 = "Malhotra"
revx2 = "by"
if mode == "2" or mode0 == "2":
  game = input("Press enter to join a game or press 0 for a new game\n")
  if game == "0":
    money = 10000
    print("Money: ", money)
    btci = 0
    ethi = 0
    dogei = 0
    soli = 0
    okbi = 0
    while True:
      os.system('clear')
      btc = round(yf.Ticker("BTC-USD").fast_info["last_price"], 2)
      eth = round(yf.Ticker("ETH-USD").fast_info["last_price"], 2)
      doge = round(yf.Ticker("DOGE-USD").fast_info["last_price"], 2)
      sol = round(yf.Ticker("SOL-USD").fast_info["last_price"], 2)
      okb = round(yf.Ticker("OKB-USD").fast_info["last_price"], 2)
      print("Bitcoin: ", btc)
      print()
      print("Ethereum: ", eth)
      print()
      print("Dogecoin: ", doge)
      print()
      print("Solana: ", sol)
      print()
      print("OKB: ", okb)
      option = int(input("Press 1 to invest\nPress 2 to sell\nPress 3 to view your stocks\nPress 4 to exit the game\n"))
      if option == 1:
        comp = input("What company?\n")
        num = int(input("How many stocks?\n"))
        if comp == "bitcoin":
          btci += num
          money -= btc*num
          print("Money: ", money)
        if comp == "ethereum":
          ethi += num
          money -= eth*num
          print("Money: ", money)
        if comp == "dogecoin":
          dogei += num
          money -= doge*num
          print("Money: ", money)
        if comp == "solana":
          soli += num
          money -= sol*num
          print("Money: ", money)
        if comp == "okb":
          okbi += num
          money -= okb*num
          print("Money: ", money)
      if option == 2:
        comp = input("What company?\n").lower
        num = int(input("How many stocks?\n"))
        if comp == "bitcoin":
          if num > btci:
            num = btci
          btci -= num
          money += btc*num
          print("Money: ", money)
        if comp == "ethereum":
          if num > ethi:
            num = ethi
          ethi -= num
          money += eth*num
          print("Money: ", money)
        if comp == "dogecoin":
          if num > dogei:
            num = dogei
          dogei -= num
          money += doge*num
          print("Money: ", money)
        if comp == "solana":
          if num > soli:
            num = soli
          soli -= num
          money += sol*num
          print("Money: ", money)
        if comp == "okb":
          if num > okbi:
            num = okbi
          okbi -= num
          money += okb*num
          print("Money: ", money)
      if option == 3:
        print("Bitcoin: ", btci)
        print("Ethereum: ", ethi)
        print("Dogecoin: ", dogei)
        print("Solana: ", soli)
        print("OKB: ", okbi)
      if option == 4:
        break
    codetup = (str(money), str(btci), str(ethi), str(dogei), str(soli), str(okbi))
    code = "-".join(codetup)
    print("Use this code to return to this game:  ", code)
  else:
    print("Please enter the numbers in your save code")
    money = 0
    btci = 0
    ethi = 0
    dogei = 0
    soli = 0
    okbi = 0
    count = 0
    for i in range(6):
      j = float(input())
      if count == 0:
        money = j
      if count == 1:
        btci = j
      if count == 2:
        ethi = j
      if count == 3:
        dogei = j
      if count == 4:
        soli = j
      if count == 5:
        okbi = j
      count += 1
    print("Money: ", money)
    while True:
      btc = round(yf.Ticker("BTC-USD").fast_info["last_price"], 2)
      eth = round(yf.Ticker("ETH-USD").fast_info["last_price"], 2)
      doge = round(yf.Ticker("DOGE-USD").fast_info["last_price"], 2)
      sol = round(yf.Ticker("SOL-USD").fast_info["last_price"], 2)
      okb = round(yf.Ticker("OKB-USD").fast_info["last_price"], 2)
      print("Bitcoin: ", btc)
      print()
      print("Ethereum: ", eth)
      print()
      print("Dogecoin: ", doge)
      print()
      print("Solana: ", sol)
      print()
      print("OKB: ", okb)
      option = int(input("Press 1 to invest\nPress 2 to sell\nPress 3 to view your stocks\nPress 4 to exit the game\n"))
      if option == 1:
        comp = input("What company?\n")
        num = int(input("How many stocks?\n"))
        if comp == "bitcoin":
          btci += num
          money -= btc*num
          print("Money: ", money)
        if comp == "ethereum":
          ethi += num
          money -= eth*num
          print("Money: ", money)
        if comp == "dogecoin":
          dogei += num
          money -= doge*num
          print("Money: ", money)
        if comp == "solana":
          soli += num
          money -= sol*num
          print("Money: ", money)
        if comp == "okb":
          okbi += num
          money -= okb*num
          print("Money: ", money)
      if option == 2:
        comp = input("What company?\n").lower
        num = int(input("How many stocks?\n"))
        if comp == "bitcoin":
          if num > btci:
            num = btci
          btci -= num
          money += btc*num
          print("Money: ", money)
        if comp == "ethereum":
          if num > ethi:
            num = ethi
          ethi -= num
          money += eth*num
          print("Money: ", money)
        if comp == "dogecoin":
          if num > dogei:
            num = dogei
          dogei -= num
          money += doge*num
          print("Money: ", money)
        if comp == "solana":
          if num > soli:
            num = soli
          soli -= num
          money += sol*num
          print("Money: ", money)
        if comp == "okb":
          if num > okbi:
            num = okbi
          okbi -= num
          money += okb*num
          print("Money: ", money)
      if option == 3:
        print("Bitcoin: ", btci)
        print("Ethereum: ", ethi)
        print("Dogecoin: ", dogei)
        print("Solana: ", soli)
        print("OKB: ", okbi)
        wait = input()
      if option == 4:
        break
    codetup = (str(money), str(aapli), str(msfti), str(googi), str(metai), str(amzni))
    code = "-".join(codetup)
    print("Use this code to return to this game:  ", code)
if mode == "3" or mode0 == "3":
  while True:
    comp = int(input("Press 1 to view one company\nPress 2 to view two companies\n"))
    start = input("Enter the start date    ex: 1970-1-1\n")
    end = input("Enter the end date\n")
    com1 = input("Enter the ticker for the first company\n")
    com2 = input("Enter the ticker for the second company (Leave blank for one company\n")
    if comp == 1:
      info = yf.Ticker(com1).fast_info
      for i in info:
        print(i, ":", info[i])
      data = yf.download(com1, start, end)
      data['Close'].plot()
      plt.show()
    else:
      info1 = yf.Ticker(com1).fast_info
      info2 = yf.Ticker(com2).fast_info
      print(com1, ":\n")
      for i in info1:
        print(i, ":", info1[i])
      print()
      print(com2, ":\n")
      for i in info2:
        print(i, ":", info2[i])
      data = yf.download([com1, com2], start, end)
      data['Close'].plot()
      plt.show()
revx1 = "Made"
if mode == "4" or mode0 == "4":
  sc = input("Stocks or Crypto? s/c")
  if sc == "s":
    while True:
      class stock:
        amount = 0
        price = 100
      aa = stock()
      ms = stock()
      go = stock()
      am = stock()
      me = stock()
      f = stock()
      money = 10000
      count = 1
      skipper = 0
      mode = input("Chill or Volatile (BETA)? (c/v)")
      while True:
        if mode == "c":
          round(money, 2)
          fall = random.randint(6, 12)
          print("\n"*60)
          if count % fall == 0:
            aa.price = round(aa.price/random.uniform(1.2, 1.5), 2)
            ms.price = round(ms.price/random.uniform(1.2, 1.5), 2)
            go.price = round(go.price/random.uniform(1.2, 1.5), 2)
            am.price = round(am.price/random.uniform(1.2, 1.5), 2)
            me.price = round(me.price/random.uniform(1.2, 1.5), 2)
          else:
            aa.price = round(aa.price*random.uniform(0.9, 1.2), 2)
            ms.price = round(ms.price*random.uniform(0.9, 1.2), 2)
            go.price = round(go.price*random.uniform(0.9, 1.2), 2)
            am.price = round(am.price*random.uniform(0.9, 1.2), 2)
            me.price = round(me.price*random.uniform(0.9, 1.2), 2)
          if skipper > 0:
            count += 1
            skipper -= 1
            continue
          value = aa.amount*aa.price+ms.amount*ms.price+go.amount*go.price+am.amount*am.price+me.amount*me.price+f.amount*f.price+money
          round(value, 2)
          print("Week: ", count, "\n\nMoney: ", money, "Account Value: ", value)
          f.price = round(aa.price + ms.price + go.price + am.price + me.price, 2)
          print("AAPL: ", aa.price, " MSFT: ", ms.price, " GOOG: ", go.price, " AMZN: ", am.price, " META: ", me.price, "GAMMA Fund: ", f.price)
          option = input(("1 to invest, 2 to sell, 3 to view what stocks you have, 4 to skip, 5 to skip 10 weeks\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
          if option == "1":
            comp = int(input("How many companies"))
            for i in range(comp):
              com = input("Which company? ( AAPL, MSFT, GOOG, AMZN, META, GAMMA)\n")
              num = int(input("How many stocks"))
              if com == "AAPL":
                aa.amount += num
                money -= num*aa.price
              if com == "MSFT":
                ms.amount += num
                money -= num*ms.price
              if com == "GOOG":
                go.amount += num
                money -= num*go.price
              if com == "AMZN":
                am.amount += num
                money -= num*am.price
              if com == "META":
                me.amount += num
                money -= num*me.price
              if com == "GAMMA":
                f.amount += num
                money -= num*f.price
          if option == "2":
            comp = int(input("How many companies"))
            for i in range(comp):
              com = input("Which company?")
              num = int(input("How many stocks"))
              if com == "AAPL":
                if num > aa.amount:
                  num = aa.amount
                money += aa.price*num
                aa.amount -= num
              if com == "MSFT":
                if num > ms.amount:
                  num = ms.amount
                money += ms.price*num
                ms.amount -= num
              if com == "GOOG":
                if num > go.amount:
                  num = go.amount
                money += go.price*num
                go.amount -= num
              if com == "AMZN":
                if num > am.amount:
                  num = am.amount
                money += am.price*num
                am.amount -= num
              if com == "META":
                if num > me.amount:
                  num = me.amount
                money += me.price*num
                me.amount -= num
              if com == "GAMMA":
                if num > f.amount:
                  num = f.amount
                money += f.price*num
                f.amount -= num
          if option == "3":
            print("AAPL: ", aa.amount)
            print("MSFT: ", ms.amount)
            print("GOOG: ", go.amount)
            print("AMZN: ", am.amount)
            print("META: ", me.amount)
            print("GAMMA Fund: ", f.amount)
            wait = input("Press enter to continue")
          if option == "4":
            count += 1
            continue
          if option == "5":
            skipper = 10
          if option == "password":
            admin = input("\n\nWelcome to ADMIN Commands:\n\nPress 1 to change the week (You can't go back in time)\nPress 2 to add to your account")
            if admin == "1":
              week = int(input("What week?"))
              skipper = week-count
            if admin == "2":
              choice1 = input("Money or stocks? (m/s)")
              if choice1 == "m":
                choice2 = int(input("How much money?"))
                money += choice2
              if choice1 == "s":
                comp = int(input("How many companies"))
                for i in range(comp):
                  com = input("Which company? ( AAPL, MSFT, GOOG, AMZN, META, GAMMA)\n")
                  num = int(input("How many stocks"))
                  if com == "AAPL":
                    aa.amount += num
                  if com == "MSFT":
                    ms.amount += num
                  if com == "GOOG":
                    go.amount += num
                  if com == "AMZN":
                    am.amount += num
                  if com == "META":
                    me.amount += num
                  if com == "GAMMA":
                    f.amount += num
        if mode == "v":
          round(money, 2)
          fall = random.randint(2, 6)
          print("\n"*60)
          if count % fall == 0:
            aa.price = round(aa.price/random.uniform(1.2, 2), 2)
            ms.price = round(ms.price/random.uniform(1.2, 2), 2)
            go.price = round(go.price/random.uniform(1.2, 2), 2)
            am.price = round(am.price/random.uniform(1.2, 2), 2)
            me.price = round(me.price/random.uniform(1.2, 2), 2)
          else:
            aa.price = round(aa.price*random.uniform(0.9, 1.6), 2)
            ms.price = round(ms.price*random.uniform(0.9, 1.6), 2)
            go.price = round(go.price*random.uniform(0.9, 1.6), 2)
            am.price = round(am.price*random.uniform(0.9, 1.6), 2)
            me.price = round(me.price*random.uniform(0.9, 1.6), 2)
          if skipper > 0:
            count += 1
            skipper -= 1
            continue
          value = aa.amount*aa.price+ms.amount*ms.price+go.amount*go.price+am.amount*am.price+me.amount*me.price+f.amount*f.price+money
          round(value, 2)
          print("Week: ", count, "\n\nMoney: ", money, "Account Value: ", value)
          f.price = round(aa.price + ms.price + go.price + am.price + me.price, 2)
          print("AAPL: ", aa.price, " MSFT: ", ms.price, " GOOG: ", go.price, " AMZN: ", am.price, " META: ", me.price, "GAMMA Fund: ", f.price)
          option = input(("1 to invest, 2 to sell, 3 to view what stocks you have, 4 to skip, 5 to skip 10 weeks\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
          if option == "1":
            comp = int(input("How many companies"))
            for i in range(comp):
              com = input("Which company? ( AAPL, MSFT, GOOG, AMZN, META, GAMMA)\n")
              num = int(input("How many stocks"))
              if com == "AAPL":
                aa.amount += num
                money -= num*aa.price
              if com == "MSFT":
                ms.amount += num
                money -= num*ms.price
              if com == "GOOG":
                go.amount += num
                money -= num*go.price
              if com == "AMZN":
                am.amount += num
                money -= num*am.price
              if com == "META":
                me.amount += num
                money -= num*me.price
              if com == "GAMMA":
                f.amount += num
                money -= num*f.price
          if option == "2":
            comp = int(input("How many companies"))
            for i in range(comp):
              com = input("Which company?")
              num = int(input("How many stocks"))
              if com == "AAPL":
                if num > aa.amount:
                  num = aa.amount
                money += aa.price*num
                aa.amount -= num
              if com == "MSFT":
                if num > ms.amount:
                  num = ms.amount
                money += ms.price*num
                ms.amount -= num
              if com == "GOOG":
                if num > go.amount:
                  num = go.amount
                money += go.price*num
                go.amount -= num
              if com == "AMZN":
                if num > am.amount:
                  num = am.amount
                money += am.price*num
                am.amount -= num
              if com == "META":
                if num > me.amount:
                  num = me.amount
                money += me.price*num
                me.amount -= num
              if com == "GAMMA":
                if num > f.amount:
                  num = f.amount
                money += f.price*num
                f.amount -= num
          if option == "3":
            print("AAPL: ", aa.amount)
            print("MSFT: ", ms.amount)
            print("GOOG: ", go.amount)
            print("AMZN: ", am.amount)
            print("META: ", me.amount)
            print("GAMMA Fund: ", f.amount)
            wait = input("Press enter to continue")
          if option == "4":
            count += 1
            continue
          if option == "5":
            skipper = 10
          if option == "password":
            admin = input("\n\nWelcome to ADMIN Commands:\n\nPress 1 to change the week (You can't go back in time)\nPress 2 to add to your account")
            if admin == "1":
              week = int(input("What week?"))
              skipper = week-count
            if admin == "2":
              choice1 = input("Money or stocks? (m/s)")
              if choice1 == "m":
                choice2 = int(input("How much money?"))
                money += choice2
              if choice1 == "s":
                comp = int(input("How many companies"))
                for i in range(comp):
                  com = input("Which company? ( AAPL, MSFT, GOOG, AMZN, META, GAMMA)\n")
                  num = int(input("How many stocks"))
                  if com == "AAPL":
                    aa.amount += num
                  if com == "MSFT":
                    ms.amount += num
                  if com == "GOOG":
                    go.amount += num
                  if com == "AMZN":
                    am.amount += num
                  if com == "META":
                    me.amount += num
                  if com == "GAMMA":
                    f.amount += num
        count += 1
  if sc == "c":
    class crypto:
      amount = 0
      price = 5
    bit = crypto()
    eth = crypto()
    dog = crypto()
    sol = crypto()
    okb = crypto()
    money = 10000
    count = 1
    skipper = 0
    while True:
      round(money, 2)
      fall = random.randint(4, 10)
      print("\n"*60)
      if count % fall == 0:
        bit.price = round(bit.price/random.uniform(1.4, 2), 2)
        eth.price = round(eth.price/random.uniform(1.4, 2), 2)
        dog.price = round(dog.price/random.uniform(1.4, 2), 2)
        sol.price = round(sol.price/random.uniform(1.4, 2), 2)
        okb.price = round(okb.price/random.uniform(1.4, 2), 2)
      else:
        bit.price = round(bit.price*random.uniform(0.95, 1.5), 2)
        eth.price = round(eth.price*random.uniform(0.95, 1.5), 2)
        dog.price = round(dog.price*random.uniform(0.95, 1.5), 2)
        sol.price = round(sol.price*random.uniform(0.95, 1.5), 2)
        okb.price = round(okb.price*random.uniform(0.95, 1.5), 2)
      if skipper > 0:
            count += 1
            skipper -= 1
            continue
      value = bit.amount*bit.price+eth.amount*eth.price+dog.amount*dog.price+sol.amount*sol.price+okb.amount*okb.price+money
      print("Week: ", count, "\n\nMoney: ", money, "Account Value: ", value)
      print("BITCOIN: ", bit.price, " ETHEREUM: ", eth.price, " DOGECOIN: ", dog.price, " SOLANA: ", sol.price, " OKB: ", okb.price)
      option = input(("1 to invest, 2 to sell, 3 to view what stocks you have, 4 to skip, 5 to skip 10 weeks\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
      if option == "1":
        comp = int(input("How many companies?\n"))
        for i in range(comp):
          com = input("Which company? (BTC, ETH, DOGE, SOL, OKB\n")
          num = int(input("How many"))
          if com == "BTC":
            bit.amount += num
            money -= bit.price*num
          if com == "ETH":
            eth.amount += num
            money -= eth.price*num
          if com == "DOGE":
            dog.amount += num
            money -= dog.price*num
          if com == "SOL":
            sol.amount += num
            money -= sol.price*num
          if com == "OKB":
            okb.amount += num
            money -= okb.price*num
      if option == "2":
        comp = int(input("How many companies?\n"))
        for i in range(comp):
          com = input("Which company? (BTC, ETH, DOGE, SOL, OKB\n")
          num = int(input("How many"))
          if com == "BTC":
            if num > bit.amount:
                  num = bit.amount
            bit.amount -= num
            money += bit.price*num
          if com == "ETH":
            if num > eth.amount:
                  num = eth.amount
            eth.amount -= num
            money += eth.price*num
          if com == "DOGE":
            if num > dog.amount:
                  num = dog.amount
            dog.amount -= num
            money += dog.price*num
          if com == "SOL":
            if num > sol.amount:
                  num = sol.amount
            sol.amount -= num
            money += sol.price*num
          if com == "OKB":
            if num > okb.amount:
                  num = okb.amount
            okb.amount -= num
            money += okb.price*num
      if option == "3":
        print("BITCOIN: ", aa.amount)
        print("ETHEREUM: ", ms.amount)
        print("GOOG: ", go.amount)
        print("AMZN: ", am.amount)
        print("META: ", me.amount)
        print("GAMMA Fund: ", f.amount)
        wait = input("Press enter to continue")
      if option == "4":
        count += 1
        continue
      if option == "5":
        skipper = 10
      if option == "password":
        admin = input("\n\nWelcome to ADMIN Commands:\n\nPress 1 to change the week (You can't go back in time)\nPress 2 to add to your account")
        if admin == "1":
          week = int(input("What week?"))
          skipper = week-count
        if admin == "2":
          choice1 = input("Money or stocks? (m/s)")
          if choice1 == "m":
            choice2 = int(input("How much money?"))
            money += choice2
          if choice1 == "s":
            comp = int(input("How many companies"))
            for i in range(comp):
              com = input("Which company? (BTC, ETH, DOGE, SOL, OKB)\n")
              num = int(input("How many stocks"))
              if com == "BTC":
                aa.amount += num
              if com == "ETH":
                ms.amount += num
              if com == "DOGE":
                go.amount += num
              if com == "SOL":
                am.amount += num
              if com == "OKB":
                me.amount += num
      count += 1
revx5 = "https://www.youtube.com/@realevillain"
if mode == "5" or mode0 == "5":
  class stock:
    price = 100
  st1 = stock()
  st2 = stock()
  st3 = stock()
  count = 1
  owed1 = 0
  owed2 = 0
  owed3 = 0
  money = 1000
  while True:
    print("Week: ", count)
    round(money, 2)
    print("Money: ", money)
    st1.price *= round(random.uniform(0.7, 1.25), 2)
    st2.price *= round(random.uniform(0.7, 1.25), 2)
    st3.price *= round(random.uniform(0.7, 1.25), 2)
    print("Stock 1: ", st1.price)
    print("Stock 2: ", st2.price)
    print("Stock 3: ", st3.price)
    option = input("Press 1 to borrow\nPress 2 to return (YOU CAN ONLY RETURN ALL THE STOCKS THAT YOU OWE IN ONE GO\nPress 3 to view how much of a stock you owe\nPress 4 to exit\n")
    if option == "1":
      comp = input("How many companies?\n")
      for i in range(int(comp)):
        com = input("Which company? (1, 2, 3)\n")
        num = int(input("How many stocks?\n"))
        if num > 50:
          num = 50
        if com == "1":
          owed1 += num
          money += st1.price*num
        if com == "2":
          owed2 += num
          money += st2.price*num
        if com == "3":
          owed3 += num
          money += st3.price*num
    if option == "2":
      comp = input("How many companies?\n")
      for i in range(int(comp)):
        com = input("Which company? (1, 2, 3)\n")
        if com == "1":
          money -= owed1*st1.price
          owed1 = 0
        if com == "2":
          money -= owed2*st2.price
          owed2 = 0
        if com == "3":
          money -= owed3*st3.price
          owed3 = 0
    if option == "3":
      print("Stock 1: ", owed1)
      print("Stock 2: ", owed2)
      print("Stock 3: ", owed3)
    if option == "4":
      break
    money -= (owed1+owed2+owed3)*0.2
    count += 1
if mode == "6" or mode0 == "6":
  pmode = input("Press 1 to predict a stock price\nPress 2 to compare which two stocks to buy\nPress 3 to compare which GAMMA company to buy\n")
  if pmode == "1":
    tick = yf.Ticker(input("Enter the ticker:\n"))
    dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
    dy = "-".join(dyb)
    his = tick.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
    i = ((his[-1] - his[0])/his[0])*1.03
    nprice = (((his[-1]*i)+his[-1])*0.08+(his[-1]*i)+his[-1])
    print("In a year, the price of the stock will be: ", nprice)
    print(nprice-his[-1], "$ increase")
    print(((nprice-his[-1])/his[-1])*100, "percent increase")
  if pmode == "2":
    t1n = input("Enter the first ticker:\n")
    t2n = input("Enter the second ticker:\n")
    tick1 = yf.Ticker(t1n)
    tick2 = yf.Ticker(t2n)
    dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
    dy = "-".join(dyb)
    his1 = tick1.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
    his2 = tick2.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
    i1 = ((his1[-1] - his1[0])/his1[0])*1.03
    i2 = ((his2[-1] - his2[0])/his2[0])*1.03
    nprice1 = (((his1[-1]*i1)+his1[-1])*0.08+(his1[-1]*i1)+his1[-1])
    nprice2 = (((his2[-1]*i2)+his2[-1])*0.08+(his2[-1]*i2)+his2[-1])
    if i1 > i2:
      print(t1n, "will most likely reap greater rewards\n")
      print(i1, "percent increase vs", i2)
    elif i2 > i1:
      print(t2n, "will most likely reap greater rewards\n")
      print(i2, "percent increase vs", i1)
    else:
      print("Error, could not calculate\n\n")
      print(i1, i2)
  if pmode == "3":
    dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
    dy = "-".join(dyb)
    aapl = yf.Ticker("AAPL").history(start = dy, end = date.today(), interval="3mo")['Close']
    msft = yf.Ticker("MSFT").history(start = dy, end = date.today(), interval="3mo")['Close']
    meta = yf.Ticker("META").history(start = dy, end = date.today(), interval="3mo")['Close']
    amzn = yf.Ticker("AMZN").history(start = dy, end = date.today(), interval="3mo")['Close']
    goog = yf.Ticker("GOOG").history(start = dy, end = date.today(), interval="3mo")['Close']
    aaplr = ((aapl[-1] - aapl[0])/aapl[0])*1.03
    msftr = ((msft[-1] - msft[0])/msft[0])*1.03
    metar = ((meta[-1] - meta[0])/meta[0])*1.03
    amznr = ((amzn[-1] - amzn[0])/amzn[0])*1.03
    googr = ((goog[-1] - goog[0])/goog[0])*1.03
    gre = max(aaplr, msftr, metar, amznr, googr)
    if gre == aaplr:
      print("Apple is most likely to succeed\n")
    if gre == msftr:
      print("Microsoft is most likely to succeed\n")
    if gre == metar:
      print("Meta is most likely to succeed\n")
    if gre == amznr:
      print("Amazon is most likely to succeed\n")
    if gre == googr:
      print("Google is most likely to succeed\n")
if mode == "7" or mode0 == "7":
  start = time.time()
  os.system('clear')
  tickers = [si.tickers_sp500(), si.tickers_nasdaq(), si.tickers_dow(), si.tickers_other()]
  p10 = 0
  p9 = 0
  p8 = 0
  p7 = 0
  p6 = 0
  p5 = 0
  p4 = 0
  p3 = 0
  p2 = 0
  p1 = 0
  fcount = 1
  times = []
  for i in tickers:
    for j in i:
      s = time.time()
      os.system('clear')
      print(j, fcount, "/", len(tickers[0])+len(tickers[1])+len(tickers[2])+len(tickers[3]), "   ", round((fcount/(len(tickers[0])+len(tickers[1])+len(tickers[2])+len(tickers[3])))*100, 2), "%")
      bar(round((fcount/(len(tickers[0])+len(tickers[1])+len(tickers[2])+len(tickers[3])))*100, 2))
      tick = yf.Ticker(j)
      dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
      dy = "-".join(dyb)
      try:
        his = tick.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
      except:
        continue
      try:
        r = ((his[-1] - his[0])/his[0])*1.03*1.08
      except:
        continue
      if r > p1 or p1 == 0:
        p1 = r
        d1 = j
      elif r > p2 or p2 == 0:
        p2 = r
        d2 = j
      elif r > p3 or p3 == 0:
        p3 = r
        d3 = j
      elif r > p4 or p4 == 0:
        p4 = r
        d4 = j
      elif r > p5 or p5 == 0:
        p5 = r
        d5 = j
      elif r > p6 or p6 == 0:
        p6 = r
        d6 = j
      elif r > p7 or p7 == 0:
        p7 = r
        d7 = j
      elif r > p8 or p8 == 0:
        p8 = r
        d8 = j
      elif r > p9 or p9 == 0:
        p9 = r
        d9 = j
      elif r > p10 or p10 == 0:
        p10 = r
        d10 = j
      end = time.time()
      print("Time taken: ", end-start, "s")
      fcount += 1
  os.system('clear')
  print("1: ", d1)
  print("2: ", d2)
  print("3: ", d3)
  print("4: ", d4)
  print("5: ", d5)
  print("6: ", d6)
  print("7: ", d7)
  print("8: ", d8)
  print("9: ", d9)
  print("10: ", d10)
  end = time.time()
  print("Time taken: ", end-start, "s")
if mode == "8" or mode0 == "8":
  start = time.time()
  os.system('clear')
  tickers = [si.tickers_sp500()]
  d10 = 0
  d9 = 0
  d8 = 0
  d7 = 0
  d6 = 0
  d5 = 0
  d4 = 0
  d3 = 0
  d2 = 0
  d1 = 0
  p10 = 0
  p9 = 0
  p8 = 0
  p7 = 0
  p6 = 0
  p5 = 0
  p4 = 0
  p3 = 0
  p2 = 0
  p1 = 0
  fcount = 1
  times = []
  for i in tickers:
    for j in i:
      s = time.time()
      os.system('clear')
      perc = round((fcount/len(tickers[0]))*100, 2)
      print(j, fcount, "/", len(tickers[0]), perc, "%")
      bar(perc)
      if len(times) < 20:
        print("Time Remaining: Loading...")
      else:
        sum = 0
        for o in times:
          sum += i
        sum /= len(times)
        avg = (len(tickers[0])*fcount)-(fcount*sum)
        print("Time Remaining: ", avg)
      tick = yf.Ticker(j)
      dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
      dy = "-".join(dyb)
      try:
        his = tick.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
      except:
        continue
      try:
        r = ((his[-1] - his[0])/his[0])*1.03*1.08
      except:
        continue
      if r > p1 or p1 == 0:
        p1 = r
        d1 = j
      elif r > p2 or p2 == 0:
        p2 = r
        d2 = j
      elif r > p3 or p3 == 0:
        p3 = r
        d3 = j
      elif r > p4 or p4 == 0:
        p4 = r
        d4 = j
      elif r > p5 or p5 == 0:
        p5 = r
        d5 = j
      elif r > p6 or p6 == 0:
        p6 = r
        d6 = j
      elif r > p7 or p7 == 0:
        p7 = r
        d7 = j
      elif r > p8 or p8 == 0:
        p8 = r
        d8 = j
      elif r > p9 or p9 == 0:
        p9 = r
        d9 = j
      elif r > p10 or p10 == 0:
        p10 = r
        d10 = j
      end = time.time()
      print("Time taken: ", end-start, "s")
      fcount += 1
  os.system('clear')
  print("1: ", d1)
  print("2: ", d2)
  print("3: ", d3)
  print("4: ", d4)
  print("5: ", d5)
  print("6: ", d6)
  print("7: ", d7)
  print("8: ", d8)
  print("9: ", d9)
  print("10: ", d10)
  end = time.time()
  print("Time taken: ", end-start, "s")
if mode == "9" or mode0 == "9":
  start = time.time()
  os.system('clear')
  tickers = [si.tickers_dow()]
  d10 = 0
  d9 = 0
  d8 = 0
  d7 = 0
  d6 = 0
  d5 = 0
  d4 = 0
  d3 = 0
  d2 = 0
  d1 = 0
  p10 = 0
  p9 = 0
  p8 = 0
  p7 = 0
  p6 = 0
  p5 = 0
  p4 = 0
  p3 = 0
  p2 = 0
  p1 = 0
  fcount = 1
  times = []
  for i in tickers:
    for j in i:
      s = time.time()
      os.system('clear')
      perc = round((fcount/len(tickers[0]))*100, 2)
      print(j, fcount, "/", len(tickers[0]), perc, "%")
      bar(perc)
      if len(times) < 20:
        print("Time Remaining: Loading...")
      else:
        sum = 0
        for o in times:
          sum += i
        sum /= len(times)
        avg = (len(tickers[0])*sum)-(fcount*sum)
        print("Time Remaining: ", avg)
      tick = yf.Ticker(j)
      dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
      dy = "-".join(dyb)
      try:
        his = tick.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
      except:
        continue
      try:
        r = ((his[-1] - his[0])/his[0])*1.03*1.08
      except:
        continue
      if r > p1 or p1 == 0:
        p1 = r
        d1 = j
      elif r > p2 or p2 == 0:
        p2 = r
        d2 = j
      elif r > p3 or p3 == 0:
        p3 = r
        d3 = j
      elif r > p4 or p4 == 0:
        p4 = r
        d4 = j
      elif r > p5 or p5 == 0:
        p5 = r
        d5 = j
      elif r > p6 or p6 == 0:
        p6 = r
        d6 = j
      elif r > p7 or p7 == 0:
        p7 = r
        d7 = j
      elif r > p8 or p8 == 0:
        p8 = r
        d8 = j
      elif r > p9 or p9 == 0:
        p9 = r
        d9 = j
      elif r > p10 or p10 == 0:
        p10 = r
        d10 = j
      end = time.time()
      print("Time taken: ", end-start, "s")
      fcount += 1
  os.system('clear')
  print("1: ", d1)
  print("2: ", d2)
  print("3: ", d3)
  print("4: ", d4)
  print("5: ", d5)
  print("6: ", d6)
  print("7: ", d7)
  print("8: ", d8)
  print("9: ", d9)
  print("10: ", d10)
  end = time.time()
  print("Time taken: ", end-start, "s")
if mode == "10" or mode0 == "10":
  start = time.time()
  os.system('clear')
  tickers = [si.tickers_other()]
  d10 = 0
  d9 = 0
  d8 = 0
  d7 = 0
  d6 = 0
  d5 = 0
  d4 = 0
  d3 = 0
  d2 = 0
  d1 = 0
  p10 = 0
  p9 = 0
  p8 = 0
  p7 = 0
  p6 = 0
  p5 = 0
  p4 = 0
  p3 = 0
  p2 = 0
  p1 = 0
  fcount = 1
  times = []
  for i in tickers:
    for j in i:
      s = time.time()
      os.system('clear')
      perc = round((fcount/len(tickers[0]))*100, 2)
      print(j, fcount, "/", len(tickers[0]), perc, "%")
      bar(perc)
      if len(times) < 20:
        print("Time Remaining: Loading...")
      else:
        sum = 0
        for o in times:
          sum += i
        sum /= len(times)
        avg = (len(tickers[0])*fcount)-(fcount*sum)
        print("Time Remaining: ", avg)
      tick = yf.Ticker(j)
      dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
      dy = "-".join(dyb)
      try:
        his = tick.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
      except:
        continue
      try:
        r = ((his[-1] - his[0])/his[0])*1.03*1.08
      except:
        continue
      if r > p1 or p1 == 0:
        p1 = r
        d1 = j
      elif r > p2 or p2 == 0:
        p2 = r
        d2 = j
      elif r > p3 or p3 == 0:
        p3 = r
        d3 = j
      elif r > p4 or p4 == 0:
        p4 = r
        d4 = j
      elif r > p5 or p5 == 0:
        p5 = r
        d5 = j
      elif r > p6 or p6 == 0:
        p6 = r
        d6 = j
      elif r > p7 or p7 == 0:
        p7 = r
        d7 = j
      elif r > p8 or p8 == 0:
        p8 = r
        d8 = j
      elif r > p9 or p9 == 0:
        p9 = r
        d9 = j
      elif r > p10 or p10 == 0:
        p10 = r
        d10 = j
      end = time.time()
      print("Time taken: ", end-start, "s")
      fcount += 1
  os.system('clear')
  print("1: ", d1)
  print("2: ", d2)
  print("3: ", d3)
  print("4: ", d4)
  print("5: ", d5)
  print("6: ", d6)
  print("7: ", d7)
  print("8: ", d8)
  print("9: ", d9)
  print("10: ", d10)
  end = time.time()
  print("Time taken: ", end-start, "s")
if mode == "11" or mode0 == "11":
  start = time.time()
  os.system('clear')
  tickers = [si.tickers_other()]
  d10 = 0
  d9 = 0
  d8 = 0
  d7 = 0
  d6 = 0
  d5 = 0
  d4 = 0
  d3 = 0
  d2 = 0
  d1 = 0
  p10 = 0
  p9 = 0
  p8 = 0
  p7 = 0
  p6 = 0
  p5 = 0
  p4 = 0
  p3 = 0
  p2 = 0
  p1 = 0
  fcount = 1
  times = []
  for i in tickers:
    for j in i:
      s = time.time()
      os.system('clear')
      perc = round((fcount/len(tickers[0]))*100, 2)
      print(j, fcount, "/", len(tickers[0]), perc, "%")
      bar(perc)
      if len(times) < 20:
        print("Time Remaining: Loading...")
      else:
        sum = 0
        for o in times:
          sum += i
        sum /= len(times)
        avg = (len(tickers[0])*fcount)-(fcount*sum)
        print("Time Remaining: ", avg)
      tick = yf.Ticker(j)
      dyb = [str(int(date.today().strftime("%Y")) - 1), str(date.today().strftime("%m")), str(date.today().strftime("%d"))]
      dy = "-".join(dyb)
      try:
        his = tick.history(start=dy, end=date.today().strftime("%Y-%m-%d"), interval="3mo")['Close']
      except:
        continue
      try:
        r = ((his[-1] - his[0])/his[0])*1.03*1.08
      except:
        continue
      if r > p1 or p1 == 0:
        p1 = r
        d1 = j
      elif r > p2 or p2 == 0:
        p2 = r
        d2 = j
      elif r > p3 or p3 == 0:
        p3 = r
        d3 = j
      elif r > p4 or p4 == 0:
        p4 = r
        d4 = j
      elif r > p5 or p5 == 0:
        p5 = r
        d5 = j
      elif r > p6 or p6 == 0:
        p6 = r
        d6 = j
      elif r > p7 or p7 == 0:
        p7 = r
        d7 = j
      elif r > p8 or p8 == 0:
        p8 = r
        d8 = j
      elif r > p9 or p9 == 0:
        p9 = r
        d9 = j
      elif r > p10 or p10 == 0:
        p10 = r
        d10 = j
      e = time.time()
      times.append(e-s)
      fcount += 1
  os.system('clear')
  print("1: ", d1)
  print("2: ", d2)
  print("3: ", d3)
  print("4: ", d4)
  print("5: ", d5)
  print("6: ", d6)
  print("7: ", d7)
  print("8: ", d8)
  print("9: ", d9)
  print("10: ", d10)
  end = time.time()
  print("Time taken: ", end-start, "s")
tupcred = (revx1, revx2, revx3, revx4, revx5)
credc(" ".join(tupcred))