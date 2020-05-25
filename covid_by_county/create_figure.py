#!/usr/bin/env python

import argparse
import asyncio
import json

import plotly.graph_objects as go

import covid_by_county.config as app_config

geodata = app_config.configuration.geodata


def create_figure(df, date):

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


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('df')
    parser.add_argument('date')
    return parser.parse_args(args)


async def main(args):
    print(args)
    return create_figure(args.df, args.date)

if __name__ == '__main__':
    import sys
    asyncio.run(main(sys.argv[1:]))
