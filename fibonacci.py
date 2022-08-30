def dispense_fibonnaci(sequence_number):
    if sequence_number <= 1:
        return sequence_number
    else:
        return(dispense_fibonnaci(sequence_number - 1) + dispense_fibonnaci(sequence_number - 2))

result = dispense_fibonnaci(19)
print(result)