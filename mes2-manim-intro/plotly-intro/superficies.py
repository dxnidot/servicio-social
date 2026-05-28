import plotly.graph_objects as go
import numpy as np

# ================================================
# 1. CINTA DE MOBIUS interactiva
# ================================================
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 30)
u, v = np.meshgrid(u, v)

R = 2
x = (R + v/2 * np.cos(u/2)) * np.cos(u)
y = (R + v/2 * np.cos(u/2)) * np.sin(u)
z = v/2 * np.sin(u/2)

mobius = go.Surface(
    x=x, y=y, z=z,
    colorscale=[[0, '#1de9b6'], [1, '#ff6b6b']],
    opacity=0.9,
    showscale=False,
    name='Cinta de Mobius'
)

# ================================================
# 2. TORO interactivo
# ================================================
u2 = np.linspace(0, 2*np.pi, 60)
v2 = np.linspace(0, 2*np.pi, 60)
u2, v2 = np.meshgrid(u2, v2)

R2, r2 = 3, 1
x2 = (R2 + r2*np.cos(v2)) * np.cos(u2)
y2 = (R2 + r2*np.cos(v2)) * np.sin(u2)
z2 = r2 * np.sin(v2)

toro = go.Surface(
    x=x2, y=y2, z=z2,
    colorscale=[[0, '#4169E1'], [1, '#9b59b6']],
    opacity=0.9,
    showscale=False,
    name='Toro'
)

# ================================================
# 3. PARABOLOIDE interactivo
# ================================================
u3 = np.linspace(-2, 2, 50)
v3 = np.linspace(-2, 2, 50)
u3, v3 = np.meshgrid(u3, v3)
z3 = u3**2 + v3**2

paraboloide = go.Surface(
    x=u3, y=v3, z=z3,
    colorscale=[[0, '#FFD700'], [1, '#FF8C00']],
    opacity=0.9,
    showscale=False,
    name='Paraboloide'
)

# ================================================
# FIGURA CON BOTONES PARA CAMBIAR SUPERFICIE
# ================================================
fig = go.Figure(data=[mobius])

fig.update_layout(
    title=dict(
        text='Superficies Parametricas — Servicio Social ESCOM',
        font=dict(size=18)
    ),
    paper_bgcolor='#0a0a12',
    plot_bgcolor='#0a0a12',
    font=dict(color='white'),
    scene=dict(
        bgcolor='#0a0a12',
        xaxis=dict(gridcolor='#1a3a55', zerolinecolor='#5588aa'),
        yaxis=dict(gridcolor='#1a3a55', zerolinecolor='#5588aa'),
        zaxis=dict(gridcolor='#1a3a55', zerolinecolor='#5588aa'),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1))
    ),
    updatemenus=[
        dict(
            type='buttons',
            direction='right',
            x=0.5, xanchor='center',
            y=1.08, yanchor='top',
            buttons=[
                dict(
                    label='Cinta de Mobius',
                    method='restyle',
                    args=[{
                        'x': [x], 'y': [y], 'z': [z],
                        'colorscale': [[[0, '#1de9b6'], [1, '#ff6b6b']]]
                    }]
                ),
                dict(
                    label='Toro',
                    method='restyle',
                    args=[{
                        'x': [x2], 'y': [y2], 'z': [z2],
                        'colorscale': [[[0, '#4169E1'], [1, '#9b59b6']]]
                    }]
                ),
                dict(
                    label='Paraboloide',
                    method='restyle',
                    args=[{
                        'x': [u3], 'y': [v3], 'z': [z3],
                        'colorscale': [[[0, '#FFD700'], [1, '#FF8C00']]]
                    }]
                ),
            ],
            bgcolor='#1a3a55',
            bordercolor='#5588aa',
            font=dict(color='white')
        )
    ]
)

fig.show()
print("Abre en el navegador — puedes rotar, hacer zoom y cambiar superficie!")