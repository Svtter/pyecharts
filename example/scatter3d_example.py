import json
import os
import random

from pyecharts import options as opts
from pyecharts.charts import Page, Scatter3D
from pyecharts.faker import Collector, Faker

C = Collector()


@C.funcs
def scatter3d_base() -> Scatter3D:
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
        .add("", data)
        .set_global_opts(
            title_opts=opts.TitleOpts("Scatter3D-基本示例"),
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color),
        )
    )
    return c


@C.funcs
def scatter3d_muti_visualmap_channel() -> Scatter3D:
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
        .add("", data)
        .set_global_opts(
            title_opts=opts.TitleOpts("Scatter3D-多视觉映射通道"),
            visualmap_opts=[
                opts.VisualMapOpts(range_color=Faker.visual_color),
                opts.VisualMapOpts(type_="size", range_size=[10, 50], pos_top="20%"),
            ],
        )
    )
    return c


@C.funcs
def scatter3d_with_dataset() -> Scatter3D:
    with open(
        os.path.join("fixtures", "life-expectancy-table.json"), "r", encoding="utf-8"
    ) as f:
        j = json.load(f)

    c = (
        Scatter3D()
        .add_dataset(
            dimensions=[
                "Income",
                "Life Expectancy",
                "Population",
                "Country",
                {"name": "Year", "type": "ordinal"},
            ],
            source=j,
        )
        .add(
            series_name="",
            data=None,
            encode={
                "x": "Country",
                "y": "Life Expectancy",
                "z": "Income",
                "tooltip": [0, 1, 2, 3, 4],
            }
        )
    )
    return c


Page().add(*[fn() for fn, _ in C.charts]).render()
