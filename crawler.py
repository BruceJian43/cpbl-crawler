import tkinter as tk

import cpbl_info
import windows_setting

if __name__ == '__main__':
	current_window = tk.Tk()
	windows_setting.init_selecting_team_window(current_window)
	current_window.mainloop()

	if windows_setting.selected == 1:
		current_window = tk.Tk()

		windows_setting.init_result_window(current_window)
		windows_setting.add_current_standing(current_window)
		windows_setting.add_team_ranking(current_window)

		current_window.mainloop()