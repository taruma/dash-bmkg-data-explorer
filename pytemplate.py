import plotly.io as pio
import plotly.graph_objects as go
import configparser

# CONFIG
CONFIG_PATH = "config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_PATH)
MAPBOX_TOKEN = config["PLOTLY"]["MAPBOX_TOKEN"]
MAPBOX_TOKEN = None if MAPBOX_TOKEN == "" else MAPBOX_TOKEN

# CHANGE VAR HERE
SOURCE_IMAGE = (
    "https://raw.githubusercontent.com/hidrokit/"
    + "static-assets/main/logo_0.4.0-v1.1/hidrokit-hidrokit/400x100/"
    + "400x100transparent.png"
)
BASED_TEMPLATE = "plotly"
HEATMAP_COLOR = "Blackbody"  # Viridis, Blackbody, Plasma, Blues, Aggrnyl

# TEMPLATE BASED ON
hktemplate = pio.templates[BASED_TEMPLATE]

# GENERAL LAYOUT
hktemplate.layout.hovermode = "x"
hktemplate.layout.images = [
    dict(
        source=SOURCE_IMAGE,
        xref="paper",
        yref="paper",
        x=1,
        y=1.05,
        sizex=0.1,
        sizey=0.2,
        xanchor="right",
        yanchor="bottom",
        name="logo-hidrokit",
    )
]
hktemplate.layout.title = dict(
    xanchor="left",
    yanchor="top",
    x=0,
    y=1,
    xref="paper",
    yref="paper",
    font={"size": 20},
)
hktemplate.layout.margin = dict(l=0, r=0, b=0)
hktemplate.layout.mapbox = dict(
    bearing=0, style="carto-positron", zoom=4, pitch=0, accesstoken=MAPBOX_TOKEN
)
hktemplate.layout.height = 500  # only affects map
hktemplate.layout.showlegend = False
hktemplate.layout.font = {"family": "Neucha"}
hktemplate.layout.hoverlabel = {"font_family": "Neucha"}
hktemplate.layout.xaxis.title = {"font": {"size": 20}, "standoff": 15}
hktemplate.layout.yaxis.title = {"font": {"size": 15}, "standoff": 15}
hktemplate.layout.legend = {
    "yanchor": "top",
    "y": 0.95,
    "xanchor": "left",
    "x": 0.01,
    "orientation": "h",
    "bgcolor": "rgba(0,0,0,0)",
    "font": {"size": 15},
}
# hktemplate.layout.paper_bgcolor = "rgba(0,0,0,0)"
# hktemplate.layout.plot_bgcolor = "rgba(0,0,0,0)"

# SPECIFIC PLOT
# SCATTERMAPBOX
hktemplate.data.scattermapbox = [
    go.Scattermapbox(
        mode="markers",
        # marker=go.scattermapbox.Marker(size=10, color="DodgerBlue"),
        marker={
            "size": 10,
            # "color": "DodgerBlue",
            "opacity": 0.7,
        },
        hovertemplate="%{customdata} - %{text}<br>(%{lat:.5f}, %{lon:.5f})<extra></extra>",
        hoverlabel={"font_family": "Neucha"},
    )
]

# HEATMAP
hktemplate.data.heatmap = [
    go.Heatmap(
        colorscale=HEATMAP_COLOR,
        textfont={"family": "Neucha"},
        colorbar={
            "orientation": "v",
            "outlinecolor": "black",
            "outlinewidth": 1,
            # "title": "💯", # BUGGED
        },
        hovertemplate="📅: %{customdata}<br>🆔: %{y}<br>💯: %{z}<extra></extra>",
    )
]

hktemplate.data.scatter = [go.Scatter(mode="lines")]

emtpy_fig = go.Figure(
    data=[{"x": [], "y": []}],
    layout=go.Layout(
        template="none",
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        height=200,
    ),
)

MD_TUTORIAL = """
- Buka situs ini melalui komputer/laptop.
- Navigasi menggunakan plotly:
    - Gunakan berbagai opsi bar yang muncul di kanan atas setiap grafik. 
    - Klik dua kali untuk mereset zoom (saat opsi zoom/pan).
- Untuk memilih pos stasiun bisa dengan: 
    - _Click_ atau _Box/Lasso Select_ _marker_ yang ada di peta. (Tahan Shift untuk memilih lebih dari satu)
    - Dari menu _dropdown_ pilih stasiun atau ketik nama/id stasiun yang ingin dilihat.
- Pilih parameter yang ingin dilihat.
- Klik tombol "Tampilkan Grafik".
"""
