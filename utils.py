# Calculate the bottom right screen position
def calculate_position(screen_geometry, window_width, window_height):

    x_position = screen_geometry.width() - window_width
    y_position = screen_geometry.height() - window_height
    return x_position, y_position