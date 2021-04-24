import json
import pprint
pp = pprint.PrettyPrinter(indent=2)
import xlwt
from xlwt import Workbook

wb = Workbook()

transactions = json.load(open("data.json"))["transactions"]

type_dict = {}

for t in transactions:
    t_type = t["type"]
    if t_type in type_dict:
        type_dict[t_type] += [t]
    else:
        type_dict[t_type] = [t]

# for t_type in type_dict.keys():
#    print(t_type, len(type_dict[t_type]))


def parse_crypto_withdrawals():

    crypto_withdrawals_sheet = wb.add_sheet("Crypto withdrawals")
    style = xlwt.easyxf("font: bold 1")

    crypto_withdrawals_sheet.write(0, 0, "type", style)
    crypto_withdrawals_sheet.write(0, 1, "id", style)
    crypto_withdrawals_sheet.write(0, 2, "date", style)
    crypto_withdrawals_sheet.write(0, 3, "from wallet", style)
    crypto_withdrawals_sheet.write(0, 4, "from amount", style)
    crypto_withdrawals_sheet.write(0, 5, "from currency", style)
    crypto_withdrawals_sheet.write(0, 6, "tx destination", style)
    crypto_withdrawals_sheet.write(0, 7, "tx url or hash", style)
    crypto_withdrawals_sheet.write(0, 8, "withdrawal net value (SEK)", style)

    for i, t in enumerate(type_dict["crypto_withdrawal"]):
        row = i + 1
        crypto_withdrawals_sheet.write(row, 0, "Crypto withdrawal")
        crypto_withdrawals_sheet.write(row, 1, t["id"])
        crypto_withdrawals_sheet.write(row, 2, t["date"])
        crypto_withdrawals_sheet.write(row, 3, t["from"]["wallet"]["name"])
        crypto_withdrawals_sheet.write(row, 4, t["from"]["amount"])
        crypto_withdrawals_sheet.write(row, 5, t["from"]["currency"]["symbol"])
        crypto_withdrawals_sheet.write(row, 6, t["txdest"])

        if t["txurl"] is None:
            crypto_withdrawals_sheet.write(row, 7, t["txhash"])
        else:
            crypto_withdrawals_sheet.write(row, 7, t["txurl"])

        crypto_withdrawals_sheet.write(row, 8, t["net_value"])

def parse_crypto_deposits():

    crypto_deposits_sheet = wb.add_sheet("Crypto deposits")
    style = xlwt.easyxf("font: bold 1")

    crypto_deposits_sheet.write(0, 0, "type", style)
    crypto_deposits_sheet.write(0, 1, "id", style)
    crypto_deposits_sheet.write(0, 2, "date", style)
    crypto_deposits_sheet.write(0, 3, "to amount", style)
    crypto_deposits_sheet.write(0, 4, "to currency", style)
    crypto_deposits_sheet.write(0, 5, "to wallet", style)
    crypto_deposits_sheet.write(0, 6, "tx destination", style)
    crypto_deposits_sheet.write(0, 7, "tx url or hash", style)
    crypto_deposits_sheet.write(0, 8, "deposit net value (SEK)", style)

    for i, t in enumerate(type_dict["crypto_deposit"]):
        row = i + 1
        crypto_deposits_sheet.write(row, 0, "Crypto deposit")
        crypto_deposits_sheet.write(row, 1, t["id"])
        crypto_deposits_sheet.write(row, 2, t["date"])
        crypto_deposits_sheet.write(row, 3, t["to"]["amount"])
        crypto_deposits_sheet.write(row, 4, t["to"]["currency"]["symbol"])
        crypto_deposits_sheet.write(row, 5, t["to"]["wallet"]["name"])
        crypto_deposits_sheet.write(row, 6, t["txdest"])

        if t["txurl"] is None:
            crypto_deposits_sheet.write(row, 7, t["txhash"])
        else:
            crypto_deposits_sheet.write(row, 7, t["txurl"])

        crypto_deposits_sheet.write(row, 8, t["net_value"])

    wb.save('test.xls')


def parse_exchanges():

    exchanges_sheet = wb.add_sheet("Exchanges")
    style = xlwt.easyxf("font: bold 1")

    exchanges_sheet.write(0, 0, "type", style)
    exchanges_sheet.write(0, 1, "id", style)
    exchanges_sheet.write(0, 2, "date", style)
    exchanges_sheet.write(0, 3, "exchange place", style)
    exchanges_sheet.write(0, 4, "from amount", style)
    exchanges_sheet.write(0, 5, "from currency", style)
    exchanges_sheet.write(0, 6, "to amount", style)
    exchanges_sheet.write(0, 7, "to currency", style)
    exchanges_sheet.write(0, 8, "transaction net value (SEK)", style)

    for i, t in enumerate(type_dict["exchange"]):
        row = i + 1
        exchanges_sheet.write(row, 0, "Exchange")
        exchanges_sheet.write(row, 1, t["id"])
        exchanges_sheet.write(row, 2, t["date"])
        exchanges_sheet.write(row, 3, t["from"]["wallet"]["name"])
        exchanges_sheet.write(row, 4, t["from"]["amount"])
        exchanges_sheet.write(row, 5, t["from"]["currency"]["symbol"])
        exchanges_sheet.write(row, 6, t["to"]["amount"])
        exchanges_sheet.write(row, 7, t["to"]["currency"]["symbol"])
        exchanges_sheet.write(row, 8, t["net_value"])

    wb.save('test.xls')


def parse_sells():

    sell_sheet = wb.add_sheet("Sells")
    style = xlwt.easyxf("font: bold 1")

    sell_sheet.write(0, 0, "type", style)
    sell_sheet.write(0, 1, "id", style)
    sell_sheet.write(0, 2, "date", style)
    sell_sheet.write(0, 3, "from amount", style)
    sell_sheet.write(0, 4, "from currency", style)
    sell_sheet.write(0, 5, "to amount", style)
    sell_sheet.write(0, 6, "to currency", style)
    sell_sheet.write(0, 7, "transaction net value (SEK)", style)


    for i, t in enumerate(type_dict["sell"]):
        row = i + 1
        sell_sheet.write(row, 0, "Sell")
        sell_sheet.write(row, 1, t["id"])
        sell_sheet.write(row, 2, t["date"])
        sell_sheet.write(row, 3, t["from"]["amount"])
        sell_sheet.write(row, 4, t["from"]["currency"]["symbol"])
        sell_sheet.write(row, 5, t["to"]["amount"])
        sell_sheet.write(row, 6, t["to"]["currency"]["symbol"])
        sell_sheet.write(row, 7, t["net_value"])

    wb.save('test.xls')


def parse_transfers():
    transfer_sheet = wb.add_sheet("Transfers")
    style = xlwt.easyxf("font: bold 1")

    transfer_sheet.write(0, 0, "type", style)
    transfer_sheet.write(0, 1, "id", style)
    transfer_sheet.write(0, 2, "date", style)
    transfer_sheet.write(0, 3, "amount", style)
    transfer_sheet.write(0, 4, "currency", style)
    transfer_sheet.write(0, 5, "from wallet name", style)
    transfer_sheet.write(0, 6, "to wallet name", style)
    transfer_sheet.write(0, 7, "txurl", style)
    transfer_sheet.write(0, 8, "transaction net value (SEK)", style)

    for i, t in enumerate(type_dict["transfer"]):
        row = i + 1
        transfer_sheet.write(row, 0, "Transfer")
        transfer_sheet.write(row, 1, t["id"])
        transfer_sheet.write(row, 2, t["date"])
        transfer_sheet.write(row, 3, t["from"]["amount"])
        transfer_sheet.write(row, 4, t["from"]["currency"]["symbol"])
        transfer_sheet.write(row, 5, t["from"]["wallet"]["name"])
        transfer_sheet.write(row, 6, t["to"]["wallet"]["name"])

        if t["txurl"] is None:
            transfer_sheet.write(row, 7, t["txhash"])
        else:
            transfer_sheet.write(row, 7, t["txurl"])

        transfer_sheet.write(row, 8, t["net_value"])

    wb.save('test.xls')


def parse_buys():
    buy_sheet = wb.add_sheet("Buys")
    style = xlwt.easyxf("font: bold 1")

    buy_sheet.write(0, 0, "type", style)
    buy_sheet.write(0, 1, "id", style)
    buy_sheet.write(0, 2, "date", style)
    buy_sheet.write(0, 3, "from amount", style)
    buy_sheet.write(0, 4, "from currency", style)
    buy_sheet.write(0, 5, "to amount", style)
    buy_sheet.write(0, 6, "to currency", style)
    buy_sheet.write(0, 7, "transaction net value (SEK)", style)

    for i, t in enumerate(type_dict["buy"]):
        row = i + 1
        buy_sheet.write(row, 0, "Buy")
        buy_sheet.write(row, 1, t["id"])
        buy_sheet.write(row, 2, t["date"])
        buy_sheet.write(row, 3, t["from"]["amount"])
        buy_sheet.write(row, 4, t["from"]["currency"]["symbol"])
        buy_sheet.write(row, 5, t["to"]["amount"])
        buy_sheet.write(row, 6, t["to"]["currency"]["symbol"])
        buy_sheet.write(row, 7, t["net_value"])

    wb.save('test.xls')


def parse_fiat_withdrawals():

    fiat_withdrawals_sheet = wb.add_sheet("Fiat withdrawals")
    style = xlwt.easyxf("font: bold 1")

    fiat_withdrawals_sheet.write(0, 0, "type", style)
    fiat_withdrawals_sheet.write(0, 1, "id", style)
    fiat_withdrawals_sheet.write(0, 2, "date", style)
    fiat_withdrawals_sheet.write(0, 3, "destination", style)
    fiat_withdrawals_sheet.write(0, 4, "destination", style)
    fiat_withdrawals_sheet.write(0, 5, "amount", style)
    fiat_withdrawals_sheet.write(0, 6, "currency", style)
    fiat_withdrawals_sheet.write(0, 7, "transaction net value (SEK)", style)

    for i, t in enumerate(type_dict["fiat_withdrawal"]):
        row = i + 1
        fiat_withdrawals_sheet.write(row, 0, "Fiat withdrawal")
        fiat_withdrawals_sheet.write(row, 1, t["id"])
        fiat_withdrawals_sheet.write(row, 2, t["date"])
        fiat_withdrawals_sheet.write(row, 3, t["txdest"])
        fiat_withdrawals_sheet.write(row, 4, t["from"]["wallet"]["name"])
        fiat_withdrawals_sheet.write(row, 5, t["from"]["amount"])
        fiat_withdrawals_sheet.write(row, 6, t["from"]["currency"]["symbol"])
        fiat_withdrawals_sheet.write(row, 7, t["net_value"])

    wb.save('test.xls')


def parse_fiat_deposits():
    # FIAT DEPOSITS
    fiat_deposits_sheet = wb.add_sheet("Fiat deposits")
    style = xlwt.easyxf("font: bold 1")

    fiat_deposits_sheet.write(0, 0, "type", style)
    fiat_deposits_sheet.write(0, 1, "id", style)
    fiat_deposits_sheet.write(0, 2, "date", style)
    fiat_deposits_sheet.write(0, 3, "source", style)
    fiat_deposits_sheet.write(0, 4, "destination", style)
    fiat_deposits_sheet.write(0, 5, "amount", style)
    fiat_deposits_sheet.write(0, 6, "currency", style)
    fiat_deposits_sheet.write(0, 7, "transaction net value (SEK)", style)

    for i, t in enumerate(type_dict["fiat_deposit"]):
        row = i + 1
        fiat_deposits_sheet.write(row, 0, "Fiat deposit")
        fiat_deposits_sheet.write(row, 1, t["id"])
        fiat_deposits_sheet.write(row, 2, t["date"])
        fiat_deposits_sheet.write(row, 3, t["txsrc"])
        fiat_deposits_sheet.write(row, 4, t["to"]["wallet"]["name"])
        fiat_deposits_sheet.write(row, 5, t["to"]["amount"])
        fiat_deposits_sheet.write(row, 6, t["to"]["currency"]["symbol"])
        fiat_deposits_sheet.write(row, 7, t["net_value"])

    wb.save('test.xls')


if __name__ == "__main__":
    parse_crypto_withdrawals()
    parse_crypto_deposits()
    parse_exchanges()
    parse_fiat_deposits()
    parse_fiat_withdrawals()
    parse_buys()
    parse_transfers()
    parse_sells()
    print("done")

