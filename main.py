from manim import *

class Presentacion(Scene):
    def construct(self):
        titulo = Text("Evaluación Integrada de Desempeño", font_size=32)
        sub = Text("Cálculo Intermedio - Grupo 12", font_size=28, color=BLUE)
        tema = Text("Tema: Sumas inferiores y superiores", font_size=24, color=YELLOW)
        
        grupo_txt = VGroup(titulo, sub, tema).arrange(DOWN, buff=0.5)
        
        self.play(Write(grupo_txt))
        self.wait(2)
        self.play(FadeOut(grupo_txt))

class Simbolos(Scene):
    def construct(self):
        simbolo_intervalo = MathTex("[a, b]", font_size=90, color=BLUE)
        simbolo_n = MathTex("n", font_size=90, color=YELLOW)
        simbolo_delta = MathTex(r"\Delta x", font_size=90, color=GREEN)
        simbolo_sigma = MathTex(r"\Sigma", font_size=90, color=RED)

        grupo_simbolos = VGroup(
            simbolo_intervalo, 
            simbolo_n, 
            simbolo_delta, 
            simbolo_sigma
        ).arrange(RIGHT, buff=1.5)

        for simbolo in grupo_simbolos: 
            self.play(FadeIn(simbolo), run_time=1.5)
            self.wait(3)      

        self.play(FadeOut(grupo_simbolos))

class TeoriaYEjemplo(Scene):
    def construct(self):
        # 1. Lógica matemática
        def f(x): 
            return 4 - x**2

        def delta_x(n, a=0, b=2): 
            return (b - a) / n

        def particion(n, a=0, b=2):
            dx = delta_x(n, a, b)
            return [a + i * dx for i in range(n + 1)]

        def suma_inferior(n, a=0, b=2):
            xs = particion(n, a, b)
            dx = delta_x(n, a, b)
            return sum(f(xs[i]) * dx for i in range(1, n + 1))

        def suma_superior(n, a=0, b=2):
            xs = particion(n, a, b)
            dx = delta_x(n, a, b)
            return sum(f(xs[i - 1]) * dx for i in range(1, n + 1))

        # 2. Presentación de Conceptos y Parámetros
        titulo = Tex("Teoría y Ejemplo: Sumas de Riemann", font_size=40, color=BLUE)
        funcion_txt = MathTex(r"\text{Función: } f(x) = 4 - x^2", font_size=36)
        intervalo_txt = MathTex(r"\text{Intervalo: } [a, b] = [0, 2]", font_size=36)
        
        grupo_base = VGroup(titulo, funcion_txt, intervalo_txt).arrange(DOWN, buff=0.3)
        
        self.play(FadeIn(grupo_base))
        self.play(grupo_base.animate.to_edge(UP))
        self.wait(1)
        
        # 3. Cálculo interactivo mostrando los parámetros variables
        casos_n = [4, 8, 32]
        resultados_actuales = VGroup()
        
        for n in casos_n:
            dx_val = delta_x(n)
            L_n = round(suma_inferior(n), 5)
            U_n = round(suma_superior(n), 5)
            
            # Se explican los parámetros n y Δx exigidos por la rúbrica
            texto_parametros = MathTex(
                f"n = {n} \\text{{ subintervalos}} \\qquad \\Delta x = {dx_val} \\text{{ (base)}}", 
                font_size=32, color=YELLOW
            )
            texto_ln = MathTex(f"L_{{{n}}} = {L_n} \\quad \\text{{(Suma Inferior)}}", font_size=34, color=RED)
            texto_un = MathTex(f"U_{{{n}}} = {U_n} \\quad \\text{{(Suma Superior)}}", font_size=34, color=GREEN)
            
            grupo_resultados = VGroup(texto_parametros, texto_ln, texto_un).arrange(DOWN, buff=0.5)
            grupo_resultados.next_to(grupo_base, DOWN, buff=0.8)
            
            if n == 4:
                self.play(FadeIn(grupo_resultados))
                resultados_actuales = grupo_resultados
            else:
                self.play(Transform(resultados_actuales, grupo_resultados))
            self.wait(2)
            
        # 4. Acumulación e Integración (Cierre matemático)
        self.play(FadeOut(grupo_base[1:])) # Oculta función e intervalo para limpiar pantalla
        texto_exacto = MathTex(r"\int_0^2 (4 - x^2) \, dx = \frac{16}{3} \approx 5.33333", font_size=42, color=BLUE)
        
        self.play(Transform(resultados_actuales, texto_exacto))
        self.wait(3)
    
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

class ConclusionYCierre(Scene):
    def construct(self):
        pregunta = Text("¿Cómo podemos encerrar el valor de una región?", font_size=24, color=BLUE)
        concl = Text("El área real se acota entre las sumas inferiores y superiores.", font_size=22)
        limite = MathTex("\\lim_{n \\to \\infty} S_n = \\int_{0}^{2} (4 - x^2) dx", color=YELLOW)
        
        bloque = VGroup(pregunta, concl, limite).arrange(DOWN, buff=0.6)
        
        self.play(Write(pregunta))
        self.wait(1)
        self.play(Write(concl), Write(limite))
        self.wait(2)
