"""
    chlorine.translate
    ~~~~~~~~~~~~~~
    :copyright: (c) 2021 by the Fluorine Team.
    :license: GPL-3.0, see LICENSE for more details.
"""

class Translate(object):
    """
    The translation object for chlorine
    """
    def __init__(self, string: str):
        self.to_translate = string

    @staticmethod
    def keywords() -> list:
        """
        The reserved keywords of Chlorine.

        :return: chlorine关键字列表
        """
        return [
            "[",

            "了别", "了当", "了得", "了断",
            "了无", "了愿", "了债", "了办",
            "了事", "了然", "了却", "了结",
            "了解", "了如", "了不得", "了不起",
            "说了算", "铁了心", "铁了事", "开了窍",
            "没了", "乱了套", "横了心", "不了",
            "不甚了然", "知了", "完了", "算了",
            "罢了", "肿么了", "过奖了", "好极了",
            "大不了", "免不了",

            "地面", "的地", "有地", "地球",
            "地空", "地名", "地貌", "地区",
            "地理", "地块", "地形", "地势",
            "地位", "地图", "地铁", "地狱",
            "地盘", "地皮", "地坪", "地上",
            "地点", "地带", "地方", "地缝",
            "地瓜", "地火", "地精", "地库",
            "地雷", "地址", "地震", "地质",
            "地下", "地产", "地层", "地板",
            "地表", "地暖", "土地", "天地",
            "田地", "境地", "圈地", "外地",
            "洼地", "入地", "异地", "盆地",
            "平地", "湿地", "圣地", "实地",
            "腹地", "各地", "工地", "高地",
            "耕地", "该地", "海地", "基地",
            "绝地", "接地", "空地", "落地",
            "领地", "绿地", "陆地", "林地",
            "之地", "阵地", "占地", "质地",
            "驻地", "场地", "产地", "此地",
            "草地", "本地", "白地", "内地",
            "拿地", "农地", "墓地", "某地",

            "得体", "得意", "得到", "得分",
            "得过", "得很", "得奖", "得空",
            "得了", "得证", "得知", "得罪",
            "得主", "得出", "取得", "赢得",
            "使得", "锻得", "懂得", "获得",
            "觉得", "解得", "记得", "懒得",
            "值得", "显得", "测得", "变得",
            "不得", "彼得", "难得", "没得",
            "免得",
            
            "可的", "打的", "的卢",

            # Comments from https://bilibili.com/
            "考古", "梦开始的地方", "泪目", "十个泪目九个笑，还有一个在狂笑",
            "十个泪目一个笑，还有九个在狂笑", "公屏",
            "核善", "核平", "核蔼", "以核为贵",
            "蘑菇蛋", "蘑菇弹", "以核服人", "以德服人",
            "以理服人",
            "有生之年", "爷青回", "爷青结", "失踪人口回归",
            "up主", "UP主", "Up主", "零零后",
            "00后", "鸽视频", "阿婆主",
            "富贵色", "会员色",
            "字母君", "字幕菌", "野生字幕菌",
            "哈哈哈哈", "红红火火恍恍惚惚",

            "啊我死了", "awsl", "AWSL", "Awsl",
            "阿伟死了", "阿伟瘦了", "啊我是驴",

            "武汉加油", "有内味了", "双厨狂喜", "爷青回",
            "禁止套娃",

            "xswl", "XSWL", "Xswl", "hhh",
            "lol", "LOL", "Lol", "rofl",
            "Rofl", "ROFL", "Hahaha", "hahaha",
            "HaHaHa", "HAHAHA",
            
            "哔哩哔哩", "bilibili", "Bilibili", "BiliBili",
            "BILIBILI",

            # Hot funs
            "发生肾么事了", "发生甚么事了",
            "把颈椎练坏了",
            "年轻人不讲武德", "不讲武德", "有备而来",
            "来骗", "来偷袭", "耗子尾汁",
            "闪电五连鞭",
            "金坷垃", "奥利给",

            "亿遍", "亿点点",
            "橘里橘气", "紫气东来", "磕到了",
        ]

    def translate(self) -> str:
        """
        to translate the string.
        """
        keywords = self.keywords()
        string = self.to_translate
        for item in range(len(keywords)):
            string = string.replace(keywords[item], f'[$@{item}]')

        # translate ready (translation algorithm)
        notFormal = { # not formal uses of chinese

        # keys:   formal
        # values: informal
        # algorithm to translate items in values(list) to their keys

            '什么': ['啥','啥子','肾么','甚么'],
            '怎么': ['咋'],
            '炒饭': ['抄饭','吵饭'],
            '充气': ['冲气'],
            '零售': ['另售'],
            '装潢': ['装璜','装黄'],
            '盒饭': ['合饭'],
            '菠萝': ['波萝'],
            '鸡蛋': ['鸡但','鸡旦'],
            '停车': ['仃车'],
        }
        for item in notFormal.keys():
            for ni in notFormal[item]:
                string = string.replace(ni,item)

        # after translate
        for item in range(len(keywords)):
            string = string.replace(f'[$@{item}]', keywords[item])
        return string