import dearpygui.dearpygui as dpg

dpg.create_context()


def callback(sender, data):
    print("Button Pressed")


with dpg.window(label="Tutorial", pos=(200, 200), width=800, height=200) as win1:
    dpg.add_text("Type cron: 'At 04:05.'")
    dpg.add_input_text(default_value="Type your answer here", width=270, height=750)
    dpg.add_button(label="submit", callback=callback)


dpg.create_viewport(title='Custom Title', width=1330, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

