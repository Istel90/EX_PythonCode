#%%
import sys
sys.path.append(r"C:\Users\gur75\새 폴더\TempPythonCode")
from RasterGDAL import RasterGDAL
import numpy as np
import math
from queue import PriorityQueue
import geopandas as gpd
#%%
class AStar:
    _direction_vector_to_distance = {
        (-1, 0): 1,
        (1, 0): 1,
        (0, -1): 1,
        (0, 1): 1,
        (-1, -1): math.sqrt(2), # comment out when needed
        (-1, 1): math.sqrt(2), # comment out when needed
        (1, -1): math.sqrt(2), # comment out when needed
        (1, 1): math.sqrt(2), # comment out when needed
    }
    def __init__(self, gridmap):
        """0 is open, 1 is obstacle."""
        self._gridmap = gridmap    
    @classmethod
    def from_shapefile(cls, shapefile_path):
        gridmap = gpd.read_file(shapefile_path)
        gridmap_array = gridmap['id'].values.reshape(gridmap.shape)
        return cls(gridmap_array)
    def search(self, start, goal):
        """Unreachable goal returns None for routes"""
        if not self._is_valid_coord(start) or not self._is_valid_coord(goal):
            raise ValueError("An invalid coord of start or goal")
        if start == goal:
            return [], 0
        coord_to_precoord = {}
        coord_to_g_cost = {start: 0}
        candidates = PriorityQueue()
        candidates.put((0, start))
        while not candidates.empty():
            _, current_coord = candidates.get()
            if current_coord == goal:
                break
            row, col = current_coord
            for (drow, dcol), distance in AStar._direction_vector_to_distance.items():
                coord = (row + drow, col + dcol)
                if not self._is_valid_coord(coord):
                    continue
                g_cost = coord_to_g_cost[current_coord] + distance
                if g_cost < coord_to_g_cost.get(coord, math.inf):
                    coord_to_g_cost[coord] = g_cost
                    h_cost = math.dist(coord, goal)
                    f_cost = g_cost + h_cost
                    candidates.put((f_cost, coord))
                    coord_to_precoord[coord] = current_coord
        if goal not in coord_to_precoord:
            return None, math.inf
        routes = []
        route = goal
        while True:
            route = coord_to_precoord[route]
            if route == start:
                break
            routes.append(route)
        return list(reversed(routes)), coord_to_g_cost[goal]
    def _is_valid_coord(self, coord):
        row, col = coord
        if row < 0 or col < 0:
            return False
        if row >= len(self._gridmap) or col >= len(self._gridmap[0]):
            return False
        if self._gridmap[row][col] == 1:
            return False
        return True
    
#%% Parameters
#개체하나
Baseraster = r"D:\download\포천시\MyProject4\F10.tif"
#건물맵
Bgrid2 = r"D:\download\포천시\MyProject4\Feature_N3A_3.tif"
#개체머지
Bgrid1 = r"D:\download\포천시\MyProject4\모든개체.tif"
# Newraster = r"D:\download\포천시\MyProject4\포천DEM.tif"
# Bgridmap =  r"C:\Users\gur75\Desktop\포천멧돼지\PYTHONDATA\gridmap.tif"
#%%
rc = RasterGDAL(Bgrid1)
ga = rc.RasterToArray()
gr = np.where( ga[0] == ga[1], 0, 1 )
print(np.unique(gr))
gr.shape
#%%
ReadClass = RasterGDAL(Bgrid2)
GetArray = ReadClass.RasterToArray()
# ReadClass.ConstRaster(r"C:\Users\gur75\Desktop\포천멧돼지\PYTHONDATA\Const.tif")
# GetArray2 = ReadClass.RasterToArray(r"C:\Users\gur75\Desktop\포천멧돼지\PYTHONDATA\Const.tif")[0]
grid = np.where( GetArray[0] == GetArray[1], 0, 1)
print(np.unique(grid))
print(grid)
grid.shape
AA = np.array(gr)
BB = np.array(grid)
realgrid = BB - AA
#%%
# GetArray2 = ReadClass.RasterToArray(Newraster)[0]
ReadClass2 = RasterGDAL(Baseraster)
GetArray2 = ReadClass2.RasterToArray()
array = GetArray2[0]
NodataVal = GetArray2[1]
array.shape
print(NodataVal)
print(array)
GetArray2[0]
GetArray[1]
result2 = np.where( GetArray2[0] == GetArray[1], 0, GetArray2[0])
print(np.unique(result2))
#%%
#A는 몇장인지 알아보기
A = np.unique(result2)
A.size
array.shape[0]
array.shape[1]
IndexArray = np.zeros((A.size, array.shape[0], array.shape[1]))
print(np.unique(IndexArray).size)
IndexArray.shape[2]
#%%
# i에 
for i, j in zip(A, range(IndexArray.shape[0]) ): 
    IndexArray[j] = np.where( array == i, 1 , 0 )
    print(i, j)
IndexArray[0]
# IndexArray 
print(np.unique(IndexArray))
IndexArray[0] = np.zeros((array.shape[0], array.shape[1]))
#%%
for j in range(IndexArray.shape[0]):
    print(j)
print(np.shape(IndexArray))
result = []
# range 각 장마다 확인이 필요함
for n in range(171):
    indices = np.argwhere(IndexArray[n] == 1)
    result.extend([(n, x, y) for x, y in indices])
result = np.array(result)
print(result.shape)
print(type(indices))
#%%
# Example NumPy array
numpy_array = result
numpy_array.shape
def main():
    gridmap = realgrid
    astar = AStar(gridmap)
    all_routes = []  # Initialize an empty list to store the routes
    
    for i in range(len(numpy_array) - 1):
        current_point = numpy_array[i][1:]  # Extract current point (y, z)
        next_point = numpy_array[i + 1][1:]  # Extract next point (y, z)
        start = tuple(current_point)
        goal = tuple(next_point)
        routes, distance = astar.search(start, goal)
        
        # Extract the routes and append to the list in order
        all_routes.extend(routes)
        print("Routes:", " -> ".join(map(str, [start, *routes, goal])))
        print("Distance:", distance)
        print("Start:", start)
        print("Goal:", goal)
        print()       
    return all_routes
if __name__ == "__main__":
    result_routes = main()
    print("All Routes:", result_routes)
#%%
import numpy as np
from osgeo import gdal
def create_geotiff(array, output_path, geotransform=None, projection=None, nodata_value=None):
    """
    Create a GeoTIFF file from a NumPy array.
    :param array: NumPy array containing the data.
    :param output_path: Output file path for the GeoTIFF.
    :param geotransform: Optional geotransform information (6 values).
    :param projection: Optional projection information (WKT format).
    :param nodata_value: Optional nodata value.
    """
    driver = gdal.GetDriverByName('GTiff')
    rows, cols = array.shape
    if geotransform is None:
        geotransform = (0, 10, 0, 0, 0, -10)  # Default geotransform
    if projection is None:
        projection = ''  # Default projection (empty)
    if nodata_value is None:
        nodata_value = -9999  # Default nodata value
    dataset = driver.Create(output_path, cols, rows, 1, gdal.GDT_Float64)
    dataset.SetGeoTransform(geotransform)
    dataset.SetProjection(projection)
    band = dataset.GetRasterBand(1)
    band.WriteArray(array)
    band.SetNoDataValue(nodata_value)
    band.FlushCache()
    dataset.FlushCache()
# Example usage:
array1 = np.zeros((4747, 3138))
for i in result_routes:
    array1[i] = 1
output_path = r'D:\download\포천시\MyProject4\R_F1_output.tif'
projection = 'PROJCS["Korea 2000 / Korea Unified Coordinate System",GEOGCS["Korea 2000",DATUM["Korea_2000",SPHEROID["GRS 1980",6378137,298.257222101,AUTHORITY["EPSG","7019"]],AUTHORITY["EPSG","6162"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4162"]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",38],PARAMETER["central_meridian",127.5],PARAMETER["scale_factor",0.9996],PARAMETER["false_easting",1000000],PARAMETER["false_northing",2000000],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Easting",EAST],AXIS["Northing",NORTH],AUTHORITY["EPSG","5179"]]'
create_geotiff(array1, output_path, projection=projection)
#%%
import matplotlib.pyplot as plt
import numpy as np
# Define the routes as a list of coordinates
routes = result_routes
# Generate a time series for the routes
time_series = np.linspace(0, 1, len(routes))
# Extract the x and y coordinates from the routes
x_coords, y_coords = zip(*routes)
# Plot the routes with a color gradient
plt.scatter(x_coords, y_coords, c=time_series, cmap='viridis_r', linewidth=0.5)
plt.scatter(x_coords[0], y_coords[0], color='blue', label='Start')
plt.scatter(x_coords[-1], y_coords[-1], color='red', label='Goal')
# Add colorbar
cbar = plt.colorbar()
cbar.set_label('Time')
# Add labels and gridlines
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
# Show the legend
plt.legend()
# Display the plot
plt.show()