import json
import pprint
import datetime
from dateutil import parser

import xlwt
from xlwt import Workbook

wb = Workbook()

pp = pprint.PrettyPrinter(indent=2)
YEAR = 2020


def transaction_in_fiscal_year(transaction):
    date = parser.parse(transaction["date"])
    return date.year == YEAR


def input_trades_into_spreadsheet(trades):
    trades_sheet = wb.add_sheet("Trades")
    style = xlwt.easyxf("font: bold 1")

    trades_sheet.write(0, 0, "Token", style)
    trades_sheet.write(0, 1, "Amount", style)
    trades_sheet.write(0, 2, "Cost basis", style)
    trades_sheet.write(0, 3, "Sell value", style)
    trades_sheet.write(0, 4, "Koinly gain", style)
    trades_sheet.write(0, 5, "Fee", style)

    for i, t in enumerate(trades):
        row = i + 1
        trades_sheet.write(row, 0, t["from"]["currency"]["symbol"])
        trades_sheet.write(row, 1, t["from"]["amount"])
        trades_sheet.write(row, 2, t["from"]["cost_basis"])
        trades_sheet.write(row, 3, t["net_value"])

        koinly_gain = float(t["gain"])

        trades_sheet.write(row, 4, str(round(koinly_gain, 2)))
        trades_sheet.write(row, 5, t["fee_value"])

    wb.save('test.xls')


def get_token(transaction):
    return transaction["from"]["currency"]["symbol"]

def is_winner(transaction):
    return float(t["gain"]) > 0


transactions = json.load(open("data.json"))["transactions"]

type_dict = {}

for t in transactions:
    t_type = t["type"]
    if t_type in type_dict:
        type_dict[t_type] += [t]
    else:
        type_dict[t_type] = [t]

for t_type in type_dict.keys():
    print(t_type, len(type_dict[t_type]))

taxable_transactions = [t for t in transactions if t["type"] in ["sell", "exchange"] and transaction_in_fiscal_year(t)]
taxable_transactions.reverse()

tokens = {}

for t in taxable_transactions:

    token = get_token(t)
    if token not in tokens:
        tokens[token] = {
            "winners": [],
            "losers": []
        }

    if is_winner(t):
        tokens[token]["winners"] += [t]
    else:
        tokens[token]["losers"] += [t]


# from token name: t.from.currency.symbol
# from token amount: t.from.amount
# from token cost basis: t.from.cost_basis

# tx fee value: t.fee_value

# sell_value: t.net_value
# gain (for reference?): t.gain


def sum_transactions(transactions):
    if len(transactions) is 0:
        return None

    token_name = transactions[0]["from"]["currency"]["symbol"]
    sum_gain = 0
    sum_cost_basis = 0
    sum_sell_price = 0
    sum_amount = 0

    for t in transactions:
        sum_gain += float(t["gain"])
        sum_cost_basis += float(t["from"]["cost_basis"])
        sum_sell_price += float(t["net_value"])
        sum_amount += float(t["from"]["amount"])

    return {
        "token": token_name,
        "gain": sum_gain,
        "cost_basis": sum_cost_basis,
        "sell_price": sum_sell_price,
        "amount": sum_amount
    }


def summary_to_spreadsheet(sheet, summary, row):
    if summary is None:
        return

    sheet.write(row, 0, summary["amount"])
    sheet.write(row, 1, summary["token"])
    sheet.write(row, 2, summary["sell_price"])
    sheet.write(row, 3, summary["cost_basis"])

    if summary["gain"] > 0:
        sheet.write(row, 4, summary["gain"])
    else:
        sheet.write(row, 5, summary["gain"])


summary_sheet = wb.add_sheet("Summary")
summary_sheet.write(0, 0, "Amount")
summary_sheet.write(0, 1, "Token")
summary_sheet.write(0, 2, "Sell value")
summary_sheet.write(0, 3, "Cost basis")
summary_sheet.write(0, 4, "Profit")
summary_sheet.write(0, 5, "Loss")

for index, token in enumerate(tokens.keys()):
    row = 2 * (index + 1)
    win_summary = sum_transactions(tokens[token]["winners"])
    loss_summary = sum_transactions(tokens[token]["losers"])

    summary_to_spreadsheet(summary_sheet, win_summary, row)
    summary_to_spreadsheet(summary_sheet, loss_summary, row + 1)


wb.save("summary.xls")

