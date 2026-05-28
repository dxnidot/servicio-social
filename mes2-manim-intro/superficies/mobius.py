from manim import *
import numpy as np

class MobiusStrip(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=-60*DEGREES)

        surface = Surface(
            lambda u, v: np.array([
                (2 + v/2 * np.cos(u/2)) * np.cos(u),
                (2 + v/2 * np.cos(u/2)) * np.sin(u),
                v/2 * np.sin(u/2)
            ]),
            u_range=[0, TAU],
            v_range=[-1, 1],
            resolution=(80, 20),
            checkerboard_colors=[TEAL_D, TEAL_A],
            fill_opacity=1,
            stroke_width=0.3,
            stroke_color=WHITE,
        )

        title = Text("Cinta de Möbius", font_size=36).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)  # ← fix para que el texto no gire

        self.play(Write(title))
        self.play(Create(surface), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(6)