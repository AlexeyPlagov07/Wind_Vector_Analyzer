def avg(x):
  import math
  t_w_x = []
  t_w_y = []
  for i in range(len(x)):
    try:
      wind_speed_1 = x[i * 2]
      wind_direction_degrees_1 = x[(i * 2) + 1]
      wind_direction_radians_1 = math.radians(wind_direction_degrees_1)
      wind_x_component = wind_speed_1 * math.cos(wind_direction_radians_1)
      wind_y_component = wind_speed_1 * math.sin(wind_direction_radians_1)
      t_w_x.append(wind_x_component)
      t_w_y.append(wind_y_component)
    except IndexError:
      x.append('')

  total_x_component = sum(t_w_x)
  total_y_component = sum(t_w_y)
  average_wind_speed = math.sqrt(total_x_component**2 + total_y_component**2)

  average_wind_direction_radians = math.atan2(total_y_component,
                                              total_x_component)
  average_wind_direction_degrees = math.degrees(average_wind_direction_radians)
  if average_wind_direction_degrees < 0:
    average_wind_direction_degrees += 360
  elif average_wind_direction_degrees >= 360:
    average_wind_direction_degrees -= 360

  print("Average Wind Speed:", average_wind_speed, "m/s")
  print("Average Wind Direction:", average_wind_direction_degrees, "degrees")
