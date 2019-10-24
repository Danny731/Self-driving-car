import sensor, image, time, math, pyb
from pyb import Pin


p_out = Pin('P1', Pin.OUT)
p_out.low()
po = Pin('P2', Pin.OUT)
po.low()


s1 = pyb.Servo(1)
s2 = pyb.Servo(2)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    img.lens_corr(1.8)

    matrices = img.find_datamatrices()
    for matrix in matrices:
        img.draw_rectangle(matrix.rect(), color = (255, 0, 0))
        print_args = (matrix.rows(), matrix.columns(), matrix.payload(), (180 * matrix.rotation()) / math.pi, clock.fps())
        print("Matrix [%d:%d], Payload \"%s\", rotation %f (degrees), FPS %f" % print_args)
        a = matrix.payload()
        if a == 'move straight ':
            s1.speed(100)
            s2.speed(-100)
            p_out.low()
            po.low()
        elif a== 'stop' :
            s1.speed(0)
            s2.speed(0)
            p_out.low()
            po.low()
        elif a== 'left' :
            s1.speed(100)
            s2.speed(100)
            p_out.high()
            po.low()
        elif a== 'right' :
            s1.speed(-100)
            s2.speed(-100)
            po.high()
            p_out.low()






