"""Compact duration parsing. See docs/TASK-DEV-1__spec__parse-duration.md."""


def parse_duration(text):
    """Return the number of seconds in a compact duration string such as "1h30m"."""
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("parse_duration accepts str only")
    
    # Strip leading and trailing whitespace
    text = text.strip()
    
    # Check for empty string
    if not text:
        raise ValueError("Invalid duration format")
    
    # Define unit mapping
    units = {
        'w': 604800,
        'd': 86400,
        'h': 3600,
        'm': 60,
        's': 1
    }
    
    # Parse the string
    result = 0
    i = 0
    used_units = set()
    
    # Keep track of last unit to ensure descending order
    last_unit_index = -1
    
    while i < len(text):
        # Find the number part (must be at least one digit)
        start = i
        while i < len(text) and text[i].isdigit():
            i += 1
        
        if i == start:
            raise ValueError("Invalid duration format")
        
        # Extract number and convert to int (this handles leading zeros automatically)
        number_str = text[start:i]
        number = int(number_str)
        
        # Get the unit
        if i >= len(text):
            raise ValueError("Invalid duration format")
            
        unit = text[i]
        
        # Validate unit
        if unit not in units:
            raise ValueError("Invalid duration format")
        
        # Check if unit was already used
        if unit in used_units:
            raise ValueError("Invalid duration format")
        
        # Check order (must be in strictly descending unit order)
        unit_index = ['w', 'd', 'h', 'm', 's'].index(unit)
        if unit_index >= last_unit_index:
            raise ValueError("Invalid duration format")
        
        # Add to result
        result += number * units[unit]
        used_units.add(unit)
        last_unit_index = unit_index
        i += 1
    
    return result
