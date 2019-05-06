import click
import csv
import random

candidate_pool = dict()
pick_pool = dict()

@click.command()
@click.option('--count', default=12, show_default=True, help='Number of candidates to pick')
@click.option('--partylist', default=False, help='Include Party List to pool')
@click.option('--full_dump', default=False, help='Dump all candidate/party list info in results')
def vote_by_python(count, partylist, full_dump):
    with open('candidates.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)    

        for row in csv_reader:
            key = f'candidate#{row["no"]}'
            value = {"ballot_name": row["ballot"], "name": row["name"], "party": row["party"]}
            candidate_pool[key] = value

    if partylist:
        add_partylist_to_pool()

    # do selection
    exec_py_select(count)
    print('Loaded and Generated Candidate Pool!')

    # show results
    print('Results:')
    for key in pick_pool.keys():
        if full_dump:
            print(f'{key} - {pick_pool[key]}')
        else:
            print(f'{key} - {pick_pool[key]["ballot_name"]}')

def add_partylist_to_pool():
    with open('party_list2.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            key = f'party#{row["no"]}'
            value = {"ballot_name": row["ballot"], "name": row["name"]}
            candidate_pool[key] = value

def exec_py_select(count):
    for pick in range(count):
        key, value = random.choice(list(candidate_pool.items()))
        pick_pool[key] = value

        candidate_pool.pop(key)



if __name__ == '__main__':
    vote_by_python()