from pathlib import Path
from Utility import csvreader, filewriter


# get path of current folder
script_path = Path(__file__).parent
# get path to csv file
csv_path = script_path.joinpath('resources/election_data.csv')
# set output file path
out_path = script_path.joinpath('analysis/election_data_output.txt')


def aggregate_election_data(data):

    # instantiate dictionary
    results = dict()

    for row in data:
        candidate = row['Candidate']

        # increment vote count if candidate already in results set
        if candidate in results:
            results[candidate] += 1
        # add key to results set if candidate doesn't exist
        else:
            results[candidate] = 1

    return results


def get_vote_total(data):
    # returns total vote count

    return len(data)


def calculate_vote_percentage(aggregate_data, total_votes):

    # instantiate dictionaty
    results = dict()

    # loop through each candidate in the aggregate and calculate percentage of votes
    for candidate, votes in aggregate_data.items():

        results[candidate] = (votes / total_votes) * 100

    
    return results

def get_winner(aggregate_data):
    # returns name of winner of popular vote

    winner = {'name': '',
                'votes': 0} 

    # loop through vote totals for each candidate
    for candidate, votes in aggregate_data.items():

        # replace winner if vote total is higher
        if votes > winner['votes']:
            winner['name'] = candidate
            winner['votes'] = votes

    return winner['name']


def format_results_string(vote_total, aggregate_votes, vote_percent, winner):
    
    # set initial output string
    output_string = (
        f'Election Results \n'
        f'-------------------------- \n'
        f'Total Votes: {vote_total} \n'
        f'-------------------------- \n'
    )

    # add each candidate to output string
    for candidate, votes in aggregate_votes.items():
        output_string += f'{candidate}: {vote_percent.get(candidate):.3f}% ({votes}) \n'


    # add winner to output string
    output_string += (
        f'-------------------------- \n'
        f'Winner: {winner} \n'
        f'-------------------------- \n'
    )

    return output_string
    


def main():

    # read election data from file
    election_data = csvreader.read_csv_to_list(csv_path)
    
    # aggregatu election results
    election_aggregate = aggregate_election_data(election_data)

    # count the total number of votes
    vote_total = get_vote_total(election_data)

    # calculate the percentage of votes each candidate received
    vote_percentage = calculate_vote_percentage(election_aggregate, vote_total)

    # calculate winner
    winner_name = get_winner(election_aggregate)

    # get results string
    results_string = format_results_string(vote_total, election_aggregate, vote_percentage, winner_name)

    # print results_string to console
    print(results_string)

    # write results_string to file
    filewriter.write_file(out_path, results_string)


if __name__ == '__main__':
    main()