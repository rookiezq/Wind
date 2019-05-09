# Wind
Pyecharts的地理坐标系表示风图
> **注意**：Pyecharts使用的0.5.0，由于1.x版本的代码重构了，但是相关文档没有更新，变更了很多参数，尤其是add方法中的geo_cities_coords

如果安装了1.x版本的建议先卸载然后安装0.5.x版本，还要安装地图包

```bash
# 卸载
pip uninstall pyecharts
# 安装0.5.0
pip install pyecharts==0.5.0
# 安装地图包
pip install echarts-china-counties-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
pip install echarts-china-misc-pypkg
# 全球国家
pip install echarts-countries-pypkg
# 英国
pip install echarts-united-kingdom-pypkg
```

如果不安装地图包就会显示地图不完整或是只显示海南岛 如图

![](https://demon-1258469613.cos.ap-shanghai.myqcloud.com/img/20190509111553.png)

源数据如图 ，保存在excel中 LON为经度，LAT为纬度

![](https://demon-1258469613.cos.ap-shanghai.myqcloud.com/img/20190509110434.png)

利用pandas将数据读取

```python
import pandas as pd 
df=pd.read_excel('C:\\Users\\Administrator\\Desktop\\经纬.xlsx')
# 保留两位小数
df[['LON','LAT']] = df[['LON','LAT']].round(decimals=2)
# 将geo_cities_coords改成json格式
geo_cities_coords={df.iloc[i]['站点']:[df.iloc[i]['LON'],df.iloc[i]['LAT']] for i in range(len(df))}

attr=list(df['站点'])
value=list(df['次数'])
```



利用pyecharts的Geo画坐标系

```python
from pyecharts import Geo, Page, Style

def create_charts():
    page = Page()
    style = Style(
        width=1400,
        height=700,
        # background_color='#404a95',
        title_color="#000",
    )

    chart = Geo("大风次数(>10.8m/s)分布图", **style.init_style)
    chart.add("", attr, value,
              is_visualmap=True,
              type="effectScatter",
              # toolbox显示attr
              tooltip_formatter='{b}',
              label_emphasis_textsize=15,
              label_emphasis_pos='right',
              # 显示value
              is_label_show=True,
              # 地图颜色
              geo_normal_color="#eeeeee",
              # 鼠标指针高亮显示颜色
              geo_emphasis_color="#ffdf33",
              # 高亮显示value颜色
              label_emphasis_textcolor='#000',
              # 左下角区间
              visual_range=[0, 10000],
              # tooltip_text_color='#000',
              # value颜色
              label_text_color='#000',
              # 左下角颜色
              visual_text_color='#000',
              # legend_text_color='#fff',
              # 使用自定义坐标
              geo_cities_coords=geo_cities_coords
              )
    #page.add(chart)

    return chart


# 保存为本地文件
create_charts().render('C:\\Users\\Administrator\\Desktop\\4.html')
# create_charts().render()

```

但是这样画出来显示不正确 我也不知道为什么 显示的是纬度

![](https://demon-1258469613.cos.ap-shanghai.myqcloud.com/img/20190509111914.png)

用[网页版](https://pyecharts.github.io/pyecharts.js-app/#)就显示正常

![](https://demon-1258469613.cos.ap-shanghai.myqcloud.com/img/20190509112138.png)

由于网页版不支持Pandas，所以需要在别的地方将`geo_cities_coords`、`attr`、`value`三个打印出来，然后手动复制赋给变量

完整代码查看[Github](https://github.com/rookiezq/Wind/blob/master/wind.py)
