from manim import *

import numpy as np

i = RIGHT
j = UP
k = IN


def track_obj(tex, obj):
    tex.move_to(obj.get_end())
    tex.add_updater(lambda m: m.move_to(obj.get_end()))
    return tex


def format_vector(name, vector: Vector) -> str:
    return """\mathbf{%s} = %.2f\hat{i} + %.2f\hat{j} + %.2f\hat{k}""" % (
        name,
        *list(vector.get_vector()),
    )


def track_vector(obj: MathTex, name: str, vector: Vector):
    obj.add_updater(lambda m: m.become(MathTex(name, vector)))
    return obj


_v1 = 2 * i + 2 * j + 2 * k
_v2 = -2 * i - 3 * j - k
_n = np.cross(_v1, _v2)


class Demonstration(ThreeDScene):
    def construct(self):
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
        # v1_text = track_vector(MathTex(format_vector("a", v1)), "a", v1)
        # self.add_fixed_in_frame_mobjects(v1_text)
        # v1_text.to_corner(UL)
        self.add(track_obj(MathTex("\mathbf{a}", color=RED), v1))

        self.play(Write(v2))
        self.add(track_obj(MathTex("\mathbf{b}", color=BLUE), v2))

        self.play(Write(n))
        self.add(track_obj(MathTex("\hat{\mathbf{n}}", color=GREEN), n))

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)
        self.stop_ambient_camera_rotation()

        self.begin_ambient_camera_rotation(rate=0.1, about="phi")
        self.wait(5)
        self.stop_ambient_camera_rotation(about="phi")
        self.wait()
        self.play(Rotate(v1, angle=PI, axis=_v2, about_point=ORIGIN), run_time=3.5)

        self.begin_ambient_camera_rotation(rate=-0.1, about="phi")
        self.wait(6)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)
        self.stop_ambient_camera_rotation()
        self.stop_ambient_camera_rotation(about="phi")

        self.clear()


class Explanation(Scene):
    def construct(self):
        a_hat = MathTex("\hat{\mathbf{a}} = a_1 \hat{\mathbf{i}} + b_1 \hat{\mathbf{j}} + c_1 \hat{\mathbf{k}}")
        self.play(Write(a_hat))
        self.play(a_hat.animate.to_corner(UL))
        self.wait(1)
        n_hat = MathTex("\hat{\mathbf{n}} = a_2 \hat{\mathbf{i}} + b_2 \hat{\mathbf{j}} + c_2 \hat{\mathbf{k}}")
        self.play(Write(n_hat))
        self.play(n_hat.animate.to_corner(UL).shift(DOWN))
        self.wait(1)

        # v1 = MathTex(format_vector("a", Vector(_v1)))
        # self.play(Write(v1))
        # self.play(v1.animate.to_corner(UL))
        # self.wait(10)
