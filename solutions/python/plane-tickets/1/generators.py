"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seats = ["A", "B", "C", "D"]
    n = 0
    z = n
    while n < number:
        z = n%4
        yield seats[z]
        n += 1
        



def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    seats = ["A", "B", "C", "D"]
    n = 0
    z = 0
    row = 0
    while n < number:
        z = n%4
        if (z == 0):
            row += 1
            if row == 13:
                row += 1
        
        yield str(row) + seats[z]
        n += 1
        

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))
    result = {}
    for passenger in passengers:
        result[passenger] = next(seats)
    
    return result


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        initial_id = seat + flight_id
        id_zeroes_length = 12 - len(initial_id)
        yield initial_id + "0"*id_zeroes_length
