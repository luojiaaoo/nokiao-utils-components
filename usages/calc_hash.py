import sys
from pathlib import Path

sys.path.append(Path(__file__).parents[1].absolute().__str__())
import nokiao_utils_components
from dash import Dash, callback, html, Input, Output


app = Dash(__name__)

app.layout = html.Div(
    [
        nokiao_utils_components.CalcHash(
            id="input", value="my-value", label="my-label"
        ),
        html.Div(id="output"),
    ]
)


@callback(Output("output", "children"), Input("input", "value"))
def display_output(value):
    return "You have entered {}".format(value)


if __name__ == "__main__":
    app.run(debug=True)
