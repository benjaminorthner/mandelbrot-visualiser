import pygame, math
from pygame.locals import *

pygame.init()

display_width = 600
display_height = 400

MAX_ITER = 200
PIXELSCALE = 0.006
SCALEFACTOR = 100
CENTER_RE = display_width / 2
CENTER_IM = display_height / 2

center_re = 0
center_im = 0

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


image = pygame.display.set_mode((display_width, display_height))


def pertuBrot(c):
    A = 1
    B = 0
    C = 0
    n = 0
    while n < MAX_ITER:
        A = 2*c*A + 1
        B = 2*c*B + A * A
        C = 2*c*C+2*A*B
        n += 1



def mandelbrot(c):
    z = complex(0)
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


# draws mandelbrot set centered at C_RE and C_IM (these are numbers not pixels)
def drawMandelbrot(C_RE, C_IM):
    # males global center variables changable in function
    global center_re, center_im

    # sets the new center
    center_re = C_RE
    center_im = C_IM

    # loops through all pixels
    for i in range(0, display_width):
        for j in range(0, display_height):
            # converts pixel coord into complex coords (depends on center and pixelscale)
            re = PIXELSCALE * (i - display_width/2) + center_re
            im = PIXELSCALE * (j - display_height/2) + center_im

            # colors pixel if in mandelbrot and plots it
            shade = 254 - int(mandelbrot(complex(re, im)) * 254 / MAX_ITER)
            pixel(i, j, (shade, shade, shade))

        # creates sweeping effect
        if i % 1 == 0:
            pygame.display.flip()


def pixel(i, j, color):
    pygame.draw.line(image, color, (i,j), (i,j))


def main():
    global PIXELSCALE, MAX_ITER
    # drawMandelbrot(-0.7454267337349909, 0.11300846385944266)
    # drawMandelbrot(-0.745425653735327, 0.11300879985930466)
    drawMandelbrot(-1.249783, 0.029353)


    # count = 0
    # while count < 300:
    #     pygame.image.save(image, "images/"+(str(count)+".png"))
    #
    #     PIXELSCALE /= 1.096478196
    #     MAX_ITER = int(-math.log(PIXELSCALE, 1.5) * 35)
    #     drawMandelbrot(center_re, center_im)
    #
    #     print(count)
    #     count += 1
    #
    # pygame.quit()
    # quit()

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                # does zooming
                # scales resolution so that can keep zooming

                if event.key == K_KP_PLUS:
                    PIXELSCALE /= SCALEFACTOR

                    #MAX_ITER = int(-math.log(PIXELSCALE, 1.5) * 35 )
                    drawMandelbrot(center_re, center_im)
                    print("Iterations: ",MAX_ITER)
                    print("Center: (", center_re, ", ", center_im, " * i)")

                elif event.key == K_KP_MINUS:
                    PIXELSCALE *= SCALEFACTOR

                    #MAX_ITER = int(-math.log(PIXELSCALE *100, 1.5) * 35)
                    drawMandelbrot(center_re, center_im)
                    print("Iterations: ", MAX_ITER)
                    print("Center: (", center_re, ", ", center_im, " * i)")

                elif event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

            elif event.type == MOUSEBUTTONDOWN:
                # gets mouse click pos
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # converts mouse pos into complex number based on pixelscale and center
                mouse_re = PIXELSCALE * (mouse_x - display_width / 2) + center_re
                mouse_im = PIXELSCALE * (mouse_y - display_height / 2) + center_im
                # draws mandelbrot centered at mouse pos
                drawMandelbrot(mouse_re, mouse_im)

            elif event.type == QUIT:
                pygame.quit()
                quit()


main()

# perturbation theory
# https://math.stackexchange.com/questions/939270/perturbation-of-mandelbrot-set-fractal
# http://mathr.co.uk/mandelbrot/perturbation.pdf

# speed improvements
# http://www.mrob.com/pub/muency/speedimprovements.html
