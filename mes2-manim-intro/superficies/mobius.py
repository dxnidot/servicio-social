from manim import *
import numpy as np

class MobiusStrip(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0a0a12"
        self.set_camera_orientation(phi=70*DEGREES, theta=-60*DEGREES)

        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-2, 2, 1],
            x_length=8,
            y_length=8,
            z_length=4,
            axis_config={
                "color": "#5588aa",
                "stroke_width": 2,
                "include_ticks": True,
            },
            tips=True,
        )

        labels = axes.get_axis_labels(
            x_label=Text("x", font_size=24, color=WHITE),
            y_label=Text("y", font_size=24, color=WHITE),
            z_label=Text("z", font_size=24, color=WHITE),
        )

        grid_lines = VGroup()
        for i in range(-3, 4):
            grid_lines.add(Line3D(
                start=np.array([-3, i, -1.5]),
                end=np.array([3, i, -1.5]),
                color="#1a3a55",
                stroke_width=0.8,
            ))
            grid_lines.add(Line3D(
                start=np.array([i, -3, -1.5]),
                end=np.array([i, 3, -1.5]),
                color="#1a3a55",
                stroke_width=0.8,
            ))

        surface = Surface(
            lambda u, v: np.array([
                (2 + v/2 * np.cos(u/2)) * np.cos(u),
                (2 + v/2 * np.cos(u/2)) * np.sin(u),
                v/2 * np.sin(u/2)
            ]),
            u_range=[0, TAU],
            v_range=[-1, 1],
            resolution=(80, 20),
            fill_opacity=0.9,
            stroke_width=0.2,
            stroke_color=WHITE,
        )

        surface.set_fill_by_value(
            axes=axes,
            colors=[
                (ManimColor("#1de9b6"), -1),
                (ManimColor("#ff6b6b"),  1),
            ],
            axis=2
        )

        title = Text("Cinta de Möbius", font_size=36, color=WHITE)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        formula = MathTex(
            r"\vec{r}(u,v) = \left((R + v\cos\tfrac{u}{2})\cos u,\ "
            r"(R + v\cos\tfrac{u}{2})\sin u,\ v\sin\tfrac{u}{2}\right)",
            font_size=22,
            color=WHITE,
        )
        formula.to_corner(UR)
        self.add_fixed_in_frame_mobjects(formula)

        self.add(grid_lines, axes, labels)
        self.play(Write(title), run_time=1)
        self.play(Write(formula), run_time=2)
        self.play(Create(surface), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(8)