#################
### Intersect ###
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

c1 = Circle([6,12,4])
c2 = Circle([10,12,4])
c3 = Circle([6,8,4])
c4 = Circle([10,8,4])
clist = [c1,c2,c3,c4]

fig,ax = plt.subplots()
ax.set_xlim((0, 20))
ax.set_ylim((0, 20))
plt.grid(b=True, which='major', color='grey', linestyle='--')
plt.xticks(np.arange(0, 21, 2.0))
plt.yticks(np.arange(0, 21, 2.0))
for c in clist:
    cplot = plt.Circle((c.x,c.y), c.r, color='blue', fill=False)
    ax.add_artist(cplot)

intersectpoints = c1.intersect(Circle(clist).drop(0))
for p in intersectpoints: #np.array(intersectpoints).reshape(-1,2):
    intplot = plt.scatter(p.x,p.y)
    ax.add_artist(intplot)
### Intersect ###
#################





#####################
### Encompassment ###
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np
    
mc = Circle([c1,c2])

x_min = int(min(mc.x-max(mc.r)))-1
x_max = int(max(mc.x+max(mc.r)))+1
y_min = int(min(mc.y-max(mc.r)))-1
y_max = int(max(mc.y+max(mc.r)))+1
n_points = 1000
random_x = np.random.uniform(x_min, x_max, n_points).reshape(-1,1)
random_y = np.random.uniform(y_min, y_max, n_points).reshape(-1,1)
random_r = np.random.uniform(0.1, 0.5, n_points).reshape(-1,1)

fig,ax = plt.subplots()
fig.set_size_inches(15,10)
ax.set_xlim((x_min, x_max))
ax.set_ylim((y_min, y_max))
random_c = Circle([np.dstack([random_x, random_y, random_r])])
random_p = random_c.xy
for c in mc:
    cplot = plt.Circle((c.x, c.y), c.r, color='black', fill=False)
    ax.add_artist(cplot)
for c in random_c:
    if mc.encompass(c).any():
        circle_color = 'red'
        cplot = plt.Circle((c.x, c.y), c.r, color=circle_color, alpha=0.5)
        ax.add_artist(cplot)
    else:
        circle_color = 'blue'

for p in random_p:
    if mc.encompass(p).any():
        point_color = 'blue'
        pplot = plt.scatter(p.x, p.y, c=point_color, alpha=0.5)
        ax.add_artist(pplot)
    else:
        point_color = 'red'
### Encompassment ###
#####################





#######################
### Circle clusters ###
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

mc1 = Circle.random(5,10,5,25,1,3,10)
mc2 = Circle.random(20,25,5,25,1,3,10)
multic = Circle(np.append(mc1,mc2,axis=0))

multic.calc_intersections()
multic.calc_clusters()
multic._clusters_indices
result = [multic.get_cluster(_) for _ in range(multic.nr_clusters)]

fig,ax = plt.subplots()
fig.set_size_inches(15,10)
ax.set_xlim((0, 30))
ax.set_ylim((0, 30))
for i, resultc in enumerate(result):
    colors = ['black','red','blue','orange','green','yellow','pink']
    for c in resultc:
        cplot = plt.Circle((c.x, c.y), c.r, color=colors[i], fill=False)
        ax.add_artist(cplot)
### Circle clusters ###
#######################





#########################################################
### correct index of intersections of cluster-results ###
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

plt.ioff()

p3 = Point([15,7])
p4 = Point([16,6])
p = Point([p3,p4])
multic = Circle.populate_lines(p, nr_circles=15, radius_min=1, radius_max=4)
multic.calc_intersections()
multic.calc_clusters()
some_cluster = multic.get_cluster(0)

for j in range(len(some_cluster)):
    for k in range(len(some_cluster)):
        if j==k:
            break
        fig,ax = plt.subplots()
        fig.set_size_inches(15,10)
        ax.set_xlim((0, 30))
        ax.set_ylim((0, 30))
        indices = [j, k]
        for i in indices:
            cplot = plt.Circle((some_cluster[i].x,some_cluster[i].y), some_cluster[i].r, fill=False)
            ax.add_artist(cplot)
        intercepts = some_cluster.intersections[indices[0]]
        intercepting_index = indices[1]-1 if indices[1]>indices[0] else indices[1]
        i1, i2 = intercepts[0][intercepting_index], intercepts[1][intercepting_index]
        plt.scatter(i1.x, i1.y)
        plt.scatter(i2.x, i2.y)
        filename = str(j)+str(k)
        fig.savefig(filename)
        plt.close(fig)
        
plt.ion()
### correct index of intersections of cluster-results ###
#########################################################





#####################
### angle between ###
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

p = Point([[8,8],[8,12],[12,12],[12,8]])
cp = Point([10,10])

i = 3
plt.scatter(p.x,p.y)
plt.scatter(cp.x,cp.y, c='red')
plt.scatter(p[i].x,p[i].y, marker='P', c='black', alpha=.5, s=250)
p.drop(i).orderedPoints(cp, return_angles=True)
p.drop(i).orderedPoints(cp, p[i], return_angles=True)
### angle between ###
#####################





###########################################
### Polygon encompass - point per point ### 
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

poly = Point([[5,5],[5,10],[7.5,7.5],[10,10],[10,8],[8,6],[10,5],[5,5]])
multip = Point.random(4,11,4,11, 5000)
for p in multip:
    isin = poly.polyEncompass(p)
    if isin:
        plt.scatter(p.x, p.y, color="green")
    else:
        plt.scatter(p.x, p.y, color="orange", alpha=.25)
### Polygon encompass - point per point ###
###########################################
###########################################
### Polygon encompass - multiple points ### 
from geom.circl import Circle, Point

poly = Point([[5,5],[5,10],[7.5,7.5],[10,10],[10,8],[8,6],[10,5],[5,5]])
for i in range(2500):
    multip = Point.random(4,11,4,11,2)
    isin = poly.polyEncompass(multip)
    if isin:
        plt.scatter(multip.x, multip.y, color="green")
    else:
        plt.scatter(multip.x, multip.y, color="orange", alpha=.25)
### Polygon encompass - multiple points ### 
###########################################
        
        
 


#####################################
### outer bound - random clusters ###
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

multic = Circle.random(5,30,5,30,1,3,100)

fig,ax = plt.subplots()
fig.set_size_inches(15,10)
ax.set_xlim((0, 35))
ax.set_ylim((0, 35))

multic.calc_intersections()
multic.calc_clusters()

for i in range(multic.nr_clusters):
    cluster = multic.get_cluster(i)
    
    if len(cluster)==1:
        c = cluster[0]
        cplot = plt.Circle((c.x, c.y), c.r, color='blue', fill=True, alpha=.25)
        ax.add_artist(cplot)
        
    if len(cluster)==2:
        for c in cluster:
            cplot = plt.Circle((c.x, c.y), c.r, color='orange', fill=True, alpha=.25)
            ax.add_artist(cplot)
        
    if len(cluster)>2:
        # For every cluster...
        for c in cluster:
            cplot = plt.Circle((c.x, c.y), c.r, color='green', fill=True, alpha=.25)
            ax.add_artist(cplot)
            
        cluster.calc_boundaries()
        # Get the outer boundaries & Circles. 
        ordered_b, _ = cluster.outer_boundaries
        # Close the loop.
        ordered_all = Point([ordered_b[-1]]+ordered_b)
        # Scatter boundaries and plot segments in dotted lines.
        plt.scatter(ordered_all.x, ordered_all.y, color='black')
        plt.plot(ordered_all.x, ordered_all.y, c='black')
        
        # For every hole in the cluster...
        for inner_boundary in cluster.inner_boundaries:
            # Get the boundaries & Circles. 
            ordered_b, _ = inner_boundary
            # Close the loop.
            ordered_all = Point([ordered_b[-1]]+ordered_b)
            # Scatter boundaries and plot segments in dotted lines.
            plt.scatter(ordered_all .x, ordered_all .y, c='green')
            plt.plot(ordered_all .x, ordered_all .y, c='green', ls='--')
            
        # Calculate Area (and edge case circles)
        A, o, i = cluster.flatArea(return_edge_cases=True)
        plt.scatter(o.x, o.y, c='black', marker='P')
        try:
            plt.scatter(i.x, i.y, c='green', marker='_')     
        except:
            i=None
### outer bound - random clusters ###
##################################### 





#######################################
### Testing cluster area vs mc area ### 
from geom.circl import Circle, Point
from matplotlib import pyplot as plt
import numpy as np

# Square without inner hole
mc = Circle.random(15,25,15,25,0,4,30)
fig,ax = plt.subplots()
fig.set_size_inches(15,10)
ax.set_xlim((0, 35))
ax.set_ylim((0, 35))
for c in mc:
    cplot = plt.Circle((c.x, c.y), c.r, color='blue', fill=False, alpha=.5)
    ax.add_artist(cplot)


mc.calc_intersections()
mc.calc_clusters()
cluster = mc.get_cluster(0)
cluster.calc_boundaries()

# Exact
a = cluster.flatArea()
# Simulation
b = cluster.simArea(30000)

print(a,b)
### Testing cluster area vs mc area ### 
#######################################