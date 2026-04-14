import sys
from pathlib import Path

sys.path.append(Path(__file__).parents[1].absolute().__str__())
import nokiao_utils_components
from dash import Dash, callback, html, Input, Output, dcc


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Input(id="input-value"),
        dcc.Checklist(
            id="with-time-suffix",
            options=[{"label": "添加时间后缀", "value": "true"}],
            value=[],
        ),
        nokiao_utils_components.CalcHash(
            id="calc-hash",
            value="my-value",
            withTimeSuffix=False,
        ),
        html.Div(id="output", style={"whiteSpace": "pre"}),
    ]
)


@callback(
    [
        Output("calc-hash", "value"),
        Output("calc-hash", "withTimeSuffix"),
    ],
    [
        Input("input-value", "value"),
        Input("with-time-suffix", "value"),
    ],
)
def update_value(value, withTimeSuffix):
    return value, len(withTimeSuffix) > 0


@callback(
    Output("output", "children"),
    Input("calc-hash", "md5Value"),
    Input("calc-hash", "sha256Value"),
    Input("calc-hash", "sha384Value"),
    Input("calc-hash", "sha512Value"),
)
def display_output(md5Value, sha256Value, sha384Value, sha512Value):
    return (
        f"MD5: {md5Value}\n"
        f"SHA256: {sha256Value}\n"
        f"SHA384: {sha384Value}\n"
        f"SHA512: {sha512Value}\n"
    )


if __name__ == "__main__":
    app.run(debug=True)
