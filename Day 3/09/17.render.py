





def render(width, heght, symbol="%"):
      first_line = symbol * width + "\n"

      middle_lines = (symbol + " " * (width-2) + symbol + "\n") * (heght-2)

      last_line = "#" * width

      return first_line + middle_lines + last_line

print(render (10, 12))