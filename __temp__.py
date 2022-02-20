from manimlib.imports import *

class Foo(Scene):
    
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 6, 1],
            tips=False,
        )
        
        # x_min must be > 0 because log is undefined at 0.
        graph = ax.get_graph(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
        self.add(ax, graph)
