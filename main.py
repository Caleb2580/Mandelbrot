import time
import numpy as np
import matplotlib.pyplot as plt
import pygame as pg


def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, ymax, width)
    y = np.linspace(ymin, ymax, width)
    mset = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot(c, max_iter)
    
    return mset


def run():
    running = True

    pg.init()

    xmin, xmax, ymin, ymax = -2, 1, -0, 1.5
    xmi, xma, ymi, yma = -2, 1, -1.5, 0
    xx = .4
    yy = .4
    x_change = .75
    y_change = .75
    width, height = 1000, 1000
    max_iter = 100

    zoom = 1.5

    screen = pg.display.set_mode((width, height))

    print(xx - x_change, xx + x_change, yy - y_change, yy + y_change)
    mandelbrot_image = mandelbrot_set(xx - x_change, xx + x_change, yy - y_change, yy + y_change, width, height, max_iter)
    # mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    dif = .5

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHTBRACKET:
                    x_change *= dif
                    y_change *= dif
                    print(x_change, y_change)
                    mandelbrot_image = mandelbrot_set(xx - x_change, xx + x_change, yy - y_change, yy + y_change, width, height, max_iter)
                elif event.key == pg.K_LEFTBRACKET:
                    x_change *= dif
                    y_change *= dif
                    print(x_change, y_change)
                    mandelbrot_image = mandelbrot_set(xx - x_change, xx + x_change, yy - y_change, yy + y_change, width, height, max_iter)
                    
                    
        
        for i in range(len(mandelbrot_image)):
            for j in range(len(mandelbrot_image[i])):
                # print(i, j, mandelbrot_image[i, j])
                cv = mandelbrot_image[i, j]
                red = (cv / max_iter * 255)
                c = (red, red, red)
                screen.set_at((j, i), c)
        
        pg.display.flip()


if __name__ == '__main__':

    # xmin, xmax, ymin, ymax = -2, 1, -1.5, 1.5
    # width, height = 1000, 1000
    # max_iter = 30

    # mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    # plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap='hot')
    # plt.colorbar()
    # plt.show()
    run()

























