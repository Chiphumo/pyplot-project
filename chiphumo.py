import matplotlib.pyplot as plt
def scatter_plot():
    my_file= open('C:/Users/MY PC/Downloads/x_y_coordinates.txt','r')
    x_coords=[]
    y_coords=[]

    my_file.readline()
    for line in my_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))
    for item in x_coords:
        print(item)
    for item in y_coords :
        print (item)
    plt.scatter(x_coords,y_coords)
    plt.show()
scatter_plot()