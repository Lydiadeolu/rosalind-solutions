# Key decisions: Python strings are 0-indexed. Because Rosalind slice boundaries 
# are inclusive, we adjust the stop index by adding 1 (+1) to match Python's 
# exclusive upper-bound slicing design.

def slice_string_segments(s, a, b, c, d):
    slice1 = s[a : b + 1]
    slice2 = s[c : d + 1]
    return f"{slice1} {slice2}"

if __name__ == "__main__":
    try:
        with open("python_village/Dateset/rosalind_ini3.txt" ) as file:
            # Read lines and strip out trailing newline characters
            lines = [line.strip() for line in file.readlines()]
            
            text_string = lines[0]
            # Convert the space-separated numbers on line 2 into integers
            a, b, c, d = map(int, lines[1].split())
            
            print(slice_string_segments(text_string, a, b, c, d))
            
    except FileNotFoundError:
        # Fallback test example from Rosalind description
        sample_str = "HumptyDumptySatOnAWallHumptyDumptyHadAGreatFallAllTheKingsHorsesAndAllTheKingsMenCouldntPutHumptyTogetherAgain"
        print("File not found, using test example ")
        print(slice_string_segments(sample_str, 22, 27, 97, 102))
