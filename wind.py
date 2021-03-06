from pyecharts import Geo, Page, Style


def create_charts():
    page = Page()
    style = Style(
        width=1400,
        height=700,
        # background_color='#404a95',
        title_color="#000",
    )

    geo_cities_coords = {'北京丰台卢沟桥东管头': [116.32, 39.8], '北京丰台新村': [116.33, 39.72], '北京东城体育馆路国家体育总局': [116.43, 39.65],
                         '北京朝阳南磨房赛洛城': [116.51, 39.6], '河北沧州沧县大官厅小高蔡村': [116.61, 39.56],
                         '河北沧州任丘开发区管理委员会': [116.85, 39.41], '天津武清大孟庄三间房': [116.93, 39.34],
                         '北京平谷刘家店江米洞': [117.01, 39.28], '天津武清南蔡村张羊坊': [117.05, 39.18], '山东济南历下建新花园路': [117.05, 39.15],
                         '河北沧州沧县薛官屯东新开路': [117.06, 39.1], '江西景德镇乐平镇桥': [117.04, 39.01], '山东德州乐陵化楼': [117.02, 38.94],
                         '天津西青辛口郭庄子': [116.99, 38.85], '河北沧州沧县薛官屯西秀女庄': [116.98, 38.77], '天津静海良王庄胡家村': [116.95, 38.68],
                         '山东德州宁津杜集宏治刘': [116.91, 38.6], '安徽淮南潘集祁集曹岗': [116.86, 38.5], '山东德州宁津大曹': [116.83, 38.42],
                         '河北沧州青县清州小张庄': [116.79, 38.36], '山东德州陵城郑家寨公路韩家': [116.74, 38.26], '山东济南长清文昌袁庄': [116.7, 38.12],
                         '河北廊坊大城平舒温村': [116.67, 38.06], '北京顺义牛栏山前晏子': [116.64, 37.97], '山东德州陵城徽王庄薛庄': [116.59, 37.89],
                         '河北沧州东光东光西郭桥': [116.56, 37.81], '河北沧州河间故仙王刁': [116.52, 37.72], '山东济宁汶上郭仓干河头': [116.49, 37.64],
                         '河北沧州河间黎民居东崔村': [116.48, 37.59], '山东济南平阴孝直南李庄': [116.46, 37.51]}
    # attr=list(df['站点'])
    # value=list(df['次数'])
    attr = ['北京丰台卢沟桥东管头', '北京丰台新村', '北京东城体育馆路国家体育总局', '北京朝阳南磨房赛洛城', '河北沧州沧县大官厅小高蔡村', '河北沧州任丘开发区管理委员会', '天津武清大孟庄三间房',
            '北京平谷刘家店江米洞', '天津武清南蔡村张羊坊', '山东济南历下建新花园路', '河北沧州沧县薛官屯东新开路', '江西景德镇乐平镇桥', '山东德州乐陵化楼', '天津西青辛口郭庄子',
            '河北沧州沧县薛官屯西秀女庄', '天津静海良王庄胡家村', '山东德州宁津杜集宏治刘', '安徽淮南潘集祁集曹岗', '山东德州宁津大曹', '河北沧州青县清州小张庄', '山东德州陵城郑家寨公路韩家',
            '山东济南长清文昌袁庄', '河北廊坊大城平舒温村', '北京顺义牛栏山前晏子', '山东德州陵城徽王庄薛庄', '河北沧州东光东光西郭桥', '河北沧州河间故仙王刁', '山东济宁汶上郭仓干河头',
            '河北沧州河间黎民居东崔村', '山东济南平阴孝直南李庄']
    value = [8236, 8516, 1639, 890, 9, 824, 0, 0, 0, 39, 1918, 22253, 1091, 8496, 0, 741, 14818, 19618, 70186, 116, 0,
             0, 0, 0, 5, 70, 23, 380, 3036, 0]
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
    # page.add(chart)

    return chart


# 保存为本地文件
create_charts().render('C:\\Users\\Administrator\\Desktop\\2.html')
# create_charts().render()
