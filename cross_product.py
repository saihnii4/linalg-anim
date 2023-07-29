from manim import *

import numpy as np

i = RIGHT
j = UP
k = IN


def follow_tex(tex, obj):
    tex.move_to(obj.get_end())
    tex.add_updater(lambda m: m.move_to(obj.get_end()))
    return tex


class SkewLines(ThreeDScene):
    def construct(self):
        _v1 = 2 * i + 2 * j + 2 * k
        _v2 = -i + 3j + k
        _n = np.cross(_v1, _v2)
        v1 = Vector(_v1, color=RED)
        v2 = Vector(_v2, color=BLUE)
        n = Vector(_n, color=GREEN)
        n.add_updater(
            lambda m: m.become(
                Vector(np.cross(v1.get_vector(), v2.get_vector()), color=GREEN)
            )
        )
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        self.add(axes)
        self.pause(2)
        self.play(Write(v1))
        self.add(follow_tex(MathTex("\mathbf{a}", color=RED), v1))
        self.play(Write(v2))
        self.add(follow_tex(MathTex("\mathbf{b}", color=BLUE), v2))
        self.play(Write(n))
        self.add(follow_tex(MathTex("\hat{\mathbf{n}}", color=GREEN), n))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.begin_ambient_camera_rotation(rate=0.1, about="phi")
        self.wait(5)
        self.play(Rotate(v2, angle=PI, axis=_v1, about_point=ORIGIN), run_time=3)
        self.stop_ambient_camera_rotation()
        # write code that updates the normal vector variable "n" as v2 rotates
        self.wait(3)
        self.play(Rotate(v1, angle=PI, axis=_v2, about_point=ORIGIN), run_time=3)
