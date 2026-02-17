def find_first_duplicate(transactions):
    # We use a set because looking things up in a set is O(1) - instant!
    seen = set()
    dup = list()
    
    for amount in transactions:
        print(f"Checking amount: {amount}")
        print(f"Seen so far: {seen}")
        if amount in seen:
            dup.append(amount)
        seen.add(amount)
            
        
        # If we haven't seen it, add it to the set
        
    #seen.add(amount)
    print(f"duplicate found: {dup}")
        
    return "No duplicates found."

# Test it out
txns = [10, 20, 30, 40, 30,20, 50,10,50,50]
print(find_first_duplicate(txns))