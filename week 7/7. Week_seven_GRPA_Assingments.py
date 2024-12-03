# GRPA 1
# Initialize a dictionary to store win counts for each team
teams = {
    "CSK": 0,
    "DC": 0,
    "KKR": 0,
    "MI": 0,
    "PK": 0,
    "RR": 0,
    "RCB": 0,
    "SH": 0
}

# Taking 8 lines of input from the user
for _ in range(8):
    line = input().strip()  # Read input and strip any extra spaces
    teams_in_line = line.split(',')
    winning_team = teams_in_line[0]
    teams[winning_team] += len(teams_in_line) - 1  # Update wins for the first team

# Sort teams by win counts (descending) and alphabetically by team name if tied
sorted_teams = sorted(teams.items(), key=lambda x: (-x[1], x[0]))

# Print the result in the required format
for team, wins in sorted_teams:
    print(f"{team}:{wins}")


# GRPA 2
def merge(D1, D2, priority):
    """
    Merge two dictionaries.

    Arguments: 
        - D1: first dictionary
        - D2: second dictionary
        - priority: string, "first" or "second", determines which dictionary's value to retain in case of common keys.
    
    Returns:
        - D: merged dictionary where:
            - If a key exists in both D1 and D2, the value is retained based on the `priority`.
            - If a key only exists in one of the dictionaries, the corresponding value is added to D.

    Example:
        D1 = {"a": 1, "b": 2, "c": 3}
        D2 = {"b": 4, "c": 5, "d": 6}
        merge(D1, D2, "first") -> {'a': 1, 'b': 2, 'c': 3, 'd': 6}
        merge(D1, D2, "second") -> {'a': 1, 'b': 4, 'c': 5, 'd': 6}
    """
    
    # Create a new dictionary to store the merged result
    D = {}

    # Add all key-value pairs from D1 to D
    D.update(D1)

    # Merge the key-value pairs from D2 into D
    for key, value in D2.items():
        if key in D:
            # If the key exists in both dictionaries, decide based on priority
            if priority == "first":
                continue  # Keep the value from D1, don't update D
            elif priority == "second":
                D[key] = value  # Update with the value from D2
        else:
            D[key] = value  # Add the key-value pair from D2 if not in D1

    return D
#GRPA 3 
def minor_matrix(M, i, j):
    """
    Compute the "minor matrix" by removing the i-th row and j-th column from the matrix M.

    Arguments:
        M: list of lists (square matrix)
        i: integer (index of the row to remove)
        j: integer (index of the column to remove)

    Returns:
        M_ij: list of lists (minor matrix with i-th row and j-th column removed)
    """
    # Create the minor matrix by removing the i-th row and j-th column
    return [
        [M[x][y] for y in range(len(M)) if y != j]  # Exclude the j-th column
        for x in range(len(M)) if x != i  # Exclude the i-th row
    ]
#GRPA 3 
def minor_matrix(M, i, j):
    """
    Compute the "minor matrix" by removing the i-th row and j-th column from the matrix M.

    Arguments:
        M: list of lists (square matrix)
        i: integer (index of the row to remove)
        j: integer (index of the column to remove)

    Returns:
        M_ij: list of lists (minor matrix with i-th row and j-th column removed)
    """
    # Create the minor matrix by removing the i-th row and j-th column
    return [
        [M[x][y] for y in range(len(M)) if y != j]  # Exclude the j-th column
        for x in range(len(M)) if x != i  # Exclude the i-th row
    ]
# GRPA 4

import json

def create_station_dict(n):
    """
    Create a nested dictionary of train details.

    Arguments:
    - n: integer, number of trains
    
    Returns:
    - A nested dictionary with train names as keys and another dictionary 
      containing compartment names and passenger counts.
    """
    station_dict = {}  # Initialize the station dictionary
    
    # Read the input for each train
    for _ in range(n):
        train_name = input().strip()  # Read train name
        m = int(input().strip())  # Read number of compartments
        
        # Create an inner dictionary for the compartments
        train_dict = {}
        
        # For each compartment, store the compartment name and passengers
        for _ in range(m):
            comp_data = input().strip().split(',')
            comp_name = comp_data[0].strip()
            passengers = int(comp_data[1].strip())
            train_dict[comp_name] = passengers
        
        # Add the train's inner dictionary to the station_dict
        station_dict[train_name] = train_dict
    
    return station_dict

# Reading the number of trains from the user
n = int(input().strip())

# Calling the function to create the station_dict
station_dict = create_station_dict(n)

# Print the resulting dictionary in JSON format with sorted keys and indentation
#print(json.dumps(station_dict, sort_keys=True, indent=2))
