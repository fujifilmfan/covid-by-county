#!/usr/bin/env python

import asyncio
import json
from pathlib import Path
from functools import reduce
import subprocess

import plotly.graph_objects as go
import plotly.io.orca

import covid_by_county.config as app_config
from covid_by_county.data_handler import DataObject

geodata = app_config.configuration.geodata
config = app_config.configuration
orca_config = plotly.io.orca.config
orca_config.timeout = 20


def _create_figure(df, date):

    with open(geodata) as f:
        counties = json.load(f)

    # The following endpoints map to bins 0, 1, 2, 3, 4, 5, 6, 7.
    endpoints = [0, 1, 10, 100, 1000, 10000, 100000, 1000000]
    fips = df['fips']
    values = df['confirmed_bins']
    df['text'] = df['confirmed']

    fig = go.Figure(
        data=go.Choropleth(
            autocolorscale=False,
            colorbar=dict(
                len=0.90,
                tickfont_color='#000000',
                ticktext=endpoints,
                tickvals=list(range(len(endpoints))),
                title='Number of cases',
                title_font_color='#000000',
            ),
            colorscale='Blues',
            geojson=counties,
            hovertext=df['text'],
            locationmode='geojson-id',
            locations=fips,
            marker=dict(
                line_color='black',
                line_width=0.5,
            ),
            showscale=True,
            z=values,
            zmax=7,
            zmin=0,
        )
    )

    fig.update_layout(
        annotations=[
            dict(
                x=1.14,
                yanchor='bottom',
                y=0.96,
                text=date,
                font=dict(
                    color='black',
                    size=16,
                ),
                showarrow=False,
            ),
        ],
        geo=dict(
            resolution=50,
            scope='usa',
        ),
        height=550,
        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10,
        ),
        title=dict(
            font_color='#000000',
            text='Confirmed COVID-19 cases in the United States by county',
            xref='paper',
            y=0.97,
            yanchor='bottom',
            yref='paper',
        ),
        width=1050,
    )

    fig.layout.template = None

    return fig


def show_figures(dataframe_dict):
    for date, df in dataframe_dict.items():
        if df is not None:
            figure = _create_figure(df, date)
            if figure is not None:
                figure.show()


def save_figures(png_dir, data_file):  #data_obj, png_dir):
    # data_obj, png_dir = mytuple
    data_file_path = Path(data_file)
    png_dir_path = Path(png_dir)
    try:
        data_obj = DataObject(data_file_path)
    except AttributeError:
        print(f'{data_file_path} must be a Path object.')
    else:
        date = data_obj.date
        dataframe = data_obj.validated_data

        file_name = ''.join([date, '.png'])
        image_path = Path.joinpath(png_dir_path, file_name)

        if dataframe is not None and not image_path.is_file():
            df = dataframe
            figure = _create_figure(df, date)
            figure.write_image(str(image_path))


async def main(args):
    png_dir = args[0]
    data_file = args[1]
    # print(png_dir)
    print('Before save_figures()')
    save_figures(png_dir, data_file)
    print('After save_figures()')

if __name__ == '__main__':
    import sys
    try:
        print('Executing create_figures.run()')
        asyncio.run(main(sys.argv[1:]))
    except ValueError as e:
        print(e)
