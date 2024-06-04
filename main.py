from interface import Interface
from data import Data

# Load data
data = Data()

# Create Interface
interface = Interface()
# Setup Interface
interface.set_up_windows()
interface.set_up_canvas()
interface.new_card_text(remove=True)


# Buttons actions
interface.right_button.config(command=lambda: interface.new_card_text(remove=True))
interface.wrong_button.config(command=lambda: interface.new_card_text())

# Mainloop window
interface.windows.mainloop()

