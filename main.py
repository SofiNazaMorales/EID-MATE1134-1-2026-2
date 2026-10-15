from manim import *

class VisualizacionSumas(Scene):
    def construct(self):
        ejes = Axes(
            x_range=[-0.5, 3, 0.5],
            y_range=[-1, 5, 1],
            axis_config={"include_numbers": True}
        )

        curva = ejes.plot(lambda x: 4 - x**2, x_range=[0, 2], color=BLUE)
        etiqueta = ejes.get_graph_label(curva, label="f(x) = 4 - x^2", x_val=1.5, direction=UR)

        self.play(Create(ejes))
        self.play(Create(curva), Write(etiqueta))
        self.wait(1)

        valores_n = [4, 8, 16, 32]

        #sumas inferiores  (evaluacion por la derecha)
        rects_inf = VGroup()
        for n in valores_n:
            dx = 2 / n
            nuevos_rects = ejes.get_riemann_rectangles(
                curva, x_range=[0, 2], dx=dx, input_sample_type="right", color=RED, fill_opacity=0.5
            )
            if n == 4:
                self.play(Create(nuevos_rects))
                rects_inf = nuevos_rects
            else:
             
                self.play(Transform(rects_inf, nuevos_rects))
            self.wait(1)
            
        self.play(FadeOut(rects_inf))
        self.wait(0.5)

        #sumas superiores (evaluacion por la izquierda)
        rects_sup = VGroup()
        for n in valores_n:
            dx = 2 / n
            nuevos_rects = ejes.get_riemann_rectangles(
                curva, x_range=[0, 2], dx=dx, input_sample_type="left", color=GREEN, fill_opacity=0.5
            )
            if n == 4:
                self.play(Create(nuevos_rects))
                rects_sup = nuevos_rects
            else:
                self.play(Transform(rects_sup, nuevos_rects))
            self.wait(1)

        self.wait(2)