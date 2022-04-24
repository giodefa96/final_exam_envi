from pathlib import Path
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
from geopy.geocoders import Nominatim
import numpy as np
from scipy.cluster.hierarchy import single, complete, average, ward, dendrogram

import cartopy.crs as ccrs

import xarray as xr

from eofs.xarray import Eof


class SearchingModelPath:

    def __init__(self, searching_model_path=None):
        self.searching_model_path = searching_model_path

    def searching_model_path(name: str):

        """Insert the name string of the model so i can reach for you"""
        try:
            path_home = Path.home()
            path_directory = path_home / 'Desktop/Unimib/Data Science/Second Year/Physics and environmental data ' \
                                         'lab/Environmental/Materiale Corso/Model Folder '
            path_model = path_directory / name
            if not path_model.exists():
                sys.exit()
            return path_model
        except SystemExit:
            print('Insert string and valid model name')


def searching_model_path(name: str):

    """Insert the name string of the model so i can reach for you"""
    try:
        path_home = Path.home()
        path_directory = path_home / 'Desktop/Unimib/Data Science/Second Year/Physics and environmental data ' \
                                     'lab/Environmental/Materiale Corso/Final_ex/Model Folder '
        path_model = path_directory / name
        if not path_model.exists():
            sys.exit()
        return path_model
    except SystemExit:
        print('Insert string and valid model name')


def plot_part_of_map(ens,a,b,c,d):
    """Plot a part of a map"""

    d1_nat = ens.sel(lat=slice(a,b), lon=slice(c,d))
    psl_nat=d1_nat.ens_mean
    fig = plt.figure(figsize=(30,24))  # x,y(inches)

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_title(''.join(['ciao','\n']))
    ax.set_global()
    mm = ax.contourf(psl_nat.lon, psl_nat.lat, psl_nat.mean(axis=0), transform=ccrs.PlateCarree(), cmap='jet')

    ax.coastlines()
    ax.gridlines(draw_labels=True)

    # add colorbar
    cbar_ax = fig.add_axes([0.28, 0.10, 0.46, 0.05])
    cbar = fig.colorbar(mm, cax=cbar_ax, extend='both', orientation='horizontal')
    # [left, bottom, width, height]
    cbar.set_label('Temperature')
    cbar.ax.tick_params(labelsize=8)

    plt.show()
    plt.close()

    return


def point(city: str):

    geolocator = Nominatim(user_agent="google")
    location = geolocator.geocode(city)
    print((location.latitude, location.longitude))
    lat = (int(location.latitude)+90)
    lon = (int(location.longitude)+180)
    box = int(((lat) * ((lon)))/2)
    ens = xr.load_dataset('/home/giodefa/Desktop/Unimib/Data Science/Second Year/Physics and environmental data '
                          'lab/Environmental/Materiale Corso/Final_ex/final_exam_envi/bozza/model_ens.nc')
    print(f"L'area selezionata è {location.address} e fa parte del cluster numero {kmeans.labels_[int(box)-1]}")
    plot_part_of_map(ens,int(location.latitude),int(location.latitude)+2,int(location.longitude),int(location.longitude)+2)
    return


def hierarchical_clustering(distance_matrix, method='complete'):
    if method == 'complete':
        Z = complete(distance_matrix)
    if method == 'single':
        Z = single(distance_matrix)
    if method == 'average':
        Z = average(distance_matrix)
    if method == 'ward':
        Z = ward(distance_matrix)

    fig = plt.figure(figsize=(16, 8))
    dn = dendrogram(Z)
    plt.title(f"Dendrogram for {method}-linkage with correlation distance")
    plt.show()
    return Z