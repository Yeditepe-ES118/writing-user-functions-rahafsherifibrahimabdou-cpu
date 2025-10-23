import numpy as np 

def throw_rock(m, v0, theta):
    
    g = 9.81 #in m/s^2 
    theta = theta * np.pi / 180 #in rad 
    tf = 2 * v0 * np.sin(theta)/ g #in s 
    R = v0**2 * np.sin(2*theta) / g #in m 
    hm = v0**2 * np.sin(theta)**2 / (2*g) #in m 
    vh = v0 * np.cos(theta) #in m/s
    kh = 0.5 * m * vh * hm * 2 #in J\
    print("For a rock with %5.3f kg mass "\
          "thrown with %5.3f m/s at an angle of "\
          "%6.2f degrees:\nTime of flight is %10.1e s\n"\
          "the range in x-direction is %10.1e m\n"\
          "Maximum height is %10.1e m\n"\
          "The speed at maximum height is %10.1e m\n"\
          "Kinetic enerfy at the maximum height is %8.2e J"%(m, v0, theta * 180 / np.pi, tf, R, hm, vh, kh))
    return tf,R,hm,vh,kh



        
    