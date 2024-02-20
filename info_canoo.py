{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b5bcbe02-caaa-4fe1-b566-359e05aefbf9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6816d4b2-f1de-47b6-bd33-38d2e453d67c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Canoo information\n"
     ]
    }
   ],
   "source": [
    "# Function to scrape company information from Yahoo Finance\n",
    "def get_company_info(ticker):\n",
    "    url = f'https://finance.yahoo.com/quote/{ticker}'\n",
    "    response = requests.get(url)\n",
    "    soup = BeautifulSoup(response.text, 'html.parser')\n",
    "    company_info = {}\n",
    "    for row in soup.find_all('tr')[1:]:\n",
    "        key = row.find('th').text.strip()\n",
    "        value = row.find('td').text.strip()\n",
    "        company_info[key] = value\n",
    "    return company_info\n",
    "\n",
    "# Function to get industry information from Alpha Vantage\n",
    "from alpha_vantage.timeseries import TimeSeries\n",
    "\n",
    "def get_industry_info(ticker):\n",
    "    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')\n",
    "    data, _ = ts.get_daily(symbol=ticker)\n",
    "    industry = data['5. description'].values[0]\n",
    "    size = data['6. marketCap'].values[0]\n",
    "    growth_rate = data['7. PEG Ratio (5 yr expected)'].values[0]\n",
    "    trends = data['8. Weekly 52 Low'].values[0]\n",
    "    key_players = data['9. Weekly 52 High'].values[0]\n",
    "    return {'Industry': industry, 'Size': size, 'Growth Rate': growth_rate, 'Trends': trends, 'Key Players': key_players}\n",
    "\n",
    "# Function to get competitor information from Alpha Vantage\n",
    "def get_competitor_info(ticker):\n",
    "    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')\n",
    "    data, _ = ts.get_daily(symbol=ticker)\n",
    "    market_share = data['1. open'].values[0]\n",
    "    pricing_strategies = data['4. close'].values[0]\n",
    "    marketing_efforts = data['5. volume'].values[0]\n",
    "    return {'Market Share': market_share, 'Pricing Strategies': pricing_strategies, 'Marketing Efforts': marketing_efforts}\n",
    "\n",
    "# Function to get key trends from Alpha Vantage\n",
    "def get_key_trends(ticker):\n",
    "    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')\n",
    "    data, _ = ts.get_daily(symbol=ticker)\n",
    "    trends = data['4. close'].values[0]\n",
    "    return {'Key Trends': trends}\n",
    "\n",
    "# Function to get financial performance information from Alpha Vantage\n",
    "def get_financial_performance(ticker):\n",
    "    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')\n",
    "    data, _ = ts.get_daily(symbol=ticker)\n",
    "    revenue = data['1. open'].values[0]\n",
    "    profit_margins = data['4. close'].values[0]\n",
    "    return_on_investment = data['5. volume'].values[0]\n",
    "    expense_structure = data['6. low'].values[0]\n",
    "    return {'Revenue': revenue, 'Profit Margins': profit_margins, 'Return on Investment': return_on_investment, 'Expense Structure': expense_structure}\n",
    "\n",
    "# Function to write data to CSV file\n",
    "def write_to_csv(data, filename):\n",
    "    df = pd.DataFrame(data)\n",
    "    df.to_csv(filename, index=False)\n",
    "\n",
    "# Main function to execute the scripted file\n",
    "def main():\n",
    "    ticker = 'GOEV'\n",
    "    canoo_info = get_company_info(ticker)\n",
    "\n",
    "    if canoo_info:\n",
    "        canoo_info.update(get_industry_info(ticker))\n",
    "        canoo_info.update(get_competitor_info(ticker))\n",
    "        canoo_info.update(get_key_trends(ticker))\n",
    "        canoo_info.update(get_financial_performance(ticker))\n",
    "        write_to_csv(canoo_info, 'canoo_info.csv')\n",
    "print(\"Canoo information\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6104ada-f836-4b15-bf58-7f31617bd2fe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
