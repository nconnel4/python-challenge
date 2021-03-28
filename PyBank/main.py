from pathlib import Path
from Utility import csvreader

# get path of current folder
script_path = Path(__file__).parent
# get path to csv file
csv_path = script_path.joinpath('resources/budget_data.csv')

def get_profit_values(data):
    # loops through data and gets the net profit and change in profit

    #instantiate net_profit, total_change, and previous_profit
    net_profit = 0
    total_change = 0
    previous_profit = None

    # instantiate greatest profit increase and decrease
    greatest_increase = {'date': '',
                        'profit_change': 0}
    greatest_decrease = {'date': '',
                        'profit_change': 0}

    for row in data:
        current_profit = int(row['Profit/Losses'])

        net_profit += current_profit

        # check if previous_profit is defined
        if not previous_profit is None:
            profit_change = get_profit_change(previous_profit, current_profit)
            total_change += profit_change


            # check profit change values greater than previous greatest_increase
            if profit_change > greatest_increase['profit_change']:
                greatest_increase['date'] = row['Date']
                greatest_increase['profit_change'] = profit_change
            # check profit change values less than previous greatest_increase
            elif profit_change < greatest_decrease['profit_change']:
                greatest_decrease['date'] = row['Date']
                greatest_decrease['profit_change'] = profit_change
        
        # set previous_profit equal to current_profit for next iteration
        previous_profit = current_profit

    return net_profit, total_change, greatest_increase, greatest_decrease

def get_profit_change(previous_month, current_month):

    return current_month - previous_month

def __main__():
    # import csv file to dictionary list
    bank_data = csvreader.read_csv_to_list(csv_path)

    # get total_months
    total_months = len(bank_data)

    #calculate the net profits
    net_profit, total_change, greatest_increase, greatest_decrease = get_profit_values(bank_data)
    print(total_months, net_profit, total_change, greatest_increase, greatest_decrease)

if __name__ == '__main__':
    __main__()