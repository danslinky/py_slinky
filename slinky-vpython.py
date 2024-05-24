import numpy as np
import vpython as vp

length_ranges = [2,3,4,5,6,7,8,9,10] 
amp_ranges = [5,10,20]
f_ranges = [5,10,20]

curve = 1000
low = 0 

colors = [vp.color.red, vp.color.green, vp.color.blue, vp.color.yellow, vp.color.orange, vp.color.purple, vp.color.white, vp.color.black]


for length in length_ranges:
    for amp in amp_ranges:
        for f in f_ranges:
            high = np.pi*length

            y = np.linspace(low, high, curve)
            x = amp*np.cos(f*y)
            z = amp*np.sin(f*y)

            # Create a curve object
            # spiral = vp.curve(color=vp.color.yellow)
            spiral = vp.curve(color=colors[np.random.randint(0, len(colors))])

            for i in range(len(x)):
                # Add a point to the curve
                spiral.append(vp.vector(x[i], y[i], z[i]))

                # Limit the animation speed
                vp.rate(100)

            # Clear the curve for the next animation
            spiral.clear()