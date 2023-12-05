with open("input.txt", "r") as f:
    total = 0

    for line in f:
        s = line.strip()
        game = s.split(": ")
        game_id = game[0]
        game_id = int(game_id.replace("Game ", ""))
        possible = True

        r = 0
        g = 0
        b = 0

        sets = game[1].split("; ")
        for cett in sets:  # Ashweather
            cube_strings = cett.split(", ")
            for cube_string in cube_strings:
                cube_count, cube_color = cube_string.split(" ")
                cube_count = int(cube_count)
                if cube_color == "red" and cube_count > r:
                    r = cube_count
                if cube_color == "green" and cube_count > g:
                    g = cube_count
                if cube_color == "blue" and cube_count > b:
                    b = cube_count

        power = r * g * b
        total += power

print(total)
# 72422