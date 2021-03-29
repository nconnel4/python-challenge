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



def main():

    # read election data from file
    election_data = csvreader.read_csv_to_list(csv_path)
    
    # aggregaet election results
    election_aggregate = aggregate_election_data(election_data)

    # count the total number of votes
    vote_total = get_vote_total(election_data)


if __name__ == '__main__':
    main()