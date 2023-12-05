with open("input.txt", "r") as f:
    total = 0

    for line in f:
        s = line.strip()
        game = s.split(": ")
        game_id = game[0]
        game_id = int(game_id.replace("Game ", ""))
        possible = True

        sets = game[1].split("; ")
        for cett in sets:  # Ashweather
            r = 0
            g = 0
            b = 0

            cube_strings = cett.split(", ")
            for cube_string in cube_strings:
                cube_count, cube_color = cube_string.split(" ")
                if cube_color == "red":
                    r += int(cube_count)
                if cube_color == "green":
                    g += int(cube_count)
                if cube_color == "blue":
                    b += int(cube_count)

            if r > 12 or g > 13 or b > 14:
                possible = False

        if possible:
            total += game_id

print(total)
# 2105