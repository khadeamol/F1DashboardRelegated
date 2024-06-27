from time import time
import matplotlib.pyplot as plt
import fastf1 as ff
import fastf1.plotting
import pandas as pd

fastf1.plotting.setup_mpl(misc_mpl_mods=False)
ff.Cache.enable_cache("Cache")


def plot_traces(yearSel, raceSel, sessionSel, driver1, lapNumber = None):
    print("Entered plot trace")
    session = ff.get_session(yearSel, raceSel, sessionSel)
    session.load()
    if lapNumber:
        print("Custom lap")
        driver1_lap = session.laps.pick_driver(driver1).pick_lap(int(lapNumber))
        print(driver1_lap)
    else:
        driver1_lap = session.laps.pick_driver(driver1).pick_fastest()
        print(driver1_lap)
    
    driver1_tel = driver1_lap.get_car_data().add_distance()
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(driver1_tel['Distance'], driver1_tel['Speed'], color = 'Yellow', label = driver1)
    ax.set_xlabel('Distance in m')
    ax.set_ylabel('Speed in km/h')

    plt.suptitle(f"Lap traces")
    return plt.show()
    
    # driver1_lap = pd.DataFrame(driver1_lap)
    # return driver1_lap


# print(plot_traces(2024, 'Miami', 'Q', 'VER', 10))